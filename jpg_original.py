import os

# Path to the parent directory containing all the subfolders
parent_folder = "E:/ConsolidatedPhotos/"

def rename_files_in_subfolders(parent_folder):
    for root, dirs, files in os.walk(parent_folder):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            print(f"Processing folder: {folder_path}")
            rename_files(folder_path)

def rename_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('_original') or file.endswith('jpeg_original'):
                # Remove "_original" from the filename
                new_name = file.replace('_original', '').replace('jpeg_original', 'jpg')
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, new_name)
                
                # Check if the new file already exists
                if os.path.exists(new_path):
                    print(f"File already exists, skipping: {new_path}")
                    # Delete the original _original file
                    os.remove(old_path)
                else:
                    # Rename the file
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} to {new_path}")

def main():
    rename_files_in_subfolders(parent_folder)

if __name__ == "__main__":
    main()
