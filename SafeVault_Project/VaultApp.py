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
    if len(p) < 3 and len(p) > 0:
        messagebox.showinfo("Error", "Sorry you need more characters for a secure password.")
        return
    length = len(p)
    special = "?!<>#$%@&*"
    special_count = 0
    for char in p:
        if char in special:
            special_count = special_count + 1
    score = length + (special_count * 2)
    percent = int((score / 20) * 100)
    if percent > 100:
        percent = 100
    bar_end = 10 + int((percent / 100) * 340)
    if score == 0:
        strength_label.config(text="Status: None", fg="gray", bg="#2a2a3e")
        percent_label.config(text="0%", fg="gray")
        canvas.coords(bar_mask, 10, 4, 352, 19)
    if score >= 1 and score <= 5:
        strength_label.config(text="Status: Weak", fg="red", bg="#3a1a1a")
        percent_label.config(text=str(percent) + "%", fg="red")
        canvas.coords(bar_mask, bar_end, 4, 352, 19)
    if score >= 6 and score <= 10:
        strength_label.config(text="Status: Okay", fg="orange", bg="#3a2a1a")
        percent_label.config(text=str(percent) + "%", fg="orange")
        canvas.coords(bar_mask, bar_end, 4, 352, 19)
    if score >= 11 and score <= 15:
        strength_label.config(text="Status: Good", fg="yellow", bg="#2a2a1a")
        percent_label.config(text=str(percent) + "%", fg="yellow")
        canvas.coords(bar_mask, bar_end, 4, 352, 19)
    if score >= 16:
        strength_label.config(text="Status: Solid", fg="#00cc44", bg="#1a3a1a")
        percent_label.config(text=str(percent) + "%", fg="#00cc44")
        canvas.coords(bar_mask, 352, 4, 352, 19)

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
    elif len(pw) < 3:
        messagebox.showinfo("Error", "Sorry you need more characters for a secure password.")
    else:
        result = data_manager.add_to_json(site, pw, username)
        if result == "duplicate":
            messagebox.showinfo("Error", "You cant save the same password for the same website/user twice.")
        else:
            add_saved_row(site, username, pw)
            count_label.config(text="Saved Passwords: " + str(data_manager.count_entries()))
            messagebox.showinfo("Saved", "Password added to vault")

def clear_all():
    entered = simpledialog.askstring("Confirm", "Enter your master password to clear all passwords:", show="*")
    if entered == master_password:
        answer = messagebox.askyesno("Warning", "Are you SURE you want to completely delete all saved passwords? You will NOT be able to recover it")
        if answer == True:
            path = "database/vault_data.json"
            f = open(path, "w")
            f.write("[]")
            f.close()
            for widget in saved_frame.winfo_children():
                widget.destroy()
            count_label.config(text="Saved Passwords: 0")
            messagebox.showinfo("Cleared", "All saved passwords have been deleted")
    else:
        messagebox.showinfo("Wrong", "Incorrect master password")

def add_saved_row(site, username, pw):
    row = tk.Frame(saved_frame, bg="#2a2a3e", pady=3)
    row.pack(anchor="w", fill="x")

    tk.Frame(saved_frame, bg="#3a3a4e", height=1).pack(fill="x")

    if username != "":
        display_text = site + " (" + username + ")"
    else:
        display_text = site

    tk.Label(row, text=display_text + "  ", bg="#2a2a3e", fg="white").pack(side="left", padx=5)

    pw_label = tk.Label(row, text="••••••••", bg="#1a1a2e", fg="#1a1a2e")
    pw_label.pack(side="left")

    is_showing = [False]

    show_btn = tk.Button(row, text="👁", bg="#2a3a5a", fg="white", relief="flat", padx=6, pady=2)
    show_btn.pack(side="left", padx=4)

    del_btn = tk.Button(row, text="🗑", bg="#5a1a1a", fg="white", relief="flat", padx=6, pady=2)
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
            count_label.config(text="Saved Passwords: " + str(data_manager.count_entries()))
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
app.geometry("480x780")
app.config(bg="#1a1a2e")

setup_master()

tk.Label(app, text="SECURE ACCESS PORTAL", bg="#1e3a5f", fg="white",
         width=50, pady=12).pack(fill="x")

frame1 = tk.Frame(app, bg="#2a2a3e", padx=20, pady=15)
frame1.pack(pady=10, padx=15, fill="x")

tk.Label(frame1, text="Website Name:", bg="#2a2a3e", fg="white").pack(anchor="w")
site_box = tk.Entry(frame1, bg="#1a1a2e", fg="white", insertbackground="white",
                    relief="flat", bd=6, highlightthickness=1,
                    highlightbackground="#3a5a8a", highlightcolor="#5a8abf")
site_box.pack(fill="x", pady=5)

tk.Label(frame1, text="Username / Email:  (optional)", bg="#2a2a3e", fg="gray").pack(anchor="w")
user_box = tk.Entry(frame1, bg="#1a1a2e", fg="white", insertbackground="white",
                    relief="flat", bd=6, highlightthickness=1,
                    highlightbackground="#3a5a8a", highlightcolor="#5a8abf")
user_box.pack(fill="x", pady=5)

tk.Label(frame1, text="Password:", bg="#2a2a3e", fg="white").pack(anchor="w")
pass_box = tk.Entry(frame1, bg="#1a1a2e", fg="white", insertbackground="white",
                    relief="flat", bd=6, show="•", highlightthickness=1,
                    highlightbackground="#3a5a8a", highlightcolor="#5a8abf")
pass_box.pack(fill="x", pady=5)

frame2 = tk.Frame(app, bg="#2a2a3e", padx=20, pady=15)
frame2.pack(pady=5, padx=15, fill="x")

strength_top = tk.Frame(frame2, bg="#2a2a3e")
strength_top.pack(fill="x")

tk.Label(strength_top, text="Password Security Strength", bg="#2a2a3e", fg="white").pack(side="left")

right_info = tk.Frame(strength_top, bg="#2a2a3e")
right_info.pack(side="right")

percent_label = tk.Label(right_info, text="0%", bg="#2a2a3e", fg="gray")
percent_label.pack(side="left", padx=6)

strength_label = tk.Label(right_info, text="Status: None", bg="#2a2a3e", fg="gray", padx=8, pady=2)
strength_label.pack(side="left")

canvas = tk.Canvas(frame2, height=22, bg="#2a2a3e", highlightthickness=0)
canvas.pack(fill="x", pady=6)

canvas.create_rectangle(10, 4, 120, 19, fill="#aa0000", outline="")
canvas.create_rectangle(120, 4, 210, 19, fill="#cc5500", outline="")
canvas.create_rectangle(210, 4, 290, 19, fill="#aaaa00", outline="")
canvas.create_rectangle(290, 4, 352, 19, fill="#00aa33", outline="")
bar_mask = canvas.create_rectangle(10, 4, 352, 19, fill="#3a3a4e", outline="")

btn_frame = tk.Frame(frame2, bg="#2a2a3e")
btn_frame.pack(fill="x", pady=8)

btn_style = {"bg": "#2a3a5a", "fg": "white", "relief": "flat",
             "padx": 8, "pady": 10, "width": 20}

tk.Button(btn_frame, text="↺  Re-check Strength", command=check_strength, **btn_style).grid(row=0, column=0, padx=4, pady=4)
tk.Button(btn_frame, text="💾  Save Password", command=run_save, **btn_style).grid(row=0, column=1, padx=4, pady=4)
tk.Button(btn_frame, text="🔍  Vault Search", command=run_search, **btn_style).grid(row=1, column=0, padx=4, pady=4)
tk.Button(btn_frame, text="🛡  API Security Scan", command=check_hacker_list, **btn_style).grid(row=1, column=1, padx=4, pady=4)

tk.Button(frame2, text="✖  Clear All Saved Passwords", command=clear_all,
          bg="#5a1a1a", fg="white", relief="flat", padx=10, pady=8, width=40).pack(pady=6)

count_label = tk.Label(app, text="Saved Passwords: " + str(data_manager.count_entries()), bg="#1a1a2e", fg="white")
count_label.pack(anchor="w", padx=20, pady=5)

saved_frame = tk.Frame(app, bg="#2a2a3e", padx=15, pady=10)
saved_frame.pack(padx=15, fill="x")

load_existing()

app.mainloop()
