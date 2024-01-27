import tkinter as tk
import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_punctuation=True):
    # Define the character set
    charset = string.ascii_lowercase
    if use_uppercase:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_punctuation:
        charset += string.punctuation

    # Generate the password
    password = ''.join(random.choice(charset) for _ in range(length))

    return password

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_var = tk.IntVar()
        self.use_uppercase_var = tk.BooleanVar()
        self.use_digits_var = tk.BooleanVar()
        self.use_punctuation_var = tk.BooleanVar()

        self.create_widgets()

    def create_widgets(self):
        # Length label and entry
        tk.Label(self.root, text="Length:").pack()
        tk.Entry(self.root, textvariable=self.length_var).pack()

        # Checkbuttons for complexity options
        tk.Checkbutton(self.root, text="Uppercase letters", variable=self.use_uppercase_var).pack()
        tk.Checkbutton(self.root, text="Digits", variable=self.use_digits_var).pack()
        tk.Checkbutton(self.root, text="Punctuation", variable=self.use_punctuation_var).pack()

        # Generate button
        tk.Button(self.root, text="Generate Password", command=self.generate_password).pack()

        # Password label
        self.password_label = tk.Label(self.root, text="")
        self.password_label.pack()

    def generate_password(self):
        length = self.length_var.get()
        use_uppercase = self.use_uppercase_var.get()
        use_digits = self.use_digits_var.get()
        use_punctuation = self.use_punctuation_var.get()

        password = generate_password(length, use_uppercase, use_digits, use_punctuation)

        self.password_label.config(text=password)

root = tk.Tk()
app = PasswordGeneratorApp(root)
root.mainloop()