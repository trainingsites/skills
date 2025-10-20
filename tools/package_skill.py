#!/usr/bin/env python3
"""
Skill Packager - Creates a distributable zip file of a skill folder for Claude upload

Usage:
    python package_skill.py <path/to/skill-folder> [output-directory]

Example:
    python package_skill.py lesson-hook-creator
    python package_skill.py lesson-hook-creator ./dist
"""

import sys
import zipfile
import os
from pathlib import Path

def validate_skill_basic(skill_path):
    """Basic validation before packaging"""
    skill_path = Path(skill_path)
    
    # Check if directory exists
    if not skill_path.exists() or not skill_path.is_dir():
        return False, f"Skill directory not found: {skill_path}"
    
    # Check for SKILL.md
    if not (skill_path / "SKILL.md").exists():
        return False, "SKILL.md not found"
    
    return True, "Basic validation passed"

def package_skill(skill_path, output_dir=None):
    """
    Package a skill folder into a zip file for Claude upload.

    Args:
        skill_path: Path to the skill folder
        output_dir: Optional output directory for the zip file (defaults to current directory)

    Returns:
        Path to the created zip file, or None if error
    """
    skill_path = Path(skill_path).resolve()

    # Validate skill folder exists
    if not skill_path.exists():
        print(f"❌ Error: Skill folder not found: {skill_path}")
        return None

    if not skill_path.is_dir():
        print(f"❌ Error: Path is not a directory: {skill_path}")
        return None

    # Run basic validation
    print("🔍 Validating skill...")
    valid, message = validate_skill_basic(skill_path)
    if not valid:
        print(f"❌ Validation failed: {message}")
        return None
    print(f"✅ {message}\n")

    # Determine output location
    skill_name = skill_path.name
    if output_dir:
        output_path = Path(output_dir).resolve()
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = Path.cwd()

    zip_filename = output_path / f"{skill_name}.zip"

    # Files to exclude from package (internal/creator-only files)
    exclude_patterns = [
        'internal/',
        '__pycache__/',
        '*.pyc',
        '.DS_Store',
        'Thumbs.db',
        '*.tmp'
    ]

    def should_exclude(file_path):
        """Check if file should be excluded from package"""
        relative_path = file_path.relative_to(skill_path)
        path_str = str(relative_path)
        
        for pattern in exclude_patterns:
            if pattern.endswith('/'):
                # Directory pattern
                if path_str.startswith(pattern) or f"/{pattern}" in f"/{path_str}":
                    return True
            else:
                # File pattern
                if path_str.endswith(pattern.replace('*', '')):
                    return True
        return False

    # Create the zip file
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through the skill directory
            for file_path in skill_path.rglob('*'):
                if file_path.is_file() and not should_exclude(file_path):
                    # Calculate the relative path within the zip
                    arcname = file_path.relative_to(skill_path.parent)
                    zipf.write(file_path, arcname)
                    print(f"  Added: {arcname}")

        print(f"\n✅ Successfully packaged skill to: {zip_filename}")
        print(f"📁 Skill is ready for Claude upload!")
        return zip_filename

    except Exception as e:
        print(f"❌ Error creating zip file: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python package_skill.py <path/to/skill-folder> [output-directory]")
        print("\nExample:")
        print("  python package_skill.py lesson-hook-creator")
        print("  python package_skill.py lesson-hook-creator ./dist")
        sys.exit(1)

    skill_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"📦 Packaging skill: {skill_path}")
    if output_dir:
        print(f"   Output directory: {output_dir}")
    print()

    result = package_skill(skill_path, output_dir)

    if result:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
