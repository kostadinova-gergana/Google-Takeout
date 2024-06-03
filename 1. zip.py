import os
import zipfile

def unzip_and_delete(folder_path):
    # Iterate through all files in the specified folder
    for file_name in os.listdir(folder_path):
        # Check if the file is a zip file
        if file_name.endswith(".zip"):
            zip_file_path = os.path.join(folder_path, file_name)
            
            # Create a folder with the same name as the zip file (without the .zip extension)
            extract_folder_path = os.path.join(folder_path, file_name[:-4])
            os.makedirs(extract_folder_path, exist_ok=True)
            
            # Print which file is being unzipped
            print(f"Unzipping: {file_name}")
            
            # Unzip the file
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_folder_path)
            
            # Delete the original zip file
            os.remove(zip_file_path)
            print(f"Deleted: {file_name}")

# Example usage
folder_path = "E:/"
unzip_and_delete(folder_path)
