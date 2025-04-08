import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

SCRIPTS_DIR = "scripts"

def run_batch(file_name):
    try:
        full_path = os.path.join(SCRIPTS_DIR, file_name)
        subprocess.Popen(["cmd.exe", "/c", full_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
        log(f"[{now()}] Launched: {file_name}")
    except Exception as e:
        error_message = f"[{now()}] Error: {str(e)}"
        log(error_message)
        messagebox.showerror("Error", error_message)

def list_scripts():
    return [f for f in os.listdir(SCRIPTS_DIR) if f.endswith(".bat")]

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log(message):
    log_box.config(state='normal')
    log_box.insert(tk.END, message + "\n")
    log_box.config(state='disabled')
    log_box.see(tk.END)

def build_gui():
    global log_box

    root = tk.Tk()
    root.title("Legacy Batch Launcher")
    root.configure(bg="#1a1a1a")

    title = tk.Label(root, text="LEGACY LAUNCHER", fg="red", bg="#1a1a1a", font=("Courier", 18, "bold"))
    title.pack(pady=10)

    for script in list_scripts():
        btn = tk.Button(root, text=script, command=lambda s=script: run_batch(s),
                        bg="black", fg="white", font=("Courier", 12), width=30)
        btn.pack(pady=5)

    exbut = tk.Button(root, text="Exit", command=exit, bg="black", fg="white", font=("Courier", 12), width=30)
    exbut.pack(pady=5)

    log_label = tk.Label(root, text="Log Output:", fg="lime", bg="#1a1a1a", font=("Courier", 12, "bold"))
    log_label.pack(pady=(20, 5))

    log_box = tk.Text(root, height=8, width=60, bg="black", fg="lime", font=("Courier", 10))
    log_box.pack(padx=10, pady=(0, 20))
    log_box.config(state='disabled')

    root.mainloop()

if __name__ == "__main__":
    if not os.path.exists(SCRIPTS_DIR):
        os.makedirs(SCRIPTS_DIR)
    build_gui()