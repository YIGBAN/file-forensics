#Yanis Nagirnyak
# Import required modules
from pathlib import Path
import os

bruce_wayne_files = input("Enter the ABSOLUTE path to Bruce Wayne's Files: ")

folder_path = Path(bruce_wayne_files)

if folder_path.exists() and folder_path.is_dir():
    print("Files in Bruce Wayne's folder:")
    for file in folder_path.iterdir():
        if file.is_file():
            print(file.name)

    for file in folder_path.iterdir():
        if file.is_file():
            with open(file, 'r') as f:
                file_contents = f.read()
                if "Batman" in file_contents:
                    print(f"Found Batman in {file.name}!!")


