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
app.geometry("400x450")
 
tk.Label(app, text="Website Name:").pack(pady=5)
site_box = tk.Entry(app)
site_box.pack()
 
tk.Label(app, text="Password:").pack(pady=5)
pass_box = tk.Entry(app)
pass_box.pack()
 
tk.Button(app, text="Save Password", command=run_save).pack(pady=5)
tk.Button(app, text="Search for Password", command=run_search).pack(pady=5)
tk.Button(app, text="API Security Check", command=check_hacker_list).pack(pady=5)
 
app.mainloop()
