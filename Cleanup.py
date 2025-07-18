import os
import shutil

def clean_desktop(desktop_path):
    # Define categories and corresponding folder names
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".doc", ".docx", ".txt"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Music": [".mp3", ".wav", ".flac"],
        "Executables": [".exe", ".dmg", ".pkg"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Others": []  # Any file types not covered by other categories
    }

    # Create folders for each category if they don't already exist
    for category in categories.keys():
        folder_path = os.path.join(desktop_path, category)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    # Move files to corresponding folders based on their types
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for category, extensions in categories.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(desktop_path, category)
                    shutil.move(file_path, destination_folder)
                    moved = True
                    break
            if not moved:
                destination_folder = os.path.join(desktop_path, "Others")
                shutil.move(file_path, destination_folder)

def main():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    clean_desktop(desktop_path)
    print("Desktop cleanup completed.")

if __name__ == "__main__":
    main()
