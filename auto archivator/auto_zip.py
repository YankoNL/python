import os
import zipfile

zip_filename = 'main_app.zip'
files_to_ignore = ['auto_zip.py', 'test_ignore_this.txt']
folders_to_ignore = ['.idea', 'venv']

current_directory = os.getcwd()

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for folder_names, sub_folders, file_names in os.walk(current_directory):
        for file_name in file_names:
            if file_name in files_to_ignore or file_name == zip_filename:
                continue
            file_path = os.path.join(folder_names, file_name)
            archive_path = os.path.relpath(file_path, current_directory)

            if any([x in archive_path for x in folders_to_ignore]):
                continue

            zipf.write(file_path, archive_path)

print(f'Folder "{current_directory}" and its contents are archived to {zip_filename}')
print(f'Directories ({", ".join(folders_to_ignore)}) marked as ignored')
print(f'Files ({", ".join(files_to_ignore)}) marked as ignored')

