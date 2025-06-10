import os
import zipfile

folder_path = r"C:\Users\Labre\OneDrive\Programmation\Python\web scraping\radiocanadarattrapage\Lib\site-packages"
zip_path = r"C:\Users\Labre\OneDrive\Programmation\Python\web scraping\radiocanadarattrapage"

def zip_directory(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Add file to zip with relative path
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

# Usage
zip_directory(folder_path, os.path.join(zip_path, 'radiocanadarattrapage.zip'))