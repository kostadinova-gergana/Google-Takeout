import os
import shutil

# Path to the directory containing all "takeout-20240602T123925Z-XXX" folders
base_dir = "E:/"

# Destination directory where all consolidated folders will be created
destination_dir = "E:/ConsolidatedPhotos/"

def merge_folders(source_folder, dest_folder):
    if not os.path.exists(dest_folder):
        print(f"Creating folder: {dest_folder}")
        shutil.copytree(source_folder, dest_folder)
    else:
        for item in os.listdir(source_folder):
            source_item = os.path.join(source_folder, item)
            dest_item = os.path.join(dest_folder, item)
            if os.path.isdir(source_item):
                merge_folders(source_item, dest_item)
            else:
                if not os.path.exists(dest_item):
                    print(f"Copying file: {source_item} to {dest_item}")
                    shutil.copy2(source_item, dest_item)
                else:
                    print(f"File already exists, skipping: {dest_item}")

def main():
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"Created destination directory: {destination_dir}")

    for i in range(1, 142):
        folder_name = f"takeout-20240602T123925Z-{str(i).zfill(3)}"
        google_photos_dir = os.path.join(base_dir, folder_name, "Takeout", "Google Снимки")
        
        if os.path.exists(google_photos_dir):
            print(f"Processing folder: {google_photos_dir}")
            for subfolder in os.listdir(google_photos_dir):
                source_subfolder = os.path.join(google_photos_dir, subfolder)
                dest_subfolder = os.path.join(destination_dir, subfolder)
                
                if os.path.isdir(source_subfolder):
                    print(f"Processing subfolder: {source_subfolder}")
                    merge_folders(source_subfolder, dest_subfolder)
        else:
            print(f"Folder not found: {google_photos_dir}")

if __name__ == "__main__":
    main()
