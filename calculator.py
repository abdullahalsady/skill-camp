import tkinter as tk
from tkinter import messagebox
import math
import re

def on_click(event):
    text = event.widget.cget("text")

    try:
        if text == "=":
            expression = display_text.get().replace("^", "**")
            expression = re.sub(r"(\d+)%", r"(\1/100)", expression)
            display_text.set(eval(expression))
        elif text == "C":
            display_text.set("")
        elif text == "√":
            display_text.set(str(math.sqrt(float(display_text.get()))))
        elif text == "^":
            display_text.set(display_text.get() + "^")
        elif text == "%":
            display_text.set(display_text.get() + "%")
        else:
            display_text.set(display_text.get() + text)
    except Exception:
        messagebox.showerror("Error", "Invalid Input")
        display_text.set("")

root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.configure(bg="#2C3e50")

display_text = tk.StringVar()
tk.Entry(root, textvariable=display_text, font=("Arial", 24), justify="right", bd=10, relief=tk.FLAT, bg="#ECF0F1", fg="#2C3E50").pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

frame = tk.Frame(root, bg="#2C3E50")
frame.pack()


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["√", "^", "%"]
]

def create_button(parent, text):
    btn = tk.Button(parent, text=text, font=("Arial", 18, "bold"), bd=0, width=5, height=2, relief=tk.RAISED, bg="#3498DB", fg="white", activebackground="#2980B9", activeforeground="white")
    btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
    btn.bind("<Button-1>", on_click)

for row in buttons:
    row_frame = tk.Frame(frame, bg="#2C3E50")
    row_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    for btn_text in row:
        create_button(row_frame, btn_text)

root.mainloop()