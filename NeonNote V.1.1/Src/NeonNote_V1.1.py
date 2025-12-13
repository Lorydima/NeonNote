# NeonNote V.1.1 Source Code Date: 13/12/2025 Dev: LDM Dev.

'''
NeonNote is a simple note-taking application with a user-friendly interface.

Git Hub Repository Link: "https://github.com/Lorydima/NeonNote"

NeonNote Website link: "https://lorydima.github.io/NeonNote/"
'''

# Library for app Dev.
from tkinter import filedialog, messagebox
from tkinter import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import webbrowser
import win32api
import win32print
import time
import pyperclip
import os
import json
import tempfile
import re

# Markdown Variable
converted_markdown = ""

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
    try:
        file_handle = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file_handle is None:
            return
        text = Entry.get(1.0, END)
        file_handle.write(text)
        file_handle.close()
        try:
            window.title(f"NeonNote V1.1 - {os.path.basename(file_handle.name)}")
        except Exception:
            pass
        messagebox.showinfo("File Saved", "Your file has been saved successfully.")
    except Exception as e:
        messagebox.showerror("File Save Error", f"Failed to save file: {e}")

# Open Function
def open_file():
    global Entry, window
    try:
        file_handle = filedialog.askopenfile(mode='r', defaultextension=".txt")
        if file_handle is not None:
            content = file_handle.read()
            Entry.delete(1.0, END)
            Entry.insert(INSERT, content)
            try:
                window.title(f"NeonNote V1.1 - {os.path.basename(file_handle.name)}")
            except Exception:
                pass
            messagebox.showinfo("File Opened", "Your file has been opened successfully.")
        else:
            return
    except Exception as e:
        messagebox.showerror("File Open Error", f"Failed to open file: {e}")

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

    info_label = Label(info_window, text="NeonNote Version 1.1\nDev: LDM Dev.", bg="#c6c6c6", font=("Arial", 18))
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
        info_window, text="Read License",
        command=lambda: read_license_window(),
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
    mf_win.geometry("700x300")  
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
    def print_text():
        try:
            text = Entry.get(1.0, END)
            if not text.strip():
                messagebox.showinfo("Print", "Nothing to print.")
                return
            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode='w', encoding='utf-8') as tmp:
                tmp.write(text)
                tmp_path = tmp.name

            default_printer = None
            try:
                try:
                    default_printer = win32print.GetDefaultPrinter()
                except Exception:
                    default_printer = None

                if default_printer:
                    try:
                        win32api.ShellExecute(0, "printto", tmp_path, '"%s"' % default_printer, ".", 0)
                        messagebox.showinfo("Print", f"Sent to printer: {default_printer}")
                        return
                    except Exception:
                        try:
                            hPrinter = win32print.OpenPrinter(default_printer)
                        except Exception:
                            hPrinter = None

                        if hPrinter:
                            try:
                                with open(tmp_path, 'rb') as fh:
                                    data = fh.read()
                                win32print.StartDocPrinter(hPrinter, 1, ("NeonNotePrint", None, "RAW"))
                                win32print.StartPagePrinter(hPrinter)
                                win32print.WritePrinter(hPrinter, data)
                                win32print.EndPagePrinter(hPrinter)
                                win32print.EndDocPrinter(hPrinter)
                                messagebox.showinfo("Print", f"Sent to printer: {default_printer}")
                                return
                            finally:
                                try:
                                    win32print.ClosePrinter(hPrinter)
                                except Exception:
                                    pass
            except Exception:
                default_printer = None
            if not default_printer:
                try:
                    import subprocess
                    ps_cmd = '(Get-Printer | Where-Object {$_.Default -eq $true}).Name'
                    completed = subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], capture_output=True, text=True)
                    name = completed.stdout.strip()
                    if name:
                        default_printer = name
                except Exception:
                    default_printer = None

            if not default_printer:
                messagebox.showerror("Print Error", "No default printer found. Configure a printer in Windows settings.")
                return
            try:
                os.startfile(tmp_path, "print")
                messagebox.showinfo("Print", "Opened system print dialog (fallback).")
            except Exception as e:
                messagebox.showerror("Print Error", f"Failed to open system print dialog: {e}")
        except Exception as e:
            messagebox.showerror("Print Error", f"Unexpected error: {e}")

    def convert_to_markdown():
        global converted_markdown
        try:
            text = Entry.get(1.0, END)
            if not text.strip():
                messagebox.showinfo("Convert Markdown", "No text to convert.")
                return
            lines = text.splitlines()
            out_lines = []
            in_code = False
            for line in lines:
                if line.startswith('    ') or line.startswith('\t'):
                    if not in_code:
                        out_lines.append('```')
                        in_code = True
                    out_lines.append(line.lstrip(' \t'))
                    continue
                else:
                    if in_code:
                        out_lines.append('```')
                        in_code = False
                stripped = line.strip()
                if stripped and stripped == stripped.upper() and len(stripped) <= 60 and ' ' in stripped:
                    out_lines.append('# ' + stripped.title())
                else:
                    out_lines.append(line)
            if in_code:
                out_lines.append('```')
            in_code = False
            processed_lines = []
            for l in out_lines:
                if l.strip() == '```':
                    processed_lines.append(l)
                    in_code = not in_code
                    continue
                if not in_code:
                    l = re.sub(r'(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)', r'**\1**', l)
                    l = re.sub(r'(?<!_)_(?!\s)(.+?)(?<!\s)_(?!_)', r'**\1**', l)
                processed_lines.append(l)

            converted_markdown = '\n'.join(processed_lines)

            md_win = Toplevel()
            md_win.title("Markdown Preview")
            md_win.geometry("700x500")
            try:
                md_win.iconbitmap(ICON_PATH)
            except Exception:
                pass
            md_text = Text(md_win, bg="#ffffff", fg="#000000", font=("Consolas", 11), wrap=WORD)

            md_text.tag_configure("h1", font=("Consolas", 18, "bold"))
            md_text.tag_configure("h2", font=("Consolas", 16, "bold"))
            md_text.tag_configure("h3", font=("Consolas", 14, "bold"))
            md_text.tag_configure("bold", font=("Consolas", 11, "bold"))
            md_text.tag_configure("inline_code", font=("Consolas", 11), background="#eef2f5")
            md_text.tag_configure("code_block", font=("Consolas", 11), background="#f4f4f4")
            md_text.tag_configure("blockquote", font=("Consolas", 11, "italic"), foreground="#666666", lmargin1=20)
            md_text.tag_configure("list", lmargin1=20)

            lines = converted_markdown.splitlines()
            i = 0
            while i < len(lines):
                line = lines[i]
                stripped = line.strip()
                if stripped.startswith('```'):
                    i += 1
                    while i < len(lines) and not lines[i].strip().startswith('```'):
                        md_text.insert(END, lines[i] + "\n", "code_block")
                        i += 1
                    i += 1
                    continue

                m = re.match(r'^(#{1,6})\s+(.*)', line)
                if m:
                    level = len(m.group(1))
                    content = m.group(2) + "\n"
                    tag = f"h{min(level,3)}"
                    md_text.insert(END, content, tag)
                    i += 1
                    continue

                if re.match(r'^\s*([-*]\s+|\d+\.\s+)', line):
                    item = re.sub(r'^\s*([-*]\s+|\d+\.\s+)', '• ', line)
                    md_text.insert(END, item, "list")
                    i += 1
                    continue

                if stripped.startswith('>'):
                    content = stripped.lstrip('> ').rstrip() + "\n"
                    md_text.insert(END, content, "blockquote")
                    i += 1
                    continue

                pos = 0
                for mm in re.finditer(r'(`.+?`)|\*\*(.+?)\*\*', line):
                    pre = line[pos:mm.start()]
                    if pre:
                        md_text.insert(END, pre)
                    if mm.group(1):
                        code = mm.group(1)[1:-1]
                        md_text.insert(END, code, "inline_code")
                    else:
                        bold = mm.group(2)
                        md_text.insert(END, bold, "bold")
                    pos = mm.end()
                rem = line[pos:]
                if rem:
                    md_text.insert(END, rem)
                md_text.insert(END, "\n")
                i += 1

            md_text.config(state=DISABLED)
            md_text.pack(padx=10, pady=10, fill=BOTH, expand=True)
            def on_export():
                export_markdown()
            export_btn = Button(md_win, text="Export in Markdown", command=on_export, bg="#2f72bb", fg="white", font=("Arial", 12, "bold"), width=20, height=1, relief="solid", bd=1, cursor="hand2")
            export_btn.pack(pady=8)

        except Exception as e:
            messagebox.showerror("Convert Markdown Error", f"Failed to convert: {e}")

    def export_markdown():
        global converted_markdown
        try:
            if not converted_markdown or not converted_markdown.strip():
                messagebox.showinfo("Export Markdown", "No converted Markdown present. Please convert first.")
                return
            save_path = filedialog.asksaveasfilename(defaultextension='.md', filetypes=[('Markdown', '*.md')])
            if not save_path:
                return
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(converted_markdown)
            messagebox.showinfo("Export Markdown", f"Saved Markdown to {save_path}")
        except Exception as e:
            messagebox.showerror("Export Markdown Error", f"Failed to export: {e}")

    def export_pdf():
        try:
            text = Entry.get(1.0, END)
            if not text.strip():
                messagebox.showinfo("Export PDF", "No text to export.")
                return
            save_path = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[('PDF', '*.pdf')])
            if not save_path:
                return
                return
            c = canvas.Canvas(save_path, pagesize=letter)
            width, height = letter
            lines = text.splitlines()
            y = height - 40
            left_margin = 40
            line_height = 12
            for line in lines:
                while len(line) > 0:
                    chunk = line[:90]
                    c.drawString(left_margin, y, chunk)
                    line = line[90:]
                    y -= line_height
                    if y < 40:
                        c.showPage()
                        y = height - 40
            c.save()
            messagebox.showinfo("Export PDF", f"Saved PDF to {save_path}")
        except Exception as e:
            messagebox.showerror("Export PDF Error", f"Failed to export PDF: {e}")
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
    Button(right_frame, text="Print text", width=18, font=("Arial", 12, "bold"), bg="#2f72bb", fg="white", relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2", command=print_text).pack(pady=5)
    Button(right_frame, text="Convert to Markdown", width=18, font=("Arial", 12, "bold"), bg="#2f72bb", fg="white", relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2", command=convert_to_markdown).pack(pady=5)
    Button(right_frame, text="Export as PDF", width=18, font=("Arial", 12, "bold"), bg="#2f72bb", fg="white", relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2", command=export_pdf).pack(pady=5)

    # Shortcuts info 
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

    license_text = """NeonNote — Source-Available License

This license applies to NeonNote latest version and all future versions of the software unless otherwise stated.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Scope of the Software
“Software” refers to all files included in the downloaded folder, including but not limited to:
- The executable file (.exe)
- The data file (DATA.json)
- The icon file (.ico)
- Any other files distributed with the application

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2. Source Code Access
The source code is available on GitHub for educational and personal reference only.
You are allowed to:
- View and study the code for learning purposes

You are not allowed to:
- Reuse, modify, or incorporate the code into your own projects
- Distribute the code in any form
- Use the software or its code for commercial purposes, including selling, licensing, or integrating it into paid products or services

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3. Redistribution Restrictions
- You may not republish or redistribute the software or its source code, in whole or in part, in any form or on any platform (including GitHub), without explicit written permission from LDM Dev.
- Forking or copying the GitHub repository is not permitted.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. Ownership
All components of the software and its source code are the intellectual property of LDM Dev.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5. Respect for Creative Work
Please respect the effort and creativity behind this project. Do not claim it as your own or use it in ways that disregard the author's intent. Sharing knowledge is valuable — so is recognizing the work of others.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6. Disclaimer
The software is provided “as is”, without any warranties, express or implied. Use it at your own risk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Thank You for your collaboration from LDM Dev.
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
    window.title("NeonNote V1.1")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}")
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

def read_license_window():
    lic_win = Toplevel()
    lic_win.title("License")
    lic_win.geometry("700x500")
    lic_win.configure(bg="#c6c6c6")
    lic_win.resizable(False, False)
    try:
        lic_win.iconbitmap(ICON_PATH)
    except Exception:
        pass

    license_text = """NeonNote — Source-Available License

This license applies to NeonNote latest version and all future versions of the software unless otherwise stated.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Scope of the Software
“Software” refers to all files included in the downloaded folder, including but not limited to:
- The executable file (.exe)
- The data file (DATA.json)
- The icon file (.ico)
- Any other files distributed with the application

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2. Source Code Access
The source code is available on GitHub for educational and personal reference only.
You are allowed to:
- View and study the code for learning purposes

You are not allowed to:
- Reuse, modify, or incorporate the code into your own projects
- Distribute the code in any form
- Use the software or its code for commercial purposes, including selling, licensing, or integrating it into paid products or services

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3. Redistribution Restrictions
- You may not republish or redistribute the software or its source code, in whole or in part, in any form or on any platform (including GitHub), without explicit written permission from LDM Dev.
- Forking or copying the GitHub repository is not permitted.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. Ownership
All components of the software and its source code are the intellectual property of LDM Dev.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5. Respect for Creative Work
Please respect the effort and creativity behind this project. Do not claim it as your own or use it in ways that disregard the author's intent. Sharing knowledge is valuable — so is recognizing the work of others.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6. Disclaimer
The software is provided “as is”, without any warranties, express or implied. Use it at your own risk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Thank You for your collaboration from LDM Dev.
"""

    # Header label
    header = Label(lic_win, text="NeonNote License", bg="#c6c6c6", font=("Arial", 16, "bold"))
    header.pack(pady=10)

    text_box = Text(lic_win, bg="#f0f0f0", fg="#000000", font=("Arial", 11), wrap=WORD, height=20, relief="solid", bd=1)
    text_box.insert(1.0, license_text)
    text_box.config(state=DISABLED)
    text_box.pack(padx=20, pady=10, fill=BOTH, expand=True)

    

# Call Main Function
if __name__ == "__main__":
    if check_license():
        gui_function()
    else:
        show_license_window()