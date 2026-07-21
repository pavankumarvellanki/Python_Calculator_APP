import tkinter as tk

root = tk.Tk()
root.title("Upgraded Calc")
expression = ""
equation = tk.StringVar()

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    try:
        # eval evaluates the mathematical string expression
        equation.set(str(eval(expression)))
    except:
        equation.set("Error")

def clear():
    global expression
    expression = ""
    equation.set("")

# Keyboard bindings
root.bind('<Return>', lambda event: equal())
root.bind('<Escape>', lambda event: clear())

# Entry Display Window
tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=5).grid(columnspan=4)

# Grid Layout for Buttons
# (Example mapping: row 1 starts below the display entry)
tk.Button(root, text=' 1 ', command=lambda: press(1), height=2, width=7).grid(row=1, column=0)
tk.Button(root, text=' 2 ', command=lambda: press(2), height=2, width=7).grid(row=1, column=1)
tk.Button(root, text=' + ', command=lambda: press('+'), height=2, width=7).grid(row=1, column=2)
tk.Button(root, text=' C ', command=clear, height=2, width=7, fg='red').grid(row=1, column=3)
tk.Button(root, text=' = ', command=equal, height=2, width=32).grid(row=2, columnspan=4)

root.mainloop()
