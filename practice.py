# Import the tkinter module for GUI components
import tkinter as tk
# Import the messagebox from tkinter for displaying error messages
from tkinter import messagebox
# Import the math module for mathematical functions like square root
import math

# Define the event handler function for button clicks
def on_click(event):
    # Retrieve the text of the clicked button
    text = event.widget.cget("text")
    try:
        # If the "=" button is clicked, evaluate the expression in the display
        if text == "=":
            display_text.set(eval(display_text.get()))
        # If the "C" button is clicked, clear the display
        elif text == "C":
            display_text.set("")
        # If the "√" button is clicked, calculate the square root of the displayed number
        elif text == "√":
            display_text.set(math.sqrt(float(display_text.get())))
        # If the "^" button is clicked, append the exponentiation operator "**" to the display
        elif text == "^":
            display_text.set(display_text.get() + "**")
        # If the "%" button is clicked, append the "%" character to the display
        elif text == "%":
            display_text.set(display_text.get() + "%")
        # For all other buttons, append their text to the current display content
        else:
            display_text.set(display_text.get() + text)
    except Exception:
        # If an error occurs (e.g., invalid expression), show an error message box
        messagebox.showerror("Error", "Invalid Input")
        # Clear the display after an error
        display_text.set("")

# Create the main application window
root = tk.Tk()
# Set the title of the window to "Calculator"
root.title("Calculator")
# Set the window size to 350x500 pixels
root.geometry("350x500")
# Set the background color of the window
root.configure(bg="#2C3E50")

# Create a StringVar to store the calculator's current expression or result
display_text = tk.StringVar()
# Create an Entry widget (input field) for displaying the current expression/result,
# set its font, justification, border, relief style, background, and foreground colors.
tk.Entry(root, textvariable=display_text, font=("Arial", 24), justify="right", bd=10,
         relief=tk.FLAT, bg="#ECF0F1", fg="#2C3E50").pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Create a frame to hold the button widgets
frame = tk.Frame(root, bg="#2C3E50")
# Pack the frame into the main window
frame.pack()

# Define a list of lists containing the button labels in the desired layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["√", "^", "%"]
]

# Define a helper function to create a button with standardized styling and behavior
def create_button(parent, text):
    # Create a Button widget with the given text and styling attributes
    btn = tk.Button(parent, text=text, font=("Arial", 18, "bold"), width=5, height=2,
                    bg="#3498DB", fg="white", bd=0, relief=tk.RAISED,
                    activebackground="#2980B9", activeforeground="white")
    # Pack the button into the parent container with padding and expansion options
    btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
    # Bind the left mouse button click event to the on_click event handler
    btn.bind("<Button-1>", on_click)

# Loop through each row in the buttons layout
for row in buttons:
    # Create a new frame for the current row of buttons, setting its background color
    row_frame = tk.Frame(frame, bg="#2C3E50")
    # Pack the row frame into the main button frame, expanding it horizontally
    row_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    # Loop through each button text in the current row
    for btn_text in row:
        # Create a button in the current row frame using the create_button helper function
        create_button(row_frame, btn_text)

# Start the Tkinter event loop to listen for user actions
root.mainloop()
