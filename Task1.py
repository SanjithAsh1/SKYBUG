import tkinter as tk
from tkinter import messagebox

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# Function to perform the selected operation
def perform_operation():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operation = operations_var.get()

        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a number.")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create the input widgets
num1_label = tk.Label(window, text="First number:")
num1_entry = tk.Entry(window)

num2_label = tk.Label(window, text="Second number:")
num2_entry = tk.Entry(window)

operations_var = tk.StringVar()
operations_var.set("Add")

operations_label = tk.Label(window, text="Operation:")
operations_dropdown = tk.OptionMenu(window, operations_var, "Add", "Subtract", "Multiply", "Divide")

calculate_button = tk.Button(window, text="Calculate", command=perform_operation)

# Place the input widgets on the window
num1_label.grid(row=0, column=0)
num1_entry.grid(row=0, column=1)

num2_label.grid(row=1, column=0)
num2_entry.grid(row=1, column=1)

operations_label.grid(row=2, column=0)
operations_dropdown.grid(row=2, column=1)

calculate_button.grid(row=3, column=1)

# Start the main event loop
window.mainloop()