# Prompt Engineering Documentation

This document captures the conversation and prompts that led to the creation of sync-guardian. It serves as both documentation and an educational resource for those interested in the development process.

## Initial Problem Statement

The project started with this user story:

```
From a friend of mine:

I purchased a subscription to Microsoft Office to get a OneDrive so I could keep my PCs synced. I work a lot with #rstats code, so it keeping my analysis directory synced is really important. Anyway, OneDrive frequently fails to do this (among other things). OneDrive, it's your only job!
```

Request: "Can we please help this friend with a python code for keeping a directory in sync with another, plus a Windows Task cron job?"

## Development Sequence

### 1. Core Implementation
First prompt: Request for Python code for directory synchronization and Windows Task scheduling.
- Resulted in the creation of the core DirectorySync class
- Included Windows Task Scheduler setup instructions

### 2. Testing Implementation
Second prompt: "Can you please unit test this?"
- Led to comprehensive test suite creation
- Included multiple test cases for various scenarios

### 3. Repository Setup
Third prompt: "Could you please suggest a name for this Github repository?"
- Multiple suggestions provided
- "sync-guardian" was chosen for its creative and descriptive nature

### 4. Repository Structure
Fourth prompt: "Please, proceed with these 4 tasks."
- Created README.md
- Added LICENSE (MIT)
- Added .gitignore
- Created requirements.txt
- Established proper project structure

### 5. Attribution
Fifth prompt: "How can I attribute credit to you?"
- Added acknowledgment to README.md crediting Claude (Anthropic)

### 6. Repository Description
Sixth prompt: "A small description for the repo tagline, please?"
- Created concise tagline focusing on key features and purpose

### 7. Documentation of Development Process
Seventh prompt: "I would like to document as part of the codebase all my prompts for this project"
- Created this prompt engineering documentation

### 8. Package Initialization
Eighth prompt: "I am missing the __init__.py code"
- Created src/__init__.py with package metadata and exports
- Created tests/__init__.py as a test package marker
- Properly structured the package for imports

### 9. Logs Directory Management
Ninth prompt: "Can you please write a gitignore file for inside the logs directory?"
- Created specialized .gitignore for logs directory
- Configured to track directory but ignore contents

## Key Decisions

1. **Tool Name**: Selected "sync-guardian" as it captures the protective and reliable nature of the tool
2. **License**: Chose MIT License for maximum flexibility and usability
3. **Project Structure**: Organized as a proper Python package with separate source and test directories
4. **Documentation**: Comprehensive README with clear installation and usage instructions
5. **Version Control**: Carefully configured .gitignore files to maintain proper structure while ignoring temporary files
6. **Package Management**: Proper Python package initialization with version tracking and exports

## Repository Description
Final tagline: "Reliable directory synchronization for Windows with task scheduling - a robust alternative to cloud sync"

## Final Project Structure
```
sync-guardian/
├── src/
│   ├── __init__.py        # Package initialization with version and exports
│   └── sync_guardian.py   # Core synchronization implementation
├── tests/
│   ├── __init__.py        # Test package marker
│   └── test_sync_guardian.py  # Comprehensive test suite
├── docs/
│   └── prompt_engineering.md  # This documentation
├── logs/
│   └── .gitignore         # Specialized ignore rules for logs
├── requirements.txt       # Project dependencies
├── README.md             # Main documentation
└── LICENSE               # MIT License
```

This documentation was created to provide transparency about the development process and serve as a reference for future development.
