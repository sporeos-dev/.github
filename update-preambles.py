#!/usr/bin/env python3
import os
import sys

# --- CONFIGURATION ---
# The list of sibling directories (neighbors)
REPOS = [
    ".github",
    "spore-os",
    "spore-os-protocol",
    "spore-core-nodes",
    "spore-client-libs",
    "spore-install",
    "spore-dialog",
    "e2e-testing"
]

PREAMBLE_FILE = "repo-preamble.md"
MARKER_START = "<!-- PREAMBLE BEGIN -->"
MARKER_END = "<!-- PREAMBLE FIN -->"

def get_script_dir():
    """Returns the absolute path of the directory containing this script."""
    return os.path.dirname(os.path.abspath(__file__))

def update_readme(repo_path, readme_path, preamble_content):
    """Injects preamble into readme between markers."""
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_idx = content.find(MARKER_START)
    end_idx = content.find(MARKER_END)

    if start_idx == -1 or end_idx == -1:
        print(f"   ⚠️  Skipped: Markers not found in {repo_path}")
        return False

    # Construct new content
    new_content = (
        content[:start_idx + len(MARKER_START)] + 
        "\n" + preamble_content + "\n" + 
        content[end_idx:]
    )

    if content == new_content:
        print(f"   ✅ {repo_path}: Up to date.")
        return False

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"   ✏️  {repo_path}: Updated.")
    return True

def main():
    script_dir = get_script_dir()
    
    # Check preamble exists relative to script
    preamble_path = os.path.join(script_dir, PREAMBLE_FILE)
    if not os.path.exists(preamble_path):
        print(f"❌ Error: '{PREAMBLE_FILE}' not found in {script_dir}")
        sys.exit(1)

    with open(preamble_path, "r", encoding="utf-8") as f:
        preamble_content = f.read().strip()

    print(f"🚀 Updating sibling repos from: {script_dir}\n")

    for repo in REPOS:
        # Construct path to sibling: ../repo_name/README.md
        readme_path = os.path.join(script_dir, "..", repo, "README.md")
        
        # Normalize path (resolves the ..)
        readme_path = os.path.normpath(readme_path)

        if not os.path.exists(readme_path):
            print(f"   ⚠️  Skipped: {repo} not found at {readme_path}")
            continue

        update_readme(repo, readme_path, preamble_content)

    print("\n🎉 Done!")

if __name__ == "__main__":
    main()   