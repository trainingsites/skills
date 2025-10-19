# TrainingSites Skills Collection

A collection of Claude AI skills for course creators and educators, built on top of Anthropic's skills framework. This repository contains the TrainingSites brand guidelines skill plus all the Anthropic example skills for reference and learning.

## 🎯 Purpose

This repository serves two purposes:
1. **TrainingSites Custom Skills**: Brand guidelines and workflow skills specifically designed for course creation and educational content
2. **Anthropic Example Skills**: A comprehensive collection of reference skills demonstrating Claude's capabilities

Our custom skills focus on:
- Brand consistency across all course materials  
- Beginner-friendly content design
- Streamlined workflows for course creators
- Professional yet approachable educational content

## 📁 Repository Structure

```
trainingsites/skills/
├── README.md                    # This file
├── trainingsites-brand/        # TrainingSites brand guidelines skill
│   ├── SKILL.md               # Main brand skill file
│   ├── README.md              # Skill documentation
│   └── examples/              # Usage examples
├── algorithmic-art/           # Anthropic example skills
├── brand-guidelines/          # Anthropic brand guidelines
├── canvas-design/             # Anthropic design skills
├── document-skills/           # Anthropic document creation skills
│   ├── docx/                 # Word document skills
│   ├── pdf/                  # PDF manipulation skills
│   ├── pptx/                 # PowerPoint skills
│   └── xlsx/                 # Excel skills
└── [other-anthropic-skills]/  # Additional Anthropic example skills
```

## 🚀 Quick Start

### Using These Skills

1. **Upload to Claude**: Copy the `.md` content from any skill in the `skills/` directory
2. **Reference in Prompts**: Use the skill keywords or reference the skill name in your Claude conversations
3. **Customize**: Modify any skill to match your specific needs

### Example Usage

```
"Using the TrainingSites brand skill, create a Google Doc checklist for beginners learning AI prompting techniques."
```

### Uploading to Claude

1. **Navigate to your skill**: Go to `https://github.com/trainingsites/skills/blob/main/trainingsites-brand/SKILL.md`
2. **Copy raw content**: Click "Raw" and copy all the text
3. **Upload to Claude**: In Claude.ai, go to Profile → Skills → Upload, paste content and save
4. **Reference in conversations**: Simply mention "TrainingSites brand skill" in your prompts

## 📋 Available Skills

### TrainingSites Custom Skills
- **[TrainingSites Brand](trainingsites-brand/)** - Complete brand guidelines with Google Docs integration for course materials

### Anthropic Example Skills
- **[Algorithmic Art](algorithmic-art/)** - Create generative art using p5.js
- **[Brand Guidelines](brand-guidelines/)** - Apply Anthropic's official brand colors and typography
- **[Canvas Design](canvas-design/)** - Create beautiful visual art in PNG and PDF formats
- **[Document Skills](document-skills/)** - Advanced document creation and editing
  - **[DOCX](document-skills/docx/)** - Word document creation and editing
  - **[PDF](document-skills/pdf/)** - PDF manipulation and creation
  - **[PPTX](document-skills/pptx/)** - PowerPoint presentation skills
  - **[XLSX](document-skills/xlsx/)** - Excel spreadsheet skills
- **[Theme Factory](theme-factory/)** - Style artifacts with professional themes
- **[Skill Creator](skill-creator/)** - Guide for creating effective skills

## 🤝 Adding New TrainingSites Skills

To add new TrainingSites-specific skills to this repository:

### File Structure
```
trainingsites-[skill-name]/
├── SKILL.md              # Main skill file (required)
├── README.md             # Skill documentation (required) 
└── examples/             # Usage examples (recommended)
    ├── input-example.txt
    └── output-example.txt
```

### Steps to Add
1. Create new folder following the `trainingsites-[name]` convention
2. Add SKILL.md with proper frontmatter and instructions
3. Include README.md with documentation and use cases
4. Add examples showing real usage
5. Update this main README to list the new skill

### Skill Format
Each SKILL.md should include:
```yaml
---
name: trainingsites-skill-name
description: Clear description of what this skill does and when to use it
---

# Skill content here
```

## 🎓 About TrainingSites

This skills collection is maintained by TrainingSites.io, specializing in beginner-friendly online course creation and AI-powered educational content development.

## 🔗 Links

- [TrainingSites.io](https://trainingsites.io)
- [Brand Guidelines](https://trainingsites.io/docs/trainingsites-brand-details/)
- [Anthropic Skills Documentation](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Original Anthropic Skills Repository](https://github.com/anthropics/skills)

---

**Repository**: `trainingsites/skills`  
**Last Updated**: October 2025  
**Maintained by**: TrainingSites Team
