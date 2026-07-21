import tkinter as tk

root = tk.Tk()
root.title("Calc")
expression = ""
equation = tk.StringVar()

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    try:
        equation.set(str(eval(expression)))
    except:
        equation.set("Error")

tk.Entry(root, textvariable=equation).grid(columnspan=4)
buttons = [
    '7','8','9','/', '4','5','6','*',
    '1','2','3','-', '0','.','=','+'
]
# ... (Layout logic omitted for brevity, see for full implementation)
tk.Button(root, text='=', command=equal).grid(row=5, columnspan=4)
root.mainloop()
