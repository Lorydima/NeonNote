"""
File operations module for NeonNote.
Handles saving and opening of text files.
"""
from tkinter import filedialog, messagebox, END, INSERT
import os

def save_file(window, text_widget):
    """
    Opens a file dialog to save the content of the text widget to a file.
    Updates the window title with the filename.
    """
    try:
        file_handle = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file_handle is None:
            return
        text = text_widget.get(1.0, END)
        file_handle.write(text)
        file_handle.close()
        try:
            window.title(f"NeonNote V1.2 - {os.path.basename(file_handle.name)}")
        except Exception:
            pass
        messagebox.showinfo("File Saved", "Your file has been saved successfully.")
    except Exception as e:
        messagebox.showerror("File Save Error", f"Failed to save file: {e}")

def open_file(window, text_widget):
    """
    Opens a file dialog to open a text file and load its content into the text widget.
    Updates the window title with the filename.
    """
    try:
        file_handle = filedialog.askopenfile(mode='r', defaultextension=".txt")
        if file_handle is not None:
            content = file_handle.read()
            text_widget.delete(1.0, END)
            text_widget.insert(INSERT, content)
            try:
                window.title(f"NeonNote V1.2 - {os.path.basename(file_handle.name)}")
            except Exception:
                pass
            messagebox.showinfo("File Opened", "Your file has been opened successfully.")
        else:
            return
    except Exception as e:
        messagebox.showerror("File Open Error", f"Failed to open file: {e}")