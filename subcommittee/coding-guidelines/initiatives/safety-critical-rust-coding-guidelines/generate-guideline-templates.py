#!/usr/bin/env -S uv run
# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

import argparse
import string
import random

# Configuration
CHARS = string.ascii_letters + string.digits
ID_LENGTH = 12

def generate_id(prefix):
    """Generate a random ID with the given prefix."""
    random_part = "".join(random.choice(CHARS) for _ in range(ID_LENGTH))
    return f"{prefix}_{random_part}"

def generate_guideline_template():
    """Generate a complete guideline template with all required sections."""
    # Generate IDs for all sections
    guideline_id = generate_id("gui")
    rationale_id = generate_id("rat")
    bad_example_id = generate_id("bad_ex")
    good_example_id = generate_id("good_ex")
    
    template = f""".. guideline:: Title Here
   :id: {guideline_id}
   :status: draft
   :fls: 
   :tags: 
   :category: 
   :recommendation: 

   Description of the guideline goes here.

   .. rationale:: 
      :id: {rationale_id}
      :status: draft

      Explanation of why this guideline is important.

   .. bad_example:: 
      :id: {bad_example_id}
      :status: draft

      Explanation of code example.
   
      .. code-block:: rust
   
        fn example_function() {{
            // Bad implementation
        }}

   .. good_example:: 
      :id: {good_example_id}
      :status: draft

      Explanation of code example.
   
      .. code-block:: rust
   
        fn example_function() {{
            // Bad implementation
        }}
"""
    return template

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate guideline templates with randomly generated IDs"
    )
    parser.add_argument(
        "-n", 
        "--number-of-templates", 
        type=int, 
        default=1,
        help="Number of templates to generate (default: 1)"
    )
    return parser.parse_args()

def main():
    """Generate the specified number of guideline templates."""
    args = parse_args()
    num_templates = args.number_of_templates
    
    for i in range(num_templates):
        if num_templates > 1:
            print(f"=== Template {i+1} ===\n")
        
        template = generate_guideline_template()
        print(template)
        
        if num_templates > 1 and i < num_templates - 1:
            print("\n" + "=" * 80 + "\n")

if __name__ == "__main__":
    main()
