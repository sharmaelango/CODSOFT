import tkinter as tk

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def add_to_entry(character):
    entry.insert(tk.END, character)
root = tk.Tk()
root.title("Simple Calculator")
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 1), ('8', 1, 2), ('9', 1, 3), ('/', 1, 4),
    ('4', 2, 1), ('5', 2, 2), ('6', 2, 3), ('*', 2, 4),
    ('1', 3, 1), ('2', 3, 2), ('3', 3, 3), ('-', 3, 4),
    ('0', 4, 1), ('.', 4, 2), ('=', 4, 3), ('+', 4, 4)
]

for (text, row, col) in buttons:
    if text != '=':
        button = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: add_to_entry(t))
        button.grid(row=row, column=col, padx=5, pady=5)
    else:
        button = tk.Button(root, text=text, padx=20, pady=10, command=calculate)
        button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
