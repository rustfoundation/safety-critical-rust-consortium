# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

# -- Path setup --------------------------------------------------------------

import os
import sys

sys.path.append(os.path.abspath("../exts"))

# -- Project information -----------------------------------------------------

project = 'Safety-Critical Rust Coding Guidelines'
copyright = '2025, Contributors to Coding Guidelines Subcommittee'
author = 'Contributors to Coding Guidelines Subcommittee'
release = '0.1'

# -- General configuration ---------------------------------------------------

# Add sphinx-needs to extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx_needs',
    'coding_guidelines',
]

# Basic needs configuration
needs_id_regex = "^[A-Za-z0-9_]+"
needs_title_optional = True
needs_id_from_title = False
needs_build_json = True

# Configure sphinx-needs
needs_types = [
    {
        "directive": "guideline",
        "title": "Guideline",
        "prefix": "gui_",
        "color": "#BFD8D2", 
        "style": "node"
    },
    {
        "directive": "rationale",
        "title": "Rationale",
        "prefix": "rat_",
        "color": "#DF744A", 
        "style": "node"
    },
    {
        "directive": "good_example",
        "title": "Good Example",
        "prefix": "good_ex_",
        "color": "#729FCF", 
        "style": "node"
    },
    {
        "directive": "bad_example",
        "title": "Bad Example",
        "prefix": "bad_ex_",
        "color": "#729FCF", 
        "style": "node"
    }
]

# Define custom sections for needs
needs_layouts = {
    "guideline": {
        "content": [
            "content",
            "rationale",
            "good_example",
            "bad_example"
        ]
    }
}

# Tell sphinx-needs which sections to render
needs_render_contexts = {
    "guideline": {
        "content": ["content"],
        "extra_content": ["rationale", "bad_example", "good_example"]
    }
}

# Make sure these sections are included in the JSON
needs_extra_sections = ["rationale", "good_example", "bad_example"]

needs_statuses = [
    dict(name="draft", description="This guideline is in draft stage", color="#999999"),
    dict(name="proposed", description="This guideline is proposed for review", color="#FFCC00"),
    dict(name="approved", description="This guideline has been approved", color="#00FF00"),
    dict(name="deprecated", description="This guideline is deprecated", color="#FF0000"),
]

needs_tags = [
    dict(name="security", description="Security-related guideline"),
    dict(name="performance", description="Performance-related guideline"),
    dict(name="readability", description="Readability-related guideline"),
    dict(name="reduce-human-error", description="Reducing human error guideline"),
    dict(name="numerics", description="Numerics-related guideline"),
]

needs_recommendations = [
    dict(name="encouraged", description="This guideline is encouraged", color="#999999"),
    dict(name="required", description="This guideline is required", color="#FFCC00"),
]

# Enable needs export
needs_extra_options = ["category", "recommendation", "fls"]

# -- Options for HTML output -------------------------------------------------

# Configure the theme
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
