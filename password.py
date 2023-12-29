import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_var = tk.IntVar()
        self.length_entry = tk.Entry(master, textvariable=self.length_var)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(master, text="Generated Password:")
        self.result_label.grid(row=2, column=0, padx=10, pady=10)

        self.result_entry = tk.Entry(master, state="readonly")
        self.result_entry.grid(row=2, column=1, padx=10, pady=10)

    def generate_password(self):
        length = self.length_var.get()
        if length <= 0:
            messagebox.showwarning("Invalid Length", "Password length must be greater than 0.")
            return

        # Generate a random password
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display the generated password
        self.result_entry.config(state="normal")
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, password)
        self.result_entry.config(state="readonly")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
