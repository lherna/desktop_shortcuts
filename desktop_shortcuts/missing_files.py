import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import pandas as pd 
import os
import sys

'''
For this program, we will need two folders for the comparison.
Ex: 'C:\\Users\\Luis\\OneDrive\\Documents\\Github'

'''

class Process():

    def __init__(self, root):
        self.root = root
        self.root.title("Local Folder Comparison")
        self.root.geometry("600x300")

        self.file_path = None
        self.df = None

        self.status = tk.StringVar(value = "No file loaded")

        tk.Button(
            root,
            text = "Open Folder",
            command = self.open_and_process_folder
        ).pack(pady = 10)

        tk.Label(
            root,
            textvariable = self.status,
            wraplength = 480
        ).pack(pady=10)

    def open_and_process_folder(self):
        self.folder_path = filedialog.askdirectory(title = "Select folder.")

        if not self.folder_path:
            return

        try:
            self.load_and_process_folder()
            self.status.set(
                f"Folder: {self.folder_path}\n"
                f"Files processed: {self.file_count}\n"
                #f"Total rows: {len(self.df)}"
            )
        except Exception as e:
            messagebox.showerror("Processing Error", str(e))


    def load_and_process_folder(self):
        self.file_count = 0

        extensions = {
            ".csv": 0,
            ".txt": 0,
            ".jpg": 0,
            ".mp3": 0,
            ".mp4": 0,
            ".pdf": 0,
            ".xml": 0,
            ".xlsx":0
        }

        for filename in os.listdir(self.folder_path):
            self.file_count +=1 
            ext = os.path.splitext(filename.lower())[1]
                
            if ext in extensions:
                extensions[ext] += 1

        #print report
        print("\n Folder Scan Report")
        print("-" * 30)
        print(f"Total Files: {self.file_count}")

        for ext, count in extensions.items():
            print(f"{ext.upper():<6}: {count}")

        print("-" * 30)

        return set(os.listdir())

    def compare(self, f1, f2):
        print('Starting comparison...')
        result = f1 - f2 
        print(f"The result is {result}")

# This block ensures the code runs only when the script is executed directly
# (e.g., python filename.py), not when it is imported as a module.
if __name__ == "__main__":
    
    print('Welcome to the program to compare files in two different locations.')
    root = tk.Tk()
    print('Running app...')
    print('Processing folder 1')
    folder1 = Process(root)
    print(folder1)
    print('Processing folder 2')
    folder2 = Process(root)
    print(folder2)
    #Compare the files and output result
    #res = Process.compare(folder1, folder2)

    # --- Run the Tkinter event loop ---
    root.mainloop()