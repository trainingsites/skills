#!/usr/bin/env python3
"""
Quick validation script for Claude skills
"""

import sys
import os
import re
from pathlib import Path

def validate_skill(skill_path):
    """Basic validation of a skill"""
    skill_path = Path(skill_path)
    
    # Check SKILL.md exists
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "SKILL.md not found"
    
    # Read and validate frontmatter
    content = skill_md.read_text().strip()
    
    # SKILL.md must start with YAML frontmatter
    if not content.startswith('---'):
        return False, "SKILL.md must start with YAML frontmatter (---)"
    
    # Look for YAML frontmatter
    yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not yaml_match:
        return False, "Invalid YAML frontmatter format"
    
    # Extract frontmatter
    frontmatter = yaml_match.group(1)
    
    # Check required fields for Claude upload (minimal)
    required_fields = ['name:', 'description:']
    for field in required_fields:
        if field not in frontmatter:
            return False, f"Missing '{field.rstrip(':')}' in frontmatter"
    
    # Extract name for validation
    name_match = re.search(r'name:\s*(.+)', frontmatter)
    if name_match:
        name = name_match.group(1).strip()
        # Check naming convention (hyphen-case: lowercase with hyphens)
        if not re.match(r'^[a-z0-9-]+$', name):
            return False, f"Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)"
        if name.startswith('-') or name.endswith('-') or '--' in name:
            return False, f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens"

    # Extract and validate description
    desc_match = re.search(r'description:\s*(.+)', frontmatter)
    if desc_match:
        description = desc_match.group(1).strip()
        # Check for angle brackets
        if '<' in description or '>' in description:
            return False, "Description cannot contain angle brackets (< or >)"

    # Check for required files
    required_files = ['HUMAN_README.md', 'QuickStart.md']
    for req_file in required_files:
        if not (skill_path / req_file).exists():
            return False, f"Missing required file: {req_file}"

    return True, "Skill is valid!"

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_skill.py <skill_directory>")
        sys.exit(1)
    
    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)

if __name__ == "__main__":
    main()
