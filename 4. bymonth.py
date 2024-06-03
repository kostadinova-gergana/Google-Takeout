import os
import subprocess
import shutil

# List of specific folders to process (e.g., ["Photos from 2023", "Photos from 2022", etc.])
folders_to_process = ["2019"]

# Path to the directory containing all consolidated folders
base_dir = "E:/ConsolidatedPhotos/"

# Path to the ExifTool executable
exiftool_path = "C:/Users/geri0/Downloads/exiftool-12.85/exiftool.exe"

# Supported file extensions for media files
supported_extensions = ['.jpg', '.jpeg', '.png', '.heic', '.mp4', '.mov', '.avi']

def delete_json_files(folder_path):
    for item in os.listdir(folder_path):
        if item.endswith('.json'):
            json_path = os.path.join(folder_path, item)
            os.remove(json_path)
            print(f"Deleted JSON file: {json_path}")

def get_photo_taken_month(media_path):
    cmd = [exiftool_path, '-d', '%m', '-DateTimeOriginal', '-s3', media_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    month = result.stdout.strip()
    if result.returncode == 0 and month:
        return month
    else:
        return None

def organize_files_by_month(folder_path):
    for item in os.listdir(folder_path):
        if any(item.lower().endswith(ext) for ext in supported_extensions):
            media_path = os.path.join(folder_path, item)
            month = get_photo_taken_month(media_path)
            if month:
                month_folder = os.path.join(folder_path, month)
                if not os.path.exists(month_folder):
                    os.makedirs(month_folder)
                    print(f"Created folder: {month_folder}")
                shutil.move(media_path, os.path.join(month_folder, item))
                print(f"Moved {media_path} to {month_folder}")

def process_folder(folder_path):
    delete_json_files(folder_path)
    organize_files_by_month(folder_path)

def main():
    for folder_name in folders_to_process:
        folder_path = os.path.join(base_dir, folder_name)
        if os.path.exists(folder_path):
            print(f"Processing folder: {folder_path}")
            process_folder(folder_path)
        else:
            print(f"Folder does not exist: {folder_path}")

if __name__ == "__main__":
    main()
