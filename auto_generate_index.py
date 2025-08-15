import os
import pathlib
from datetime import date
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from colorama import Fore, Style, init


init(autoreset=True)


# ==== CONFIG ====
PROJECTS_DIR = os.getcwd()  # Use the current folder where the script runs
OUTPUT_FILE = os.path.join(PROJECTS_DIR, "PROJECTS_INDEX.md")


# Priority mapping for nice titles and emojis
PRIORITY_MAP = {
    "01": ("🔴 Priority 01 – Active Work (WIP)", Fore.RED),
    "02": ("🟠 Priority 02 – Secondary", Fore.YELLOW),
    "03": ("🟡 Priority 03 – On Hold / Backlog", Fore.LIGHTYELLOW_EX),
    "99": ("⚪ Priority 99 – Archived", Fore.WHITE),
}


# Order of priorities for output
PRIORITY_ORDER = ["01", "02", "03", "99"]


def parse_folder_name(name):
    parts = name.split("_")
    if len(parts) < 6:
        return None
    return {
        "priority": parts[0],
        "status": parts[1],
        "category": parts[2],
        "tech": parts[3],
        "description": parts[4],
        "date_or_version": "_".join(parts[5:]),
    }


def generate_index():
    projects = {}
    for folder in os.listdir(PROJECTS_DIR):
        folder_path = os.path.join(PROJECTS_DIR, folder)
        if os.path.isdir(folder_path) and folder != "__pycache__":
            parsed = parse_folder_name(folder)
            if parsed:
                prio = parsed["priority"]
                if prio not in projects:
                    projects[prio] = []
                projects[prio].append(parsed)

    lines = []
    lines.append(f"# 📂 Coding Projects Index\n")
    lines.append(f"_Last updated: {date.today()}_\n")
    lines.append("---\n")

    for prio in PRIORITY_ORDER:
        title, _ = PRIORITY_MAP.get(prio, (f"Priority {prio}", Fore.WHITE))
        lines.append(f"## {title}\n")
        lines.append(
            "| Project Name | Tech | Description | Start Date/Version | Status |"
        )
        lines.append(
            "|--------------|------|-------------|--------------------|--------|"
        )

        if prio in projects:
            for p in sorted(projects[prio], key=lambda x: x["description"]):
                project_name = f"{p['priority']}_{p['status']}_{p['category']}_{p['tech']}_{p['description']}_{p['date_or_version']}"
                folder_path = os.path.join(PROJECTS_DIR, project_name)
                folder_uri = pathlib.PurePath(folder_path).as_uri()
                folder_link = f"[{project_name}]({folder_uri})"
                lines.append(
                    f"| {folder_link} | {p['tech']} | {p['description']} | {p['date_or_version']} | {p['status']} |"
                )
        else:
            lines.append("| _(none)_ | | | | |")

        lines.append("\n")

    lines.append("---\n")
    lines.append("## 📌 Status Codes\n")
    lines.append("- **WIP** – Work in progress")
    lines.append("- **PLAN** – Planned, not started")
    lines.append("- **HOLD** – Paused for now")
    lines.append("- **DONE** – Completed")
    lines.append("- **ARCH** – Archived\n")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # Terminal output with colors
    print(f"{Fore.GREEN}✅ Project index updated: {OUTPUT_FILE}")
    for prio in PRIORITY_ORDER:
        if prio in projects:
            color = PRIORITY_MAP[prio][1]
            print(f"{color}{PRIORITY_MAP[prio][0]}: {len(projects[prio])} projects")


class ProjectWatcher(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            generate_index()


if __name__ == "__main__":
    generate_index()
    print(Fore.CYAN + f"👀 Watching for changes in: {PROJECTS_DIR}")
    event_handler = ProjectWatcher()
    observer = Observer()
    observer.schedule(event_handler, PROJECTS_DIR, recursive=False)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
