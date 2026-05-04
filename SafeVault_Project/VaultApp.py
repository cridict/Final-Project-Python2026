#API / Webscraping (20 pts) and GUI (10 pts)
 
import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("Safe Vault App")
app.geometry("400x450")

tk.Label(app, text="Website Name:").pack(pady=5)
site_box = tk.Entry(app)
site_box.pack()

tk.Label(app, text="Password:").pack(pady=5)
pass_box = tk.Entry(app)
pass_box.pack()

tk.Button(app, text="Save Password").pack(pady=5)
tk.Button(app, text="Search for Password").pack(pady=5)
tk.Button(app, text="API Security Check").pack(pady=5)

app.mainloop()
