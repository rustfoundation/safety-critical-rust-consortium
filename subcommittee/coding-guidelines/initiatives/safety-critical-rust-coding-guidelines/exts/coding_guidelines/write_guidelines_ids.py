"""
Module to generate checksums for guidelines and write paragraph-ids.json file.
"""
import hashlib
import json
import logging
import os
from collections import defaultdict
import sphinx
from sphinx_needs.data import SphinxNeedsData

# Get the Sphinx logger
logger = logging.getLogger('sphinx')

def calculate_checksum(content, options):
    """Calculate a SHA-256 checksum of content and options"""
    # Combine content and sorted options
    options_str = json.dumps(options, sort_keys=True)
    combined = content + options_str
    
    # Calculate SHA-256 hash
    hash_obj = hashlib.sha256(combined.encode('UTF-8'))
    return hash_obj.hexdigest()

def write_guidelines_ids(app):
    """
    Write guideline IDs and checksums to JSON file with guidelines as the primary structure.
    
    This collects all guidelines and their directly associated rationale, good example, 
    and bad example, computes checksums for their content, and writes a structured JSON file.
    
    Fails the build if any guideline is missing a rationale, good example, or bad example.
    """
    env = app.env

    data = SphinxNeedsData(env)
    all_needs = data.get_needs_view()
    
# Organize by document
    documents_data = defaultdict(lambda: {
        "title": "",
        "link": "",
        "guidelines": []
    })
    
    # Collect document titles and links
    for docname, title in env.titles.items():
        doc_uri = app.builder.get_target_uri(docname)
        documents_data[docname]["title"] = title.astext()
        documents_data[docname]["link"] = doc_uri
    
    # List to track guidelines with missing elements
    incomplete_guidelines = []
    
    # Process all guidelines
    for need_id, need in all_needs.items():
        if need['type'] == 'guideline':
            docname = need['docname']
            doc_uri = app.builder.get_target_uri(docname)
            
            # Compute checksum for the guideline
            content = need.get('content', '')
            options = {k: v for k, v in need.items() if k not in ('content', 'docname', 'lineno', 'refid', 'content_node')}
            checksum = calculate_checksum(content, options)
            
            # Create guideline structure
            guideline_data = {
                "id": need['id'],
                "title": need.get('title', 'Untitled Guideline'),
                "link": f"{doc_uri}#{need['id']}",
                "checksum": checksum,
                "rationale": None,
                "bad_example": None,
                "good_example": None
            }
            
            # Look for associated elements using parent_needs_back
            missing_elements = []
            
            # Get all needs that have this guideline as their parent
            parent_needs_back = need.get('parent_needs_back', [])
            
            for related_id in parent_needs_back:
                if related_id in all_needs:
                    related_need = all_needs[related_id]
                    related_type = related_need.get('type')
                    
                    # Compute checksum for the related need
                    related_content = related_need.get('content', '')
                    related_options = {k: v for k, v in related_need.items() 
                                     if k not in ('content', 'docname', 'lineno', 'refid', 'content_node')}
                    related_checksum = calculate_checksum(related_content, related_options)
                    
                    # Create the related need data
                    related_data = {
                        "id": related_id,
                        "link": f"{app.builder.get_target_uri(related_need['docname'])}#{related_id}",
                        "checksum": related_checksum
                    }
                    
                    # Add to the appropriate field based on type
                    if related_type == 'rationale':
                        guideline_data["rationale"] = related_data
                    elif related_type == 'bad_example':
                        guideline_data["bad_example"] = related_data
                    elif related_type == 'good_example':
                        guideline_data["good_example"] = related_data
            
            # Check for missing elements
            if guideline_data["rationale"] is None:
                missing_elements.append("rationale")
            if guideline_data["bad_example"] is None:
                missing_elements.append("bad_example")
            if guideline_data["good_example"] is None:
                missing_elements.append("good_example")
            
            # Track incomplete guidelines
            if missing_elements:
                incomplete_guidelines.append({
                    "id": need_id,
                    "title": need.get('title', 'Untitled Guideline'),
                    "missing": missing_elements,
                    "docname": docname
                })
            
            # Add this guideline to the document
            documents_data[docname]["guidelines"].append(guideline_data)
    
    # Prepare the final structure for JSON
    documents = []
    for docname, doc_data in documents_data.items():
        if doc_data["guidelines"]:  # Only include documents with guidelines
            documents.append(doc_data)
    
    # Write the JSON file with the new name
    output_file = os.path.join(app.outdir, "guidelines-ids.json")
    with open(output_file, 'w') as f:
        json.dump({"documents": documents}, f, indent=2)
        f.write("\n")
    
    logger.info(f"Guidelines IDs written to {output_file}")
    
    # Fail the build if we have incomplete guidelines
    if incomplete_guidelines:
        error_message = "The following guidelines are missing required elements:\n\n"
        
        for incomplete in incomplete_guidelines:
            error_message += f"Guideline: {incomplete['id']} ({incomplete['title']})\n"
            error_message += f"Location: {incomplete['docname']}\n"
            error_message += f"Missing: {', '.join(incomplete['missing'])}\n\n"
        
        error_message += "Each guideline must have an associated rationale, good example, and bad example."
        logger.error(error_message)
        raise Exception(error_message)

def build_finished(app, exception):
    """Hook to run at the end of the build process."""
    # The build finished hook also runs when an exception is raised.
    if exception is not None:
        return
    
    logger.info("Generating guidelines IDs and checksums...")
    
    try:
        with sphinx.util.display.progress_message("dumping paragraph ids"):
            write_guidelines_ids(app)
    except Exception as e:
        logger.error(str(e))
        raise

