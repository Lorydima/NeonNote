"""
Info window module for NeonNote.
Displays application information and license details.
"""
from tkinter import Toplevel, Label, Button, Text, DISABLED, WORD, BOTH
import webbrowser
import os
from config import ICON_PATH, LICENSE_PATH

def read_license_window():
    """
    Creates and displays a window containing the text of the LICENSE.txt file.
    """
    lic_win = Toplevel()
    lic_win.title("License")
    lic_win.geometry("700x500")
    lic_win.configure(bg="#c6c6c6")
    lic_win.resizable(False, False)
    try:
        lic_win.iconbitmap(ICON_PATH)
    except Exception:
        pass

    license_text = "LICENSE.txt not found."
    if os.path.exists(LICENSE_PATH):
        try:
            with open(LICENSE_PATH, "r", encoding="utf-8") as f:
                license_text = f.read()
        except Exception as e:
            license_text = f"Error reading license file: {e}"

    header = Label(lic_win, text="NeonNote License", bg="#c6c6c6", font=("Arial", 16, "bold"))
    header.pack(pady=10)

    text_box = Text(lic_win, bg="#f0f0f0", fg="#000000", font=("Arial", 11), wrap=WORD, height=20, relief="solid", bd=1)
    text_box.insert(1.0, license_text)
    text_box.config(state=DISABLED)
    text_box.pack(padx=20, pady=10, fill=BOTH, expand=True)

def info_function():
    """
    Creates and displays the information window with links to GitHub and the website.
    """
    info_window = Toplevel()
    info_window.title("Info")
    info_window.geometry("300x350")
    info_window.configure(bg="#c6c6c6")
    info_window.resizable(False, False)
    try:
        info_window.iconbitmap(ICON_PATH)
    except Exception:
        pass

    info_label = Label(info_window, text="NeonNote Version 1.2\nDev: LDM Dev.", bg="#c6c6c6", font=("Arial", 18))
    info_label.pack(pady=20)

    def create_styled_button(text, command):
        btn = Button(
            info_window, text=text,
            command=command,
            bg="#2f72bb", fg="white",
            font=("Arial", 12, "bold"),
            width=22, height=2,
            relief="solid", bd=1,
            highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a",
            cursor="hand2"
        )
        def on_enter(e): btn['bg'] = "#17508a"
        def on_leave(e): btn['bg'] = "#2f72bb"
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.pack(pady=10)
        return btn

    # GitHub Button
    create_styled_button(
        "NeonNote GitHub Repository",
        lambda: webbrowser.open("https://github.com/Lorydima/NeonNote")
    )

    # Website Button
    create_styled_button(
        "NeonNote Website",
        lambda: webbrowser.open("https://lorydima.github.io/NeonNote/")
    )

    # License Button
    create_styled_button("Read License", read_license_window)