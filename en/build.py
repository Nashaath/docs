# build.py
import subprocess
import sys
import os

def run_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        print(result.stderr)
        sys.exit(1)
    print(result.stdout)

def main():
    # Ensure Python is running in the correct environment with necessary packages installed
    run_command("mdspell -V")

    # Run mdspell checks
    run_command("mdspell -n -a --en-us docs/**/*.md -d dictionary/en_US-large")
    run_command("mdspell -n -a --en-us docs/**/**/*.md -d dictionary/en_US-large")
    run_command("mdspell -n -a --en-us mkdocs.yml -d dictionary/en_US-large")
    run_command("mdspell -n -a --en-us theme/material/templates/home-page2.html -d dictionary/en_US-large")

    # Run markdown link checks
    run_command("find docs/** -type f -name '*.md' | xargs -L1 markdown-link-check -c ./markdown-link-check-config.json --quiet")
    run_command("find docs/**/* -type f -name '*.md' | xargs -L1 markdown-link-check -c ./markdown-link-check-config.json --quiet")

    # Build MkDocs site
    run_command("mkdocs build -c")

    # List contents of the site directory
    run_command("ls site/")

if __name__ == "__main__":
    main()
