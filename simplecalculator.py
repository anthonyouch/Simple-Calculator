from tkinter import *
root = Tk()
root.title("Simple Calculator")
root.configure(background='light blue')
equationline = StringVar()
e = Entry(root, width=20, borderwidth=5, textvariable = equationline, font = ("Arial", 20))
e.grid(row=0, column=0, columnspan=4, pady = 10, padx = 10, ipady = 15, ipadx = 40)

equation = ''

def button_click(char):
    global equation
    if len(equation) == 0 and char not in range(0,10):
        equationline.set("please enter a number first",)

    elif char == "=":
        try:
            ans = eval(equation)
            equationline.set(ans)
            equation = str(ans)
        except ZeroDivisionError:
            equationline.set("Divided by Zero!")
            equation = ''
        except:
            equationline.set("invalid equation")
            equation = ''

    elif char == "c":
        equationline.set('')
        equation = ''

    else:
        dic = {'−': '-', '×':'*', '÷': '/'}
        if char in dic:
            equation += (str(dic[char]))
        else:
            equation += (str(char))
        equationline.set(equation)

values = [[7,8,9,'+'], [4,5,6,'−'], [1,2,3,'×'], ['c', '0', '=', '÷']]

for i in range(len(values)):
    for j in range(4):
        char =  values[i][j]
        button = Button(root, text = char , font = ("Arial", 20), command = lambda x = char: button_click(x))
        button.grid(row = i+1, column = j, ipadx = 30, ipady = 20, padx=2,pady=2)

root.mainloop()