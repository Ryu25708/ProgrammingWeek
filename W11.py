import tkinter as tk

def calculate():
    a = float(num1.get())
    b = float(num2.get())
    op = operator.get()

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b

    answer.config(text="Result: " + str(result))

window = tk.Tk()
window.title("Calculator")
window.geometry("300x250")

tk.Label(window, text="First number").pack()
num1 = tk.Entry(window)
num1.pack()

tk.Label(window, text="Operator (+, -, *, /)").pack()
operator = tk.Entry(window)
operator.pack()

tk.Label(window, text="Second number").pack()
num2 = tk.Entry(window)
num2.pack()

tk.Button(window, text="Calculate", command=calculate).pack()

answer = tk.Label(window, text="Result: ")
answer.pack()

window.mainloop()
