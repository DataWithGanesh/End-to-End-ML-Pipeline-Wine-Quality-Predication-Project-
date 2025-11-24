# Project Folder Structure Template Generator 

import os
from pathlib import Path
import logging


# Logging String Format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "mlProject"



list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", # Configuration file
    "params.yaml", # Parameters file
    "schema.yaml", # Schema file
    "main.py", # Main entry point of the project
    "app.py", # Application file
    "setup.py", # Setup file for packaging
    "research/trials.ipynb", # Jupyter notebook for research
    "templates/index.html", # HTML template file


]



for filepath in list_of_files:
    filepath = Path(filepath) # Convert to Path object
    filedir, filename = os.path.split(filepath) # Split into directory and file name


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")