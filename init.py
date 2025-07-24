import os
from pathlib import Path

project_name = "AI_Project"

list_of_files = [
    ".gitignore",
    "README.md",
    "requirements.txt",
    ".env",
    "app.py",

    f"src/{project_name}/__init__.py",
    f"src/{project_name}app.py",
   


    
    "init_setup.sh",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass
    else:
        print(f"Skipping existing file: {filepath}")