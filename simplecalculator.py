from tkinter import *
root = Tk()
root.title("Simple Calculator")
e = Entry(root, width=45, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, pady = 10, padx = 10)

f_num = None
current_sign = None
def button_click(num):
    e.insert(END, str(num))

def button_addition():
    global f_num
    global current_sign
    current_sign = "+"
    f_num = float(e.get())
    e.delete(0, END)

def button_substraction():
    global f_num
    global current_sign
    current_sign = "-"
    f_num = float(e.get())
    e.delete(0, END)

def button_multiplication():
    global f_num
    global current_sign
    current_sign = "*"
    f_num = float(e.get())
    e.delete(0, END)

def button_division():
    global f_num
    global current_sign
    current_sign = "/"
    f_num = float(e.get())
    e.delete(0, END)

def button_clear():
    global f_num
    f_num = None
    e.delete(0,END)

def button_equal():
    global f_num
    global current_sign
    second_number = e.get()
    e.delete(0, END)
    if current_sign == "+":
        e.insert(0, f_num + float(second_number))
    if current_sign == "-":
        e.insert(0, f_num - float(second_number))
    if current_sign == "*":
        e.insert(0, f_num * float(second_number))
    if current_sign == "/":
        e.insert(0, f_num / float(second_number))

# displaying all number buttons

val = 1
for i in range(3,0,-1):
    for j in range(3):
        button = Button(root, text = val, padx = 28, pady = 25, command = lambda x = val: button_click(x))
        button.grid(row=i, column = j)
        val += 1

button0 = Button(root, text="0",padx=28, pady=25, command = lambda: button_click(0))
button0.grid(row=4, column=0)

#adding all symbol buttons

additionButton = Button(root, text="+", padx=27, pady=25, command = lambda: button_addition())
additionButton.grid(row=4,column=2)

substractionButton = Button(root, text="−", padx=27, pady=25, command = lambda: button_substraction())
substractionButton.grid(row=4,column=1)

multiplicationButton = Button(root, text="×", padx=27, pady=25, command = lambda: button_multiplication())
multiplicationButton.grid(row=3,column=3)

divisionButton = Button(root, text="÷", padx=27, pady=25, command = lambda: button_division())
divisionButton.grid(row=2,column=3)

clearButton = Button(root, text="Clear", padx=17, pady=25, command = button_clear)
clearButton.grid(row=1, column=3)

equalButton = Button(root, text="=", padx=27, pady=25, command = button_equal)
equalButton.grid(row=4, column=3)

root.mainloop()
