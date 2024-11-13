import os
from pathlib import Path
import logging
import sys

# Set up logging with a custom format
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# Taking Project Name from CLI
if len(sys.argv) > 1:
    project_name = sys.argv[1]
    print("Project Name is set to:", project_name)
else:
    print("No Name provided.")


list_of_files = [
    ".github/workflows/.gitkeep",  #placeholder file,
    f"src/{project_name}/__init__.py", #constructor file for using project as a local package,
    f"src/{project_name}/components/___init__.py", #components folder,
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init.py__",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", #model configurations,
    "dvc.yaml",
    'params.yaml',
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
                         

