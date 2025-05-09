#ovjoy33
import os
import shutil
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import askdirectory
import tkfilebrowser
from tkinter import *


class FileTransferApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Transfer")
        self.root.geometry("800x600") 
        self.source_folders = []  # List to store multiple source folders
        
        self.create_widgets()
        
    def create_widgets(self):
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Source folders list with scrollbar
        ttk.Label(self.frame, text="Source Folders:").pack(pady=5)
        
        # Create frame for listbox and scrollbar
        list_frame = ttk.Frame(self.frame)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox for showing selected folders
        self.folders_listbox = tk.Listbox(
            list_frame, 
            width=70, 
            height=10,
            yscrollcommand=scrollbar.set
        )
        self.folders_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.folders_listbox.yview)
        
        # Buttons for source folder management
        btn_frame = ttk.Frame(self.frame)
        btn_frame.pack(pady=5)
        
        ttk.Button(
            btn_frame, 
            text="Select target folders", 
            command=self.add_source
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            btn_frame, 
            text="Remove Selected", 
            command=self.remove_source
        ).pack(side=tk.LEFT, padx=5)
        
        # Destination folder
        dest_frame = ttk.Frame(self.frame)
        dest_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(dest_frame, text="Destination Folder:").pack()
        self.dest_entry = ttk.Entry(dest_frame, width=70)
        self.dest_entry.pack(pady=5)
        ttk.Button(
            dest_frame, 
            text="Browse", 
            command=self.select_destination
        ).pack()
        
        # Transfer button
        ttk.Button(
            self.frame, 
            text="Transfer All Files", 
            command=self.transfer_files,
            style='Accent.TButton'
        ).pack(pady=20)
        
        # Create custom style for main transfer button
        style = ttk.Style()
        style.configure('Accent.TButton', font=('Helvetica', 10, 'bold'))
        
    def add_source(self):
        folder = tkfilebrowser.askopendirnames(title="Select folder to move files from")
        if folder:
            if folder not in self.source_folders:
                self.source_folders.append(folder)
                self.folders_listbox.insert(tk.END, folder)
            else:
                messagebox.showwarning("Warning", "This folder has already been added!")
                
    def remove_source(self):
        try:
            selection = self.folders_listbox.curselection()
            if selection:
                folder = self.folders_listbox.get(selection)
                self.folders_listbox.delete(selection)
                self.source_folders.remove(folder)
        except:
            pass
            
    def select_destination(self):
        folder = askdirectory(title="Select destination folder")
        if folder:
            self.dest_entry.delete(0, tk.END)
            self.dest_entry.insert(0, folder)
            
    def transfer_files(self):
        if not self.source_folders:
            messagebox.showerror("Error", "Please add at least one source folder!")
            return
            
        parent_folder = self.dest_entry.get()
        if not parent_folder:
            messagebox.showerror("Error", "Please select a destination folder!")
            return
            
        try:
            total_files = 0
            # Process each source folder
            for child_folder in self.source_folders:
                # Move all files from source to destination
                for filename in os.listdir(child_folder):
                    file_path = os.path.join(child_folder, filename)
                    if os.path.isfile(file_path):
                        shutil.move(file_path, parent_folder)
                        total_files += 1
                
                # Delete the source folder
                shutil.rmtree(child_folder)
            
            # Clear everything after successful transfer
            self.folders_listbox.delete(0, tk.END)
            self.source_folders.clear()
            self.dest_entry.delete(0, tk.END)
            
            messagebox.showinfo(
                "Success", 
                f"Successfully moved {total_files} files from {len(self.source_folders)} folders!\n"
                "All source folders have been deleted."
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileTransferApp(root)
    root.mainloop()
    
    #make a button to verify are you ssure you wanna proceed with this operation
    # make an option to choose mutiple files at once to delete and move files from child folders
    #this code is for moving files from multiple folders to a single destination folder and deleting the source folders after the transfer.