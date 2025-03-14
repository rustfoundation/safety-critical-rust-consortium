import re
import os
import logging
import sphinx

# Get the Sphinx logger
logger = logging.getLogger('sphinx')

def build_finished(app, exception):
    """Hook to run at the end of the build process."""
    # The build finished hook also runs when an exception is raised.
    if exception is not None:
        return
    
    logger.info("Adding FLS links...")
    
    try:
        with sphinx.util.display.progress_message("dumping paragraph ids"):
            post_process_html(app)
    except Exception as e:
        logger.error(str(e))
        raise


def load_fls_ids(app):
    """Load FLS IDs and their URLs."""
    try:
        from . import fls_checks
        fls_ids, _ = fls_checks.gather_fls_paragraph_ids(app.config.fls_paragraph_ids_url)
        return {fls_id: data['url'] for fls_id, data in fls_ids.items()}
    except Exception as e:
        logger.error(f"Failed to load FLS IDs: {e}")
        return {}

def post_process_html(app):
    
    # Load FLS IDs if not already loaded
    if not hasattr(app, 'fls_urls'):
        app.fls_urls = load_fls_ids(app)
    
    # Pattern to match the proper HTML structure
    pattern = r'<span class="needs_fls"><span class="needs_label">fls: </span><span class="needs_data">(fls_[a-zA-Z0-9]{9,12})</span></span>'
    
    # Function to replace FLS IDs with links
    def replace_fls(match):
        """Replace FLS ID with a link if it exists."""
        fls_id = match.group(1)
        
        if fls_id in app.fls_urls:
            return f'<span class="needs_fls"><span class="needs_label">fls: </span><span class="needs_data"><a href="{app.fls_urls[fls_id]}" class="fls-id">{fls_id}</a></span></span>'
        else:
            return f'<span class="needs_fls"><span class="needs_label">fls: </span><span class="needs_data"><span class="fls-id unknown-fls">{fls_id}</span></span></span>'
    
    # CSS for styling
    css = """
/* Styling for FLS ID links */
.fls-id {
    font-family: monospace;
    background-color: rgba(0, 0, 0, 0.05);
    padding: 0.2em 0.4em;
    border-radius: 3px;
    text-decoration: none;
    border-bottom: 1px dotted #666;
}
a.fls-id:hover {
    background-color: rgba(0, 120, 215, 0.1);
    color: #0078d7;
    border-bottom-color: #0078d7;
}
.unknown-fls {
    border-bottom: 1px dashed #cc0000;
    color: #cc0000;
}
"""
    
    # Write CSS file
    css_path = os.path.join(app.outdir, '_static', 'fls_links.css')
    os.makedirs(os.path.dirname(css_path), exist_ok=True)
    with open(css_path, 'w') as f:
        f.write(css)
    
    # Process all HTML files
    for root, _, files in os.walk(app.outdir):
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                
                # Read HTML content
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace FLS IDs with links
                modified = re.sub(pattern, replace_fls, content)
                
                # Add CSS link if needed
                if modified != content and '<link rel="stylesheet" href="_static/fls_links.css"' not in modified:
                    # Fix path to CSS file based on file location relative to outdir
                    rel_path = os.path.relpath(app.outdir, os.path.dirname(filepath))
                    css_path = os.path.join(rel_path, '_static', 'fls_links.css').replace('\\', '/')
                    
                    modified = modified.replace('</head>', 
                                             f'<link rel="stylesheet" href="{css_path}" type="text/css" />\n</head>')
                
                # Write modified content back
                if modified != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(modified)
                    logger.debug(f"Updated FLS links in {filepath}")
