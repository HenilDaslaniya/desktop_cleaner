# Desktop Cleanup Script

This Python script automatically organizes files on your desktop into categorized folders based on file type. It's a simple and effective tool to keep your desktop clutter-free and well-organized.

## Features

* Categorizes files into the following folders:

  * **Images** (`.jpg`, `.jpeg`, `.png`, `.gif`)
  * **Documents** (`.pdf`, `.doc`, `.docx`, `.txt`)
  * **Videos** (`.mp4`, `.mov`, `.avi`)
  * **Music** (`.mp3`, `.wav`, `.flac`)
  * **Executables** (`.exe`, `.dmg`, `.pkg`)
  * **Archives** (`.zip`, `.rar`, `.tar`, `.gz`)
  * **Others** for all other file types
* Automatically creates the necessary folders if they do not already exist
* Moves files to their respective folders based on file extension

## Requirements

* Python 3.x
* No external dependencies (uses built-in `os` and `shutil` modules)

## Usage

1. **Download** the `Cleanup.py` script.

2. **Run** the script:

   ```bash
   python Cleanup.py
   ```

3. The script will:

   * Scan your desktop directory
   * Sort all files into categorized folders

> ⚠️ This script is designed to operate on the current user's Desktop. Make sure you don't have unsaved work on your desktop before running it.

## Customization

To customize folder names or file type groupings, modify the `categories` dictionary in the script:

```python
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    ...
}
```

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Author

Created by \Henil Daslaniya
