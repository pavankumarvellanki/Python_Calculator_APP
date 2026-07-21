import tkinter as tk

class Release2Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator - Release 2")
        self.root.geometry("350x450")
        
        self.expression = ""
        self.equation = tk.StringVar()
        
        # Configure grid weight so window elements resize dynamically
        for i in range(10):
            self.root.rowconfigure(i, weight=1)
        for j in range(4):
            self.root.columnconfigure(j, weight=1)
            
        self.create_widgets()

    def create_widgets(self):
        # Premium feeling display window
        display = tk.Entry(self.root, textvariable=self.equation, font=('Helvetica', 22), 
                           bd=12, relief="flat", justify="right", bg="#f4f4f4")
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, py=10)

        # Button Layout Configuration
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('⌫', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            action = lambda x=text: self.on_button_click(x)
            btn = tk.Button(self.root, text=text, font=('Helvetica', 14), 
                            command=action, relief="groove", borderwidth=1)
            btn.grid(row=row, column=col, sticky="nsew", padx=2, py=2)

        # Dedicated Span Equals Button
        eq_btn = tk.Button(self.root, text='=', font=('Helvetica', 16, 'bold'), 
                           command=self.calculate, bg="#4CAF50", fg="white", relief="flat")
        eq_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=2, py=4)
        self.root.rowconfigure(5, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '⌫':
            self.expression = self.expression[:-1]
        else:
            # Prevent starting calculation with multiple math symbols
            if char in ['+', '-', '*', '/'] and (not self.expression or self.expression[-1] in ['+', '-', '*', '/']):
                return 
            self.expression += str(char)
            
        self.equation.set(self.expression)

    def calculate(self):
        try:
            # Safely evaluate string math expression
            result = str(eval(self.expression))
            self.expression = result
            self.equation.set(result)
        except ZeroDivisionError:
            self.equation.set("Cannot divide by 0")
            self.expression = ""
        except Exception:
            self.equation.set("Syntax Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = Release2Calculator(root)
    root.mainloop()
