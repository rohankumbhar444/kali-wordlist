
#!/usr/bin/env python3
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def run_aircrack():
    cap_file = cap_entry.get()
    wordlist = wordlist_entry.get()

    if not cap_file or not wordlist:
        messagebox.showerror("Error", "Please select both .cap file and wordlist!")
        return

    cmd = ["x-terminal-emulator", "-e", f"aircrack-ng '{cap_file}' -w '{wordlist}'"]
    try:
        subprocess.Popen(cmd)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run aircrack-ng:\n{e}")

def browse_cap():
    filename = filedialog.askopenfilename(filetypes=[("Capture Files", "*.cap")])
    cap_entry.delete(0, tk.END)
    cap_entry.insert(0, filename)

def browse_wordlist():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    wordlist_entry.delete(0, tk.END)
    wordlist_entry.insert(0, filename)

# GUI layout
root = tk.Tk()
root.title("Aircrack-ng GUI Tool (Kali Linux)")
root.geometry("500x200")
root.resizable(False, False)

tk.Label(root, text="Select .cap file:").pack(pady=5)
cap_entry = tk.Entry(root, width=60)
cap_entry.pack()
tk.Button(root, text="Browse", command=browse_cap).pack(pady=3)

tk.Label(root, text="Select Wordlist file:").pack(pady=5)
wordlist_entry = tk.Entry(root, width=60)
wordlist_entry.pack()
tk.Button(root, text="Browse", command=browse_wordlist).pack(pady=3)

tk.Button(root, text="Start Cracking", command=run_aircrack, bg="green", fg="white").pack(pady=10)

root.mainloop()
