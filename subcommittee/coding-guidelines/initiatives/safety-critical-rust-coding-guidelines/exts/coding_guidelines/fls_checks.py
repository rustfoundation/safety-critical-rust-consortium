# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

import requests
import logging
import re
import json
from pathlib import Path
from sphinx.errors import SphinxError
from sphinx_needs.data import SphinxNeedsData

# Get the Sphinx logger
logger = logging.getLogger('sphinx')
fls_paragraph_ids_url = "https://spec.ferrocene.dev/paragraph-ids.json"

class FLSValidationError(SphinxError):
    category = "FLS Validation Error"

def check_fls(app, env):
    """Main checking function for FLS validation"""
    # First make sure all guidelines have correctly formatted FLS IDs
    check_fls_exists_and_valid_format(app, env)
    
    # Gather all FLS paragraph IDs from the specification and get the raw JSON
    fls_ids, raw_json_data = gather_fls_paragraph_ids(fls_paragraph_ids_url)
    
    # Error out if we couldn't get the raw JSON data
    if not raw_json_data:
        error_message = f"Failed to retrieve or parse the FLS specification from {fls_paragraph_ids_url}"
        logger.error(error_message)
        raise FLSValidationError(error_message)
    
    # Check for differences against lock file
    has_differences, differences = check_fls_lock_consistency(app, env, raw_json_data)
    if has_differences:
        error_message = "The FLS specification has changed since the lock file was created:\n"
        for diff in differences:
            error_message += f"  - {diff}\n"
        error_message += "\nPlease manually inspect FLS spec items whose checksums have changed as corresponding guidelines may need to account for these changes."
        logger.error(error_message)
        raise FLSValidationError(error_message)
    
    # Check if all referenced FLS IDs exist
    check_fls_ids_correct(app, env, fls_ids)
    
    # Read the ignore list
    fls_id_ignore_list = read_fls_ignore_list(app)
    
    # Insert coverage information into fls_ids
    insert_fls_coverage(app, env, fls_ids)
    
    # Calculate and report coverage
    coverage_data = calculate_fls_coverage(fls_ids, fls_id_ignore_list)
    
    # Log coverage report
    log_coverage_report(coverage_data)


def read_fls_ignore_list(app):
    """Read the list of FLS IDs to ignore from a file"""
    ignore_file_path = app.confdir / 'fls_ignore_list.txt'
    ignore_list = []
    
    if ignore_file_path.exists():
        logger.info(f"Reading FLS ignore list from {ignore_file_path}")
        with open(ignore_file_path, 'r') as f:
            for line in f:
                # Remove comments and whitespace
                line = line.split('#')[0].strip()
                if line:
                    ignore_list.append(line)
        logger.info(f"Loaded {len(ignore_list)} FLS IDs to ignore")
    else:
        logger.warning(f"No FLS ignore list found at {ignore_file_path}")
    
    return ignore_list


def check_fls_exists_and_valid_format(app, env):
    logger.debug("check_fls_exists_and_valid_format")

    data = SphinxNeedsData(env)

    needs = data.get_needs_view()
    logger.debug(f"Checking needs {needs!r}")

    # Regular expression for FLS ID validation
    # Format: fls_<12 alphanumeric chars including upper and lowercase>
    fls_pattern = re.compile(r'^fls_[a-zA-Z0-9]{9,12}$')
    for need_id, need in needs.items():
        logger.debug(f"ID: {need_id}, Need: {need}")

        if need.get('type') == 'guideline':
            fls_value = need.get("fls")
            
            # Check if fls field exists and is not empty
            if fls_value is None:
                msg = f"Need {need_id} has no fls field"
                logger.error(msg)
                raise FLSValidationError(msg)
                
            if fls_value == "":
                msg = f"Need {need_id} has empty fls field"
                logger.error(msg)
                raise FLSValidationError(msg)
            
            # Validate FLS ID format
            if not fls_pattern.match(fls_value):
                msg = f"Need {need_id} has invalid fls format: '{fls_value}'. Expected format: fls_ followed by 12 alphanumeric characters"
                logger.error(msg)
                raise FLSValidationError(msg)

    
def check_fls_ids_correct(app, env, fls_ids):
    """
    Check that all FLS IDs referenced in guidelines actually exist in the specification.
    
    Args:
        app: The Sphinx application
        env: The Sphinx environment
        fls_ids: Dictionary of FLS paragraph IDs mapped to their source URLs
    """
    logger.debug("check_fls_ids_correct")
    data = SphinxNeedsData(env)
    needs = data.get_needs_view()
    
    # Track any errors found
    invalid_ids = []
    
    # Check each guideline's FLS reference
    for need_id, need in needs.items():
        if need.get('type') == 'guideline':
            fls_value = need.get("fls")
            
            # Skip needs we already validated format for
            if fls_value is None or fls_value == "":
                continue
                
            # Check if the FLS ID exists in the gathered IDs
            if fls_value not in fls_ids:
                invalid_ids.append((need_id, fls_value))
                logger.warning(f"Need {need_id} references non-existent FLS ID: '{fls_value}'")
    
    # Raise error if any invalid IDs were found
    if invalid_ids:
        error_message = "The following needs reference non-existent FLS IDs:\n"
        for need_id, fls_id in invalid_ids:
            error_message += f"  - Need {need_id} references '{fls_id}'\n"
        logger.error(error_message)
        raise FLSValidationError(error_message)
    
    logger.info("All FLS references in guidelines are valid")


def gather_fls_paragraph_ids(json_url):
    """
    Gather all Ferrocene Language Specification paragraph IDs from the paragraph-ids.json file,
    including both container section IDs and individual paragraph IDs.
    
    Args:
        json_url: The URL or path to the paragraph-ids.json file
        
    Returns:
        Dictionary mapping paragraph IDs to metadata AND the complete raw JSON data
    """
    logger.info("Gathering FLS paragraph IDs from %s", json_url)
    
    # Dictionary to store all FLS IDs and their metadata
    all_fls_ids = {}
    raw_json_data = None
    
    try:
        # Load the JSON file
        response = requests.get(json_url)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Parse the JSON data
        try:
            raw_json_data = response.json()
            data = raw_json_data  # Keep reference to the original data
            logger.debug("Successfully parsed JSON data")
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON: {e}")
            logger.debug(f"Response content preview: {response.text[:500]}...")
            raise
        
        # Check if we have the expected document structure
        if 'documents' not in data:
            logger.error("JSON does not have 'documents' key")
            logger.debug(f"JSON keys: {list(data.keys())}")
            return {}, None
        
        # Base URL for constructing direct links
        base_url = "https://spec.ferrocene.dev/"
        
        # Process each document in the JSON structure
        for document in data['documents']:
            doc_title = document.get('title', 'Unknown')
            doc_link = document.get('link', '')
            
            # Process each section in the document
            for section in document.get('sections', []):
                section_title = section.get('title', 'Unknown')
                section_id = section.get('id', '')
                section_number = section.get('number', '')
                section_link = section.get('link', '')
                is_informational = section.get('informational', False)
                
                # Add the section container ID if it starts with 'fls_'
                if section_id and section_id.startswith('fls_'):
                    direct_url = f"{base_url}{section_link}"
                    
                    # Store section metadata
                    all_fls_ids[section_id] = {
                        "url": direct_url,
                        "section_id": section_number,
                        "document_title": doc_title,
                        "section_title": section_title,
                        "section_number": section_number,
                        "is_container": True,  # Mark as a container/section
                        "informational": is_informational
                        # Note: No checksum for container IDs
                    }
                
                # Process each paragraph in the section
                for paragraph in section.get('paragraphs', []):
                    para_id = paragraph.get('id', '')
                    para_number = paragraph.get('number', '')
                    para_link = paragraph.get('link', '')
                    para_checksum = paragraph.get('checksum', '')
                    
                    # Skip entries without proper IDs
                    if not para_id or not para_id.startswith('fls_'):
                        continue
                    
                    # Create the full URL
                    direct_url = f"{base_url}{para_link}"
                    
                    # Store metadata
                    all_fls_ids[para_id] = {
                        "url": direct_url,
                        "section_id": para_number,
                        "document_title": doc_title,
                        "section_title": section_title,
                        "section_number": section_number,
                        "checksum": para_checksum,
                        "is_container": False,  # Mark as individual paragraph
                        "parent_section_id": section_id if section_id else None
                    }
        
        logger.info(f"Found {len(all_fls_ids)} total FLS IDs (sections and paragraphs)")
        # Count sections vs paragraphs
        sections_count = sum(1 for metadata in all_fls_ids.values() if metadata.get('is_container', False))
        paragraphs_count = len(all_fls_ids) - sections_count
        logger.info(f"  - {sections_count} section/container IDs")
        logger.info(f"  - {paragraphs_count} paragraph IDs")
        
        return all_fls_ids, raw_json_data
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching paragraph IDs from {json_url}: {e}")
        return {}, None

def check_fls_lock_consistency(app, env, fls_raw_data):
    """
    Compare live FLS JSON data with the lock file to detect changes
    
    Args:
        app: The Sphinx application
        env: The Sphinx environment
        fls_raw_data: Raw JSON data from the live specification
        
    Returns:
        Tuple containing:
        - Boolean indicating whether differences were found
        - List of difference descriptions with affected guidelines (for error reporting)
    """
    logger.info("Checking FLS lock file consistency")
    lock_path = app.confdir / 'fls.lock'
    
    # Get the needs data to find affected guidelines
    data = SphinxNeedsData(env)
    needs = data.get_needs_view()
    
    # Map of FLS IDs to guidelines that reference them
    fls_to_guidelines = {}
    for need_id, need in needs.items():
        if need.get('type') == 'guideline':
            fls_value = need.get("fls")
            if fls_value:
                if fls_value not in fls_to_guidelines:
                    fls_to_guidelines[fls_value] = []
                fls_to_guidelines[fls_value].append({
                    'id': need_id,
                    'title': need.get('title', 'Untitled')
                })
    
    # Differences to report
    differences = []
    has_differences = False
    
    # If no lock file exists, skip checking
    if not lock_path.exists():
        logger.warning(f"No FLS lock file found at {lock_path}, skipping consistency check")
        return False, []
    
    try:
        # Load lock file
        with open(lock_path, 'r', encoding='utf-8') as f:
            locked_data = json.load(f)
        
        # Create maps of paragraph IDs to checksums for both live and locked data
        live_checksums = {}
        locked_checksums = {}
        
        # Extract from live data
        for document in fls_raw_data.get('documents', []):
            for section in document.get('sections', []):
                for paragraph in section.get('paragraphs', []):
                    para_id = paragraph.get('id', '')
                    para_checksum = paragraph.get('checksum', '')
                    para_number = paragraph.get('number', '')
                    
                    if para_id and para_id.startswith('fls_'):
                        live_checksums[para_id] = {
                            'checksum': para_checksum,
                            'section_id': para_number
                        }
        
        # Extract from locked data
        for document in locked_data.get('documents', []):
            for section in document.get('sections', []):
                for paragraph in section.get('paragraphs', []):
                    para_id = paragraph.get('id', '')
                    para_checksum = paragraph.get('checksum', '')
                    para_number = paragraph.get('number', '')
                    
                    if para_id and para_id.startswith('fls_'):
                        locked_checksums[para_id] = {
                            'checksum': para_checksum,
                            'section_id': para_number
                        }
        
        logger.info(f"Found {len(live_checksums)} paragraphs in live data")
        logger.info(f"Found {len(locked_checksums)} paragraphs in lock file")
        
        # Format affected guidelines information
        def format_affected_guidelines(fls_id):
            affected = fls_to_guidelines.get(fls_id, [])
            if not affected:
                return "    No guidelines affected"
            
            result = []
            for guideline in affected:
                result.append(f"    - {guideline['id']}: {guideline['title']}")
            return "\n".join(result)
        
        # Look for new IDs
        new_ids = set(live_checksums.keys()) - set(locked_checksums.keys())
        if new_ids:
            for fls_id in sorted(new_ids):
                diff_msg = f"New FLS ID added: {fls_id} ({live_checksums[fls_id]['section_id']})"
                affected_msg = format_affected_guidelines(fls_id)
                differences.append(f"{diff_msg}\n  Affected guidelines:\n{affected_msg}")
            has_differences = True
        
        # Look for removed IDs
        removed_ids = set(locked_checksums.keys()) - set(live_checksums.keys())
        if removed_ids:
            for fls_id in sorted(removed_ids):
                diff_msg = f"FLS ID removed: {fls_id} ({locked_checksums[fls_id]['section_id']})"
                affected_msg = format_affected_guidelines(fls_id)
                differences.append(f"{diff_msg}\n  Affected guidelines:\n{affected_msg}")
            has_differences = True
        
        # Check for checksum changes on existing IDs
        common_ids = set(live_checksums.keys()) & set(locked_checksums.keys())
        for fls_id in sorted(common_ids):
            live_checksum = live_checksums[fls_id]['checksum']
            locked_checksum = locked_checksums[fls_id]['checksum']
            
            changes = []
            
            if live_checksum != locked_checksum:
                changes.append(
                    f"Content changed for FLS ID {fls_id} ({live_checksums[fls_id]['section_id']}): " +
                    f"checksum was {locked_checksum[:8]}... now {live_checksum[:8]}..."
                )
            
            # Also check if section IDs have changed
            live_section = live_checksums[fls_id]['section_id']
            locked_section = locked_checksums[fls_id]['section_id']
            
            if live_section != locked_section:
                changes.append(
                    f"Section changed for FLS ID {fls_id}: {locked_section} -> {live_section}"
                )
            
            if changes:
                affected_msg = format_affected_guidelines(fls_id)
                differences.append(f"{changes[0]}\n  Affected guidelines:\n{affected_msg}")
                
                # Add any additional changes separately
                for i in range(1, len(changes)):
                    differences.append(changes[i])
                
                has_differences = True
        
        if has_differences:
            logger.warning(f"Found {len(differences)} differences between live FLS data and lock file")
        else:
            logger.info("No differences found between live FLS data and lock file")
        
        return has_differences, differences
        
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Error reading or parsing lock file {lock_path}: {e}")
        return False, [f"Failed to read lock file: {e}"]


def insert_fls_coverage(app, env, fls_ids):
    """
    Enrich the fls_ids with whether each FLS ID is covered by coding guidelines
    
    Args:
        app: The Sphinx application
        env: The Sphinx environment
        fls_ids: Dictionary of FLS paragraph IDs with metadata
    """
    logger.debug("Inserting FLS coverage data")
    data = SphinxNeedsData(env)
    needs = data.get_needs_view()
    
    # Initialize coverage for all FLS IDs
    for fls_id in fls_ids:
        fls_ids[fls_id]['covered'] = False
        fls_ids[fls_id]['covering_needs'] = []  # List to store all covering guidelines
        
        # Extract chapter information from section_id (e.g., "22.1:4" -> chapter 22)
        section_id = fls_ids[fls_id]['section_id']
        logger.debug(f"Processing section_id: {section_id} for {fls_id}")
        
        # Handle formats like "22.1:4", "4.3.1:9", or "A.1:2"
        if ':' in section_id:
            # Split at colon to get the section number without paragraph number
            section_parts = section_id.split(':')[0].split('.')
        else:
            # Fallback if no colon present
            section_parts = section_id.split('.')
            
        if section_parts and section_parts[0].isdigit():
            chapter = int(section_parts[0])
            fls_ids[fls_id]['chapter'] = chapter
        else:
            # Handle appendices or other non-standard formats
            first_char = section_id[0] if section_id else None
            if first_char and first_char.isalpha():
                # For appendices like "A.1.1", use the letter as chapter
                fls_ids[fls_id]['chapter'] = first_char
            else:
                fls_ids[fls_id]['chapter'] = 'unknown'
    
    # Mark covered FLS IDs
    unique_covered_ids = set()
    total_references = 0
    
    for need_id, need in needs.items():
        if need.get('type') == 'guideline':
            fls_value = need.get("fls")
            if fls_value and fls_value in fls_ids:
                fls_ids[fls_value]['covered'] = True
                fls_ids[fls_value]['covering_needs'].append(need_id)
                unique_covered_ids.add(fls_value)
                total_references += 1
    
    logger.info(f"Found {total_references} references to FLS IDs in guidelines")
    logger.info(f"Found {len(unique_covered_ids)} unique FLS IDs covered by guidelines")
    return fls_ids


def calculate_fls_coverage(fls_ids, fls_id_ignore_list):
    """
    Calculate coverage statistics for FLS IDs
    
    Args:
        fls_ids: Dictionary of FLS paragraph IDs with metadata, including coverage status
        fls_id_ignore_list: List of FLS IDs to ignore in coverage calculations
    
    Returns:
        Dictionary containing coverage statistics
    """
    logger.debug("Calculating FLS coverage statistics")
    
    # Track statistics
    total_ids = 0
    covered_ids = 0
    ignored_ids = 0
    
    # Organize by chapter
    chapters = {}
    
    # Process each FLS ID
    for fls_id, metadata in fls_ids.items():
        chapter = metadata.get('chapter', 'unknown')
        
        # Initialize chapter data if needed
        if chapter not in chapters:
            chapters[chapter] = {
                'total': 0,
                'covered': 0,
                'ignored': 0,
                'ids': []
            }
        
        # Add to chapter's ID list
        chapters[chapter]['ids'].append(fls_id)
        chapters[chapter]['total'] += 1
        total_ids += 1
        
        # Check if ID should be ignored
        if fls_id in fls_id_ignore_list:
            ignored_ids += 1
            chapters[chapter]['ignored'] += 1
            # Mark as ignored in the original data structure too
            fls_ids[fls_id]['ignored'] = True
        else:
            fls_ids[fls_id]['ignored'] = False
            
            # Count coverage if not ignored
            if metadata.get('covered', False):
                covered_ids += 1
                chapters[chapter]['covered'] += 1
    
    # Calculate coverage percentages
    effective_total = total_ids - ignored_ids
    overall_coverage = (covered_ids / effective_total * 100) if effective_total > 0 else 0
    
    # Calculate chapter coverage
    chapter_coverage = {}
    for chapter, data in chapters.items():
        effective_chapter_total = data['total'] - data['ignored']
        
        if effective_chapter_total == 0:
            # All IDs in this chapter are ignored
            chapter_coverage[chapter] = "IGNORED"
        else:
            chapter_coverage[chapter] = (data['covered'] / effective_chapter_total * 100)
    
    # Sort chapters by custom logic to handle mixed types
    def chapter_sort_key(chapter):
        if isinstance(chapter, int):
            return (0, chapter)  # Sort integers first, by their value
        elif isinstance(chapter, str) and chapter.isalpha():
            return (1, chapter)  # Sort letters second, alphabetically
        else:
            return (2, str(chapter))  # Sort anything else last
    
    sorted_chapters = sorted(chapters.keys(), key=chapter_sort_key)
    
    # Prepare result
    coverage_data = {
        'total_ids': total_ids,
        'covered_ids': covered_ids,
        'ignored_ids': ignored_ids,
        'effective_total': effective_total,
        'overall_coverage': overall_coverage,
        'chapters': sorted_chapters,
        'chapter_data': chapters,
        'chapter_coverage': chapter_coverage
    }
    
    return coverage_data

def log_coverage_report(coverage_data):
    """Log a report of FLS coverage statistics"""
    logger.info("=== FLS Coverage Report ===")
    logger.info(f"Total FLS IDs: {coverage_data['total_ids']}")
    logger.info(f"Covered FLS IDs: {coverage_data['covered_ids']}")
    logger.info(f"Ignored FLS IDs: {coverage_data['ignored_ids']}")
    logger.info(f"Overall coverage: {coverage_data['overall_coverage']:.2f}%")
    
    logger.info("\nCoverage by chapter:")
    for chapter in coverage_data['chapters']:
        coverage = coverage_data['chapter_coverage'][chapter]
        if coverage == "IGNORED":
            logger.info(f"  Chapter {chapter}: IGNORED (all IDs are on ignore list)")
        else:
            logger.info(f"  Chapter {chapter}: {coverage:.2f}%")


