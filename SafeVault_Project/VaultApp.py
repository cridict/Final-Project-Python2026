#API / Webscraping (20 pts) and GUI (10 pts)

import tkinter as tk
from tkinter import messagebox
import requests

def check_hacker_list():
    secret_code = pass_box.get()
    if secret_code == "":
        messagebox.showinfo("Error", "Type a password first")
    else:
        messagebox.showinfo("API Scan", "coming soon")

def check_strength():
    p = pass_box.get()
    length = len(p)
    if length == 0:
        strength_label.config(text="Strength: None", fg="gray")
        canvas.coords(bar_fill, 10, 0, 10, 20)
    if length >= 1 and length <= 4:
        strength_label.config(text="Status: Weak", fg="red")
        canvas.coords(bar_fill, 10, 0, 120, 20)
        canvas.itemconfig(bar_fill, fill="red")
    if length >= 5 and length <= 8:
        strength_label.config(text="Status: Okay", fg="orange")
        canvas.coords(bar_fill, 10, 0, 220, 20)
        canvas.itemconfig(bar_fill, fill="orange")
    if length >= 9:
        strength_label.config(text="Status: Solid", fg="green")
        canvas.coords(bar_fill, 10, 0, 340, 20)
        canvas.itemconfig(bar_fill, fill="green")

def run_save():
    site = site_box.get()
    pw = pass_box.get()
    if site == "" or pw == "":
        messagebox.showinfo("Error", "Please fill out both boxes")
    else:
        messagebox.showinfo("Saved", "coming soon")

def run_search():
    messagebox.showinfo("Search", "not done yet")

app = tk.Tk()
app.title("Safe Vault App")
app.geometry("460x550")
app.config(bg="#1a1a2e")

tk.Label(app, text="SECURE ACCESS PORTAL", bg="#1e3a5f", fg="white",
         font=("Arial", 16, "bold"), width=40, pady=10).pack()

frame1 = tk.Frame(app, bg="#2a2a3e", padx=20, pady=20)
frame1.pack(pady=10, padx=20, fill="x")

tk.Label(frame1, text="Website Name:", bg="#2a2a3e", fg="white").pack(anchor="w")
site_box = tk.Entry(frame1, bg="#1a1a2e", fg="gray", insertbackground="white",
                    relief="flat", bd=5)
site_box.insert(0, "e.g., example.com")
site_box.pack(fill="x", pady=5)

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

btn_style = {"bg": "#2a2a4e", "fg": "white", "relief": "flat",
             "padx": 10, "pady": 10, "width": 18}

tk.Button(btn_frame, text="Re-check Strength", command=check_strength, **btn_style).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Securely Save Password", command=run_save, **btn_style).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Vault Search", command=run_search, **btn_style).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Run API Security Scan", command=check_hacker_list, **btn_style).grid(row=1, column=1, padx=5, pady=5)

app.mainloop()
