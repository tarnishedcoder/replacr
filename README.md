# 🗂️ File Transfer App

A simple, user-friendly Python application built with Tkinter for transferring files from multiple source folders into a single destination folder. After transferring, it deletes the original source folders.

## ✨ Features

- ✅ Select multiple source folders using a graphical interface.
- ✅ Display selected folders in a scrollable list.
- ✅ Choose a single destination folder to move all files into.
- ✅ Automatically moves files and deletes empty source folders.
- ✅ Allows removal of individual folders from the source list.
- ✅ Warning prompts and error handling for safe usage.
- ✅ GUI built using `tkinter` and `ttk` for a polished feel.
- 🛡️ Future Improvements:
  - Confirmation dialog before executing file transfer and deletion.
  - Option to delete or move selected files within subfolders.

## 📦 Requirements

- Python 3.x
- `tkfilebrowser`

Install dependencies with:

```bash
pip install tkfilebrowser
🚀 How to Run
Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/file-transfer-app.git
cd file-transfer-app
Run the application:

bash
Copy
Edit
python file_transfer_app.py
✅ Note: Only files (not folders) will be moved from the selected source directories.

📷 Screenshots
Coming soon

🛠️ How it Works
Select multiple source folders from which you want to move files.

Select a single destination folder.

Click Transfer All Files.

The app will:

Move all files from the source folders to the destination.

Delete each original source folder.

Show a message confirming how many files were transferred.

⚠️ Warning
This app deletes all selected source folders after the transfer is completed.

Always double-check your selections before starting.

It's strongly recommended to back up important files beforehand.

📌 Notes
Only regular files are moved. Subdirectories inside source folders are ignored.

Recursive transfer from nested folders is not yet supported.
