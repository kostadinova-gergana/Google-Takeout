import os
import json
import subprocess

# Path to the directory containing all consolidated folders (e.g., "Photos from 2023", "Photos from 2022", etc.)
base_dir = "E:/ConsolidatedPhotos/"

# Path to the ExifTool executable
exiftool_path = "C:/Users/geri0/Downloads/exiftool-12.85/exiftool.exe"

# Supported file extensions for media files
supported_extensions = ['.jpg', '.jpeg', '.png', '.heic', '.mp4', '.mov', '.avi']

def apply_metadata(media_path, metadata):
    # Set the tags
    tags = {
        'EXIF:ImageDescription': metadata['description'],
        'EXIF:DateTimeOriginal': metadata['photoTakenTime']['formatted'],
        'EXIF:GPSLatitude': metadata['geoData']['latitude'],
        'EXIF:GPSLongitude': metadata['geoData']['longitude'],
        'EXIF:GPSAltitude': metadata['geoData']['altitude']
    }
    
    # Construct the ExifTool command
    cmd = [exiftool_path]
    for k, v in tags.items():
        cmd.append(f"-{k}={v}")
    cmd.append(media_path)
    
    # Apply the tags to the media file
    print(f"Applying metadata to {media_path}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Check for errors
    if result.returncode != 0:
        print(f"Error applying metadata to {media_path}: {result.stderr}")

def process_folder(folder_path):
    for item in os.listdir(folder_path):
        if item.endswith('.json'):
            json_path = os.path.join(folder_path, item)
            with open(json_path, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
                
            media_title = metadata['title']
            media_path = os.path.join(folder_path, media_title)
            
            if os.path.exists(media_path) and any(media_path.lower().endswith(ext) for ext in supported_extensions):
                apply_metadata(media_path, metadata)
            else:
                print(f"Media file not found or unsupported format for {json_path}")

def main():
    for root, dirs, files in os.walk(base_dir):
        for name in dirs:
            folder_path = os.path.join(root, name)
            print(f"Processing folder: {folder_path}")
            process_folder(folder_path)

if __name__ == "__main__":
    main()
