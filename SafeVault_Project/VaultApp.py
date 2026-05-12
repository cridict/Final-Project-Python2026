#API / Webscraping and GUI

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import requests
import hashlib
import data_manager
import os
 
master_password = ""
 
def setup_master():
    global master_password
    if os.path.exists("database") == False:
        os.mkdir("database")
    path = "database/master.txt"
    if os.path.exists(path) == False:
        pw = simpledialog.askstring("First Time Setup", "Create a master password for your vault:", show="*")
        if pw == None or pw == "":
            pw = "admin"
        f = open(path, "w")
        f.write(pw)
        f.close()
        master_password = pw
        messagebox.showinfo("Done", "Master password saved! Do not forget it.")
    else:
        f = open(path, "r")
        master_password = f.read()
        f.close()
 
def check_hacker_list():
    secret_code = pass_box.get()
    if secret_code == "":
        messagebox.showinfo("Error", "Type a password first")
    else:
        sha1hash = hashlib.sha1(secret_code.encode("utf-8")).hexdigest()
        sha1hash = str(sha1hash).upper()
        first5 = sha1hash[0:5]
        therest = sha1hash[5:]
        url = "https://api.pwnedpasswords.com/range/" + first5
        messagebox.showinfo("API Scan", "Checking the internet for breaches...")
        try:
            response = requests.get(url)
            if therest in response.text:
                messagebox.showinfo("Result", "WARNING: This password was found in a data breach!")
            else:
                messagebox.showinfo("Result", "No breaches found for this password!")
        except:
            messagebox.showinfo("Error", "Could not connect to the internet.")
 
def check_strength():
    p = pass_box.get()
    length = len(p)
    special = "?!<>#$%@&*"
    special_count = 0
    for char in p:
        if char in special:
            special_count = special_count + 1
    score = length + (special_count * 2)
    if score == 0:
        strength_label.config(text="Status: None", fg="gray")
        canvas.coords(bar_fill, 10, 5, 10, 18)
        canvas.itemconfig(bar_fill, fill="gray")
    if score >= 1 and score <= 5:
        strength_label.config(text="Status: Weak", fg="red")
        canvas.coords(bar_fill, 10, 5, 100, 18)
        canvas.itemconfig(bar_fill, fill="red")
    if score >= 6 and score <= 10:
        strength_label.config(text="Status: Okay", fg="orange")
        canvas.coords(bar_fill, 10, 5, 200, 18)
        canvas.itemconfig(bar_fill, fill="orange")
    if score >= 11 and score <= 15:
        strength_label.config(text="Status: Good", fg="yellow")
        canvas.coords(bar_fill, 10, 5, 280, 18)
        canvas.itemconfig(bar_fill, fill="yellow")
    if score >= 16:
        strength_label.config(text="Status: Solid", fg="green")
        canvas.coords(bar_fill, 10, 5, 340, 18)
        canvas.itemconfig(bar_fill, fill="green")
 
def run_search():
    site = site_box.get()
    if site == "":
        messagebox.showinfo("Error", "Type a website name first")
    else:
        result = data_manager.find_password(site)
        messagebox.showinfo("Vault Search", result)
 
def run_save():
    site = site_box.get()
    pw = pass_box.get()
    username = user_box.get()
    if site == "" or pw == "":
        messagebox.showinfo("Error", "Please fill out website and password")
    elif len(pw) < 6:
        messagebox.showinfo("Error", "Password is too short, must be at least 6 characters")
    else:
        data_manager.add_to_json(site, pw, username)
        add_saved_row(site, username, pw)
        messagebox.showinfo("Saved", "Password added to vault")
 
def clear_all():
    answer = messagebox.askyesno("Warning", "Are you SURE you want to completely delete all saved passwords? You will NOT be able to recover it")
    if answer == True:
        path = "database/vault_data.json"
        f = open(path, "w")
        f.write("[]")
        f.close()
        for widget in saved_frame.winfo_children():
            widget.destroy()
        messagebox.showinfo("Cleared", "All saved passwords have been deleted")
 
def add_saved_row(site, username, pw):
    row = tk.Frame(saved_frame, bg="#2a2a3e")
    row.pack(anchor="w", fill="x", pady=2)
 
    if username != "":
        display_text = site + " (" + username + ")"
    else:
        display_text = site
 
    tk.Label(row, text=display_text + "  ", bg="#2a2a3e", fg="white").pack(side="left")
 
    pw_label = tk.Label(row, text="••••••••", bg="#1a1a2e", fg="#1a1a2e")
    pw_label.pack(side="left")
 
    is_showing = [False]
 
    show_btn = tk.Button(row, text="👁", bg="#2a2a4e", fg="white", relief="flat", padx=5)
    show_btn.pack(side="left", padx=5)
 
    del_btn = tk.Button(row, text="🗑", bg="#5a1a1a", fg="white", relief="flat", padx=5)
    del_btn.pack(side="left", padx=2)
 
    def toggle():
        if is_showing[0] == False:
            entered = simpledialog.askstring("Unlock", "Enter your master password:", show="*")
            if entered == master_password:
                pw_label.config(text=pw, fg="white", bg="#2a2a3e")
                is_showing[0] = True
            else:
                messagebox.showinfo("Wrong", "Incorrect master password")
        else:
            pw_label.config(text="••••••••", fg="#1a1a2e", bg="#1a1a2e")
            is_showing[0] = False
 
    def delete_row():
        entered = simpledialog.askstring("Confirm Delete", "Enter your master password to delete this entry:", show="*")
        if entered == master_password:
            data_manager.delete_one_entry(site, username)
            row.destroy()
        else:
            messagebox.showinfo("Wrong", "Incorrect master password")
 
    show_btn.config(command=toggle)
    del_btn.config(command=delete_row)
 
def load_existing():
    entries = data_manager.get_all_entries()
    for entry in entries:
        site = entry["website"]
        username = entry["username"]
        pw = entry["password"]
        add_saved_row(site, username, pw)
 
app = tk.Tk()
app.title("Safe Vault App")
app.geometry("460x750")
app.config(bg="#1a1a2e")
 
setup_master()
 
tk.Label(app, text="SECURE ACCESS PORTAL", bg="#1e3a5f", fg="white",
         width=40, pady=10).pack()
 
frame1 = tk.Frame(app, bg="#2a2a3e", padx=20, pady=20)
frame1.pack(pady=10, padx=20, fill="x")
 
tk.Label(frame1, text="Website Name:", bg="#2a2a3e", fg="white").pack(anchor="w")
site_box = tk.Entry(frame1, bg="#1a1a2e", fg="white", insertbackground="white",
                    relief="flat", bd=5)
site_box.pack(fill="x", pady=5)
 
tk.Label(frame1, text="Username / Email:  (optional)", bg="#2a2a3e", fg="gray").pack(anchor="w")
user_box = tk.Entry(frame1, bg="#1a1a2e", fg="white", insertbackground="white",
                    relief="flat", bd=5)
user_box.pack(fill="x", pady=5)
 
tk.Label(frame1, text="Password:", bg="#2a2a3e", fg="white").pack(anchor="w")
pass_box = tk.Entry(frame1, bg="#1a1a2e", fg="white", insertbackground="white",
                    relief="flat", bd=5, show="•")
pass_box.pack(fill="x", pady=5)
 
frame2 = tk.Frame(app, bg="#2a2a3e", padx=20, pady=15)
frame2.pack(pady=5, padx=20, fill="x")
 
tk.Label(frame2, text="Password Security Strength", bg="#2a2a3e", fg="white").pack(anchor="w")
 
canvas = tk.Canvas(frame2, height=20, bg="#2a2a3e", highlightthickness=0)
canvas.pack(fill="x", pady=5)
canvas.create_rectangle(10, 5, 350, 18, fill="#3a3a4e", outline="")
bar_fill = canvas.create_rectangle(10, 5, 10, 18, fill="gray", outline="")
 
strength_label = tk.Label(frame2, text="Status: None", bg="#2a2a3e", fg="gray")
strength_label.pack(anchor="e")
 
btn_frame = tk.Frame(frame2, bg="#2a2a3e")
btn_frame.pack(fill="x", pady=10)
 
btn_style = {"bg": "#2a2a4e", "fg": "white", "relief": "flat", "padx": 10, "pady": 10, "width": 18}
 
tk.Button(btn_frame, text="Re-check Strength", command=check_strength, **btn_style).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Securely Save Password", command=run_save, **btn_style).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Vault Search", command=run_search, **btn_style).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Run API Security Scan", command=check_hacker_list, **btn_style).grid(row=1, column=1, padx=5, pady=5)
 
tk.Button(frame2, text="Clear All Saved Passwords", command=clear_all,
          bg="#5a1a1a", fg="white", relief="flat", padx=10, pady=8, width=38).pack(pady=5)
 
tk.Label(app, text="Saved Passwords:", bg="#1a1a2e", fg="white").pack(anchor="w", padx=20, pady=5)
 
saved_frame = tk.Frame(app, bg="#2a2a3e", padx=20, pady=10)
saved_frame.pack(padx=20, fill="x")
 
load_existing()
 
app.mainloop()
