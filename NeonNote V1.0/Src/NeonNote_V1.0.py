# NeonNote V.1.0 Source Code Date: 00/00/0000 Dev: LDM Dev.

'''
NeonNote is a simple note-taking application with a user-friendly interface.
'''

# Library for app Dev.
from tkinter import filedialog, messagebox
from tkinter import *
import webbrowser
import time
import pyperclip
import json
import os

# Icon Path
ICON_PATH = os.path.join(os.path.dirname(__file__), "NeonNote_Icon.ico")
LOGO_PATH = os.path.join(os.path.dirname(__file__), "NeonNote_Logo.png")

try:
    lic_win.iconbitmap(ICON_PATH)
except Exception:
    pass

try:
    Logo_IMG = PhotoImage(file=LOGO_PATH)
except Exception:
    pass

# Save Function
def save_file():
    global Entry, window
    open_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt",)
    if open_file is None:
        messagebox.showerror("File Save Error", "Failed to save file.")
        return
    Text = str(Entry.get(1.0, END))
    open_file.write(Text)
    open_file.close()
    window.title(f"NeonNote V1.0 - {open_file.name.split('/')[-1]}")
    messagebox.showinfo("File Saved Successful", "Your file has been saved successfully.")

# Open Function
def open_file():
    global Entry, window
    open_file = filedialog.askopenfile(mode='r', defaultextension=".txt",)
    if open_file is not None:
        content = open_file.read()
        Entry.delete(1.0, END)  
        Entry.insert(INSERT, content)
        messagebox.showinfo("File Open Successful", "Your file has been opened successfully.")
        window.title(f"NeonNote V1.0 - {open_file.name.split('/')[-1]}")
    else:
        messagebox.showerror("File Open Error", "Failed to open file.")

# License Window Function
def license_window():
    lic_win = Toplevel()
    lic_win.title("License Agreement")
    lic_win.geometry("700x500")
    lic_win.configure(bg="#c6c6c6")
    lic_win.resizable(False, False)
    try:
        lic_win.iconbitmap(ICON_PATH)
    except Exception:
        pass

    label = Label(lic_win, text="NeonNote License Agreement", bg="#c6c6c6", font=("Arial", 16, "bold"))
    label.pack(pady=20)

    license_text = """Thank you for downloading NeonNote V1.0 Before using the software, please take a moment to review license outlined below. Your compliance with these license ensures the responsible and appropriate use of this application.

LICENSE:

- By software we mean the entire program folder that was downloaded. So the EXE file, 
  the DATA.json file and the .ICO Logo file.

- You can freely download and use this application.

- You can view the source code on Git Hub for educational or personal purposes.

- It is not permitted to republish either the application or the source code, in any form or for 
  any purpose, without explicit written permission from me.

- The software is provided 'as is', without any warranties of any kind.

LICENSE update date: 02/04/2025

Thank You again from LDM Dev.❤️
"""
    text_box = Text(lic_win, bg="#f0f0f0", fg="#000000", font=("Arial", 11), wrap=WORD, height=10, relief="solid", bd=1)
    text_box.insert(1.0, license_text)
    text_box.config(state=DISABLED)
    text_box.pack(padx=20, pady=10, fill=BOTH, expand=True)
    lic_win.mainloop()

# Info Function
def info_function():
    info_window = Toplevel()
    info_window.title("Info")
    info_window.geometry("300x350")
    info_window.configure(bg="#c6c6c6")
    info_window.resizable(False, False)
    try:
        info_window.iconbitmap(ICON_PATH)
    except Exception:
        pass

    info_label = Label(info_window, text="NeonNote Version 1.0\nDev: LDM Dev.", bg="#c6c6c6", font=("Arial", 18))
    info_label.pack(pady=20)

    # GitHub Button
    git_hub_repository_button = Button(
        info_window, text="NeonNote GitHub Repository",
        command=lambda: webbrowser.open("https://github.com/Lorydima/NeonNote"),
        bg="#2f72bb", fg="white",
        font=("Arial", 12, "bold"),
        width=22, height=2,
        relief="solid", bd=1,
        highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a",
        cursor="hand2"
    )
    def gh_on_enter(e): git_hub_repository_button['bg'] = "#17508a"
    def gh_on_leave(e): git_hub_repository_button['bg'] = "#2f72bb"
    git_hub_repository_button.bind("<Enter>", gh_on_enter)
    git_hub_repository_button.bind("<Leave>", gh_on_leave)
    git_hub_repository_button.pack(pady=10)

    # Website Button
    website_button = Button(
        info_window, text="NeonNote Website",
        command=lambda: webbrowser.open("https://lorydima.github.io/NeonNote/"),
        bg="#2f72bb", fg="white",
        font=("Arial", 12, "bold"),
        width=22, height=2,
        relief="solid", bd=1,
        highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a",
        cursor="hand2"
    )
    def ws_on_enter(e): website_button['bg'] = "#17508a"
    def ws_on_leave(e): website_button['bg'] = "#2f72bb"
    website_button.bind("<Enter>", ws_on_enter)
    website_button.bind("<Leave>", ws_on_leave)
    website_button.pack(pady=10)

    # License Button
    license_button = Button(
        info_window, text="NeonNote License",
        command=license_window,
        bg="#2f72bb", fg="white",
        font=("Arial", 12, "bold"),
        width=22, height=2,
        relief="solid", bd=1,
        highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a",
        cursor="hand2"
    )
    def lc_on_enter(e): license_button['bg'] = "#17508a"
    def lc_on_leave(e): license_button['bg'] = "#2f72bb"
    license_button.bind("<Enter>", lc_on_enter)
    license_button.bind("<Leave>", lc_on_leave)
    license_button.pack(pady=10)

# More Functions Window Function
def more_functions_window():
    global Entry
    mf_win = Toplevel()
    mf_win.title("More Functions")
    mf_win.geometry("700x300")  # aumentata larghezza per spazio shortcut
    mf_win.configure(bg="#c6c6c6")
    mf_win.resizable(False, False)
    try:
        mf_win.iconbitmap(ICON_PATH)
    except Exception:
        pass

    title_label = Label(mf_win, text="More Functions", bg="#c6c6c6", font=("Arial", 18, "bold"))
    title_label.pack(pady=20, padx=150, anchor="w")

    shortcut_title = Label(mf_win, text="Shortcuts Available", bg="#c6c6c6", fg="#000000", font=("Arial", 15, "bold"))
    shortcut_title.place(x=470, y=65)

    # Functions
    def Write_time():
        Entry.insert(INSERT, time.strftime("%H:%M:%S") + "\n")
    def Write_date():
        Entry.insert(INSERT, time.strftime("%d/%m/%Y") + "\n")
    def set_arial():
        Entry.config(font=("Arial", 12))
    def set_calibri():
        Entry.config(font=("Calibri", 12))
    def set_sans():
        Entry.config(font=("Segoe UI", 12))
    def copy_all():
        pyperclip.copy(Entry.get(1.0, END))
        messagebox.showinfo("Copy Successful", "All text has been copied to clipboard.")
    def delete_all():
        Entry.delete(1.0, END)
        messagebox.showinfo("Delete Successful", "All text has been deleted.")
    def count_chars_words():
        text = Entry.get(1.0, END)
        chars = len(text) - 1  
        words = len(text.split())
        messagebox.showinfo("Count", f"Characters: {chars}\nWords: {words}")

    center_frame = Frame(mf_win, bg="#c6c6c6")
    center_frame.place(x=0, y=60)

    left_frame = Frame(center_frame, bg="#c6c6c6")
    left_frame.grid(row=0, column=0, padx=20)
    Button(left_frame, text="Write actual time", width=18, font=("Arial", 12, "bold"), bg="#2f72bb", fg="white", relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2", command=Write_time).pack(pady=5)
    Button(left_frame, text="Write actual date", width=18, font=("Arial", 12, "bold"), bg="#2f72bb", fg="white", relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2", command=Write_date).pack(pady=5)
    Button(left_frame, text="Count chars/words", width=18, font=("Arial", 12, "bold"), bg="#2f72bb", fg="white", relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2", command=count_chars_words).pack(pady=5)

    right_frame = Frame(center_frame, bg="#c6c6c6")
    right_frame.grid(row=0, column=1, padx=20)
    Button(right_frame, text="Change font in Arial", width=18, font=("Arial", 12, "bold"), bg="#2f72bb", fg="white", relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2", command=set_arial).pack(pady=5)
    Button(right_frame, text="Change font in Calibri", width=18, font=("Arial", 12, "bold"), bg="#2f72bb", fg="white", relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2", command=set_calibri).pack(pady=5)
    Button(right_frame, text="Change font in Segoe UI", width=18, font=("Arial", 12, "bold"), bg="#2f72bb", fg="white", relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2", command=set_sans).pack(pady=5)

    # Shortcuts info label a destra
    shortcuts_text = (
        "Ctrl+S  →  Save file\n"
        "Ctrl+O  →  Open file\n"
        "Ctrl+I  →  Info\n"
        "Ctrl+M  →  More Functions\n"
        "ESC     →  Exit"
    )
    shortcuts_label = Label(mf_win, text=shortcuts_text, bg="#c6c6c6", fg="#17508a", font=("Arial", 13, "bold"), justify=LEFT)
    shortcuts_label.place(x=470, y=100)

    bottom_frame = Frame(mf_win, bg="#c6c6c6")
    bottom_frame.place(y=225)
    Button(bottom_frame, text="Copy all Text", width=18, font=("Arial", 12, "bold"), bg="#2f72bb", fg="white", relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2", command=copy_all).grid(row=0, column=0, padx=20)
    Button(bottom_frame, text="Delete all Text", width=18, font=("Arial", 12, "bold"), bg="#2f72bb", fg="white", relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2", command=delete_all).grid(row=0, column=1, padx=20)

# Check License Functions
LICENSE_FILE = os.path.join(os.path.dirname(__file__), "license_status.json")

def check_license():
    if os.path.exists(LICENSE_FILE):
        with open(LICENSE_FILE, "r") as f:
            data = json.load(f)
            if data.get("license_accepted", False):
                return True
    return False

def save_license_status(accepted):
    with open(LICENSE_FILE, "w") as f:
        json.dump({"license_accepted": accepted}, f)

def show_license_window():
    lic_win = Tk()
    lic_win.title("License Agreement")
    lic_win.geometry("700x500")
    lic_win.configure(bg="#c6c6c6")
    lic_win.resizable(False, False)
    try:
        lic_win.iconbitmap(ICON_PATH)
    except Exception:
        pass

    label = Label(lic_win, text="NeonNote License Agreement", bg="#c6c6c6", font=("Arial", 16, "bold"))
    label.pack(pady=20)

    license_text = """Thank you for downloading NeonNote V1.0 Before using the software, please take a moment to review license outlined below. Your compliance with these license ensures the responsible and appropriate use of this application.

LICENSE:

- By software we mean the entire program folder that was downloaded. So the EXE file, 
  the DATA.json file and the .ICO Logo file.

- You can freely download and use this application.

- You can view the source code on Git Hub for educational or personal purposes.

- It is not permitted to republish either the application or the source code, in any form or for 
  any purpose, without explicit written permission from me.

- The software is provided 'as is', without any warranties of any kind.

LICENSE update date: 02/04/2025

Thank You again from LDM Dev.❤️
"""
    text_box = Text(lic_win, bg="#f0f0f0", fg="#000000", font=("Arial", 11), wrap=WORD, height=10, relief="solid", bd=1)
    text_box.insert(1.0, license_text)
    text_box.config(state=DISABLED)
    text_box.pack(padx=20, pady=10, fill=BOTH, expand=True)

    def accept():
        save_license_status(True)
        lic_win.destroy()
        gui_function()

    def on_close():
        save_license_status(False)
        lic_win.destroy()
        exit()  

    accept_button = Button(
        lic_win, text="Accept", command=accept, bg="#27ae60", fg="white",
        font=("Arial", 12, "bold"), width=18, height=2, relief="solid", bd=1,
        highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2"
    )
    accept_button.pack(pady=20)

    lic_win.protocol("WM_DELETE_WINDOW", on_close)
    lic_win.mainloop()

# GUI Function
def gui_function():
    global Entry, window
    window = Tk()
    window.title("NeonNote V1.0")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height }")
    window.state('zoomed')
    window.configure(bg="#c6c6c6")
    try:
        window.iconbitmap(ICON_PATH)
    except Exception:
        pass

    # Logo IMG
    try:
        Logo_IMG = PhotoImage(file=LOGO_PATH)
        Logo_IMG = Logo_IMG.subsample(6)
        logo_label = Label(window, image=Logo_IMG, bg="#c6c6c6")
        logo_label.image = Logo_IMG  
        logo_label.place(x=100, y=24)
    except Exception:
        pass

    button_width = 18
    button_height = 2

    # More Functions Button
    more_functions_button = Button(
        window, text="More Functions", command=more_functions_window, bg="#2f72bb", fg="white",
        font=("Arial", 12, "bold"), width=button_width, height=button_height,
        relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2"
    )
    def mf_on_enter(e): more_functions_button['bg'] = "#17508a"
    def mf_on_leave(e): more_functions_button['bg'] = "#2f72bb"
    more_functions_button.bind("<Enter>", mf_on_enter)
    more_functions_button.bind("<Leave>", mf_on_leave)
    more_functions_button.place(x=695, y=50)

    # Save Button
    save_button = Button(
        window, text="Save file", command=save_file, bg="#2f72bb", fg="white",
        font=("Arial", 12, "bold"), width=button_width, height=button_height,
        relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2"
    )
    def save_on_enter(e): save_button['bg'] = "#17508a"
    def save_on_leave(e): save_button['bg'] = "#2f72bb"
    save_button.bind("<Enter>", save_on_enter)
    save_button.bind("<Leave>", save_on_leave)
    save_button.place(x=895, y=50)

    # Open Button
    open_button = Button(
        window, text="Open file", command=open_file, bg="#2f72bb", fg="white",
        font=("Arial", 12, "bold"), width=button_width, height=button_height,
        relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2"
    )
    def open_on_enter(e): open_button['bg'] = "#17508a"
    def open_on_leave(e): open_button['bg'] = "#2f72bb"
    open_button.bind("<Enter>", open_on_enter)
    open_button.bind("<Leave>", open_on_leave)
    open_button.place(x=1095, y=50)

    # Info Button
    info_button = Button(
        window, text="Info", command=info_function, bg="#2f72bb", fg="white",
        font=("Arial", 12, "bold"), width=button_width, height=button_height,
        relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2"
    )
    def info_on_enter(e): info_button['bg'] = "#17508a"
    def info_on_leave(e): info_button['bg'] = "#2f72bb"
    info_button.bind("<Enter>", info_on_enter)
    info_button.bind("<Leave>", info_on_leave)
    info_button.place(x=1295, y=50)

    # Text Area
    Entry = Text(window, bg="#ffffff", fg="#000000", font=("Arial", 12), relief="solid", highlightthickness=5, highlightbackground="#2f72bb", highlightcolor="#2f72bb", wrap=WORD)
    Entry.place(y=150, width=screen_width, height=screen_height-220)

    # Shortcuts
    window.bind('<Control-s>', lambda e: save_file())
    window.bind('<Control-o>', lambda e: open_file())
    window.bind('<Control-i>', lambda e: info_function())
    window.bind('<Control-m>', lambda e: more_functions_window())
    window.bind('<Escape>', lambda e: window.destroy())

    window.mainloop()

# Call Main Function
if __name__ == "__main__":
    if check_license():
        gui_function()
    else:
        show_license_window()