import os
from pathlib import Path
import logging

# Use logging.INFO (an integer) instead of logging.info (a function)
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [
    "src/__init__.py",      # Usually, this should be __init__.py
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    # os.path.split expects a string, so convert Path to str
    fileidir, filename = os.path.split(str(filepath))
    
    if fileidir != "":
        # Corrected "os.makeirs" to "os.makedirs"
        os.makedirs(fileidir, exist_ok=True)
        logging.info(f"Creating directory: {fileidir} for the file {filename}")
    
    # Check if the file doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")
       