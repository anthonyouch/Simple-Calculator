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
myButton1 = Button(root, text="1",padx=28, pady=25, command = lambda: button_click(1))
myButton1.grid(row=3, column=0)
myButton2 = Button(root, text="2",padx=28, pady=25, command = lambda: button_click(2))
myButton2.grid(row=3, column=1)
myButton3 = Button(root, text="3",padx=28, pady=25, command = lambda: button_click(3))
myButton3.grid(row=3, column=2)
myButton4 = Button(root, text="4",padx=28, pady=25, command = lambda: button_click(4))
myButton4.grid(row=2, column=0)
myButton5 = Button(root, text="5",padx=28, pady=25, command = lambda: button_click(5))
myButton5.grid(row=2, column=1)
myButton6 = Button(root, text="6",padx=28, pady=25, command = lambda: button_click(6))
myButton6.grid(row=2, column=2)
myButton7 = Button(root, text="7",padx=28, pady=25, command = lambda: button_click(7))
myButton7.grid(row=1, column=0)
myButton8 = Button(root, text="8",padx=28, pady=25, command = lambda: button_click(8))
myButton8.grid(row=1, column=1)
myButton9 = Button(root, text="9",padx=28, pady=25, command = lambda: button_click(9))
myButton9.grid(row=1, column=2)
myButton9 = Button(root, text="0",padx=28, pady=25, command = lambda: button_click(0))
myButton9.grid(row=4, column=0)

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
