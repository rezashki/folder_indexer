# Coding Projects Indexer

This project provides a Python script to automatically generate and update an organized Markdown index of your coding projects in a specified folder.

---

## Features

- Scans folders with specific naming conventions to categorize projects
- Generates a clear Markdown index file (`PROJECTS_INDEX.md`) listing projects by priority
- Creates clickable links in the Markdown file to open project folders (works best with Obsidian and compatible Markdown viewers)
- Automatically updates the index when project folders change, using a watcher
- Color-coded terminal output showing summary by priority

---

## Folder Naming Convention Guide

Each project folder should follow this format:

`[PRIORITY]_[STATUS]_[CATEGORY]_[TECH]_[DESCRIPTION]_[DATE_OR_VERSION]`

### Example

01_WIP_Web_Python_Chatbot_2025-08-15
02_PLAN_Data_R_Pipeline_Research_2025Q3
03_HOLD_Mobile_Flutter_UserApp_2024v2
99_ARCH_Utility_Bash_BackupScript_2021-12


### Breakdown of Naming Parts

| Part             | Description                                      | Example        |
|------------------|------------------------------------------------|----------------|
| PRIORITY         | Project urgency: 01, 02, 03, or 99             | 01             |
| STATUS           | Project status: WIP, PLAN, HOLD, DONE, ARCH    | WIP            |
| CATEGORY         | Project type/category                           | Web, Data      |
| TECH             | Main technology used                            | Python, R      |
| DESCRIPTION      | Short, clear description                        | Chatbot        |
| DATE_OR_VERSION  | Start date or version info (YYYY-MM-DD, etc.) | 2025-08-15     |

### Priority Codes

- **01** – 🔴 Active Work (WIP)
- **02** – 🟠 Secondary
- **03** – 🟡 On Hold / Backlog
- **99** – ⚪ Archived

### Status Codes

- **WIP** – Work in progress
- **PLAN** – Planned, not started
- **HOLD** – Paused
- **DONE** – Completed
- **ARCH** – Archived

### Tips

- Use an underscore `_` as the separator – no spaces between or within parts.
- Keep the folder names concise but descriptive.
- If your description or category includes multiple words, join them withCamelCase or remove spaces.
- Use a consistent date or version format so you can sort and search easily.
- Avoid special characters except underscores and dashes.

---

## Installation

1. Ensure Python 3.7+ is installed.
2. Install dependencies:
`pip install watchdog colorama`

3. Place the script in the directory you want to index or modify the `PROJECTS_DIR` variable inside the script.

---

## Usage

Run the script:
`python projects_indexer.py`

- It generates `PROJECTS_INDEX.md`.
- The script watches the folder for changes and updates automatically.
- Stop the script with `Ctrl+C`.

---

## How It Works

- The script parses folder names according to the naming convention.
- Groups projects by priority.
- Generates a Markdown file with project details and clickable folder links.
- Uses file system watcher to auto-refresh on folder changes.

---

## Troubleshooting

- Ensure folder names follow the exact naming pattern.
- If links do not open folders, confirm your Markdown viewer supports `file://` URIs.
- Running inside Obsidian? Some versions may require absolute file paths.

---

## Contributing

Feel free to open issues or submit pull requests for improvements.

---

## License

This project is open-source under the MIT License.

---

Made with ❤️ for organized coding.


