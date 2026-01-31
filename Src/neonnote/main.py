# NeonNote V.1.2 Source Code Date: 31/01/2026 Dev: LDM Dev.

'''
NeonNote is a simple note-taking application with a user-friendly interface.

Git Hub Repository Link: "https://github.com/Lorydima/NeonNote"

NeonNote Website link: "https://lorydima.github.io/NeonNote/"

Before you use this code read the license in the LICENSE.txt or on Git Hub Repository.

If you discover a security vulnerability please read the file SECURITY.md on the Git Hub Repository.
'''

# Library for app Dev.
from tkinter import *
from tkinter import filedialog, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import webbrowser
import os
import time
import tempfile
import re
import pyperclip
import win32api
import win32print


# Icon Path
ICON_PATH = os.path.join(os.path.dirname(__file__), "NeonNote_Icon.ico")
LOGO_PATH = os.path.join(os.path.dirname(__file__), "NeonNote_Logo.png")

# Markdown Variable
converted_markdown = ""

def save_file():
    """
    Saves the current text content to a file.
    """
    global Entry, window
    try:
        file_handle = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file_handle is None:
            return
        text = Entry.get(1.0, END)
        file_handle.write(text)
        file_handle.close()
        try:
            window.title(f"NeonNote V1.2 - {os.path.basename(file_handle.name)}")
        except Exception:
            pass
        messagebox.showinfo("File Saved", "Your file has been saved successfully.")
    except Exception as e:
        messagebox.showerror("File Save Error", f"Failed to save file: {e}")

def open_file():
    """
    Opens a text file and loads it into the editor.
    """
    global Entry, window
    try:
        file_handle = filedialog.askopenfile(mode='r', defaultextension=".txt")
        if file_handle is not None:
            content = file_handle.read()
            Entry.delete(1.0, END)
            Entry.insert(INSERT, content)
            try:
                window.title(f"NeonNote V1.2 - {os.path.basename(file_handle.name)}")
            except Exception:
                pass
            messagebox.showinfo("File Opened", "Your file has been opened successfully.")
        else:
            return
    except Exception as e:
        messagebox.showerror("File Open Error", f"Failed to open file: {e}")

def read_license_window():
    """
    Displays the license agreement in a new window.
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

    license_path = os.path.join(os.path.dirname(__file__), "LICENSE.txt")
    license_text = "LICENSE.txt not found."
    if os.path.exists(license_path):
        try:
            with open(license_path, "r", encoding="utf-8") as f:
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
    Displays the application information window.
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

    create_styled_button("NeonNote GitHub Repository", lambda: webbrowser.open("https://github.com/Lorydima/NeonNote"))
    create_styled_button("NeonNote Website", lambda: webbrowser.open("https://lorydima.github.io/NeonNote/"))
    create_styled_button("Read License", read_license_window)

def more_functions_window():
    """
    Displays the window with additional functions (Print, PDF, Markdown, etc.).
    """
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

    def Write_time():
        """Inserts current time."""
        Entry.insert(INSERT, time.strftime("%H:%M:%S") + "\n")
    def Write_date():
        """Inserts current date."""
        Entry.insert(INSERT, time.strftime("%d/%m/%Y") + "\n")
    
    def print_text():
        """Handles printing of the text."""
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
                        pass
            except Exception:
                pass
            
            try:
                os.startfile(tmp_path, "print")
                messagebox.showinfo("Print", "Opened system print dialog (fallback).")
            except Exception as e:
                messagebox.showerror("Print Error", f"Failed to open system print dialog: {e}")
        except Exception as e:
            messagebox.showerror("Print Error", f"Unexpected error: {e}")

    def convert_to_markdown():
        """Converts text to markdown and shows preview."""
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
            md_text.tag_configure("bold", font=("Consolas", 11, "bold"))
            
            md_text.insert(END, converted_markdown)
            
            md_text.config(state=DISABLED)
            md_text.pack(padx=10, pady=10, fill=BOTH, expand=True)
            
            def on_export():
                export_markdown()
            export_btn = Button(md_win, text="Export in Markdown", command=on_export, bg="#2f72bb", fg="white", font=("Arial", 12, "bold"), width=20, height=1, relief="solid", bd=1, cursor="hand2")
            export_btn.pack(pady=8)

        except Exception as e:
            messagebox.showerror("Convert Markdown Error", f"Failed to convert: {e}")

    def export_markdown():
        """Exports markdown to file."""
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
        """Exports text to PDF."""
        try:
            text = Entry.get(1.0, END)
            if not text.strip():
                messagebox.showinfo("Export PDF", "No text to export.")
                return
            save_path = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[('PDF', '*.pdf')])
            if not save_path:
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
        """Copies all text."""
        pyperclip.copy(Entry.get(1.0, END))
        messagebox.showinfo("Copy Successful", "All text has been copied to clipboard.")
    def delete_all():
        """Deletes all text."""
        Entry.delete(1.0, END)
        messagebox.showinfo("Delete Successful", "All text has been deleted.")
    def count_chars_words():
        """Counts characters and words."""
        text = Entry.get(1.0, END)
        chars = len(text) - 1  
        words = len(text.split())
        messagebox.showinfo("Count", f"Characters: {chars}\nWords: {words}")

    center_frame = Frame(mf_win, bg="#c6c6c6")
    center_frame.place(x=0, y=60)

    def create_grid_btn(parent, text, cmd):
        return Button(parent, text=text, width=18, font=("Arial", 12, "bold"), bg="#2f72bb", fg="white", relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2", command=cmd)

    left_frame = Frame(center_frame, bg="#c6c6c6")
    left_frame.grid(row=0, column=0, padx=20)
    create_grid_btn(left_frame, "Write actual time", Write_time).pack(pady=5)
    create_grid_btn(left_frame, "Write actual date", Write_date).pack(pady=5)
    create_grid_btn(left_frame, "Count chars/words", count_chars_words).pack(pady=5)

    right_frame = Frame(center_frame, bg="#c6c6c6")
    right_frame.grid(row=0, column=1, padx=20)
    create_grid_btn(right_frame, "Print text", print_text).pack(pady=5)
    create_grid_btn(right_frame, "Convert to Markdown", convert_to_markdown).pack(pady=5)
    create_grid_btn(right_frame, "Export as PDF", export_pdf).pack(pady=5)

    shortcuts_text = "Ctrl+S  →  Save file\nCtrl+O  →  Open file\nCtrl+I  →  Info\nCtrl+M  →  More Functions\nESC     →  Exit"
    shortcuts_label = Label(mf_win, text=shortcuts_text, bg="#c6c6c6", fg="#17508a", font=("Arial", 13, "bold"), justify=LEFT)
    shortcuts_label.place(x=470, y=100)

    bottom_frame = Frame(mf_win, bg="#c6c6c6")
    bottom_frame.place(y=225)
    create_grid_btn(bottom_frame, "Copy all Text", copy_all).grid(row=0, column=0, padx=20)
    create_grid_btn(bottom_frame, "Delete all Text", delete_all).grid(row=0, column=1, padx=20)

def gui_function():
    """
    Initializes and runs the main GUI of the application.
    """
    global Entry, window
    window = Tk()
    window.title("NeonNote V1.2")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}")
    window.state('zoomed')
    window.configure(bg="#c6c6c6")
    try:
        window.iconbitmap(ICON_PATH)
    except Exception:
        pass

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

    def create_main_btn(text, cmd, x_pos):
        btn = Button(
            window, text=text, command=cmd, bg="#2f72bb", fg="white",
            font=("Arial", 12, "bold"), width=button_width, height=button_height,
            relief="solid", bd=1, highlightthickness=4, highlightbackground="#17508a", highlightcolor="#17508a", cursor="hand2"
        )
        def on_enter(e): btn['bg'] = "#17508a"
        def on_leave(e): btn['bg'] = "#2f72bb"
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.place(x=x_pos, y=50)
        return btn

    Entry = Text(window, bg="#ffffff", fg="#000000", font=("Arial", 12), relief="solid", highlightthickness=5, highlightbackground="#2f72bb", highlightcolor="#2f72bb", wrap=WORD)
    Entry.place(y=150, width=screen_width, height=screen_height-220)

    create_main_btn("More Functions", more_functions_window, 695)
    create_main_btn("Save file", save_file, 895)
    create_main_btn("Open file", open_file, 1095)
    create_main_btn("Info", info_function, 1295)

    window.bind('<Control-s>', lambda e: save_file())
    window.bind('<Control-o>', lambda e: open_file())
    window.bind('<Control-i>', lambda e: info_function())
    window.bind('<Control-m>', lambda e: more_functions_window())
    window.bind('<Escape>', lambda e: window.destroy())

    window.mainloop()

if __name__ == "__main__":
    gui_function()