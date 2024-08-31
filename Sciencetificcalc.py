from tkinter import *
import math

def click(value): 
    ex = enteryfield.get()  
    answer =''

    try:

        if value == 'C':
            
            ex = ex[0:len(ex)-1]
            enteryfield.delete(0,END)
            enteryfield.insert(0,ex)

        elif value =="CE":
            enteryfield.delete(0,END)

        elif value=="√":
            answer=math.sqrt(eval(ex))

        elif value =="π":
            answer = math.pi

        elif value =="cosθ":
            answer = math.cos(math.radians(eval(ex)))


        elif value =="sinθ":
            answer = math.sin(math.radians(eval(ex)))

        elif value =="tanθ":
            answer = math.tan(math.radians(eval(ex)))

        elif value =="2π":
            answer = 2*math.pi
        
        elif value =="cosh":
            answer = math.cosh(math.radians(eval(ex)))

        elif value =="tanh":
            answer = math.tanh(math.radians(eval(ex)))
        
        elif value =="sinh":
            answer = math.sinh(math.radians(eval(ex)))
        
        elif value ==chr(8731):
            answer = eval(ex)**(1/3)
        
        elif value == "x\u02b8":
            enteryfield.insert(END,'**')
            return
        
        elif value == "x\u00b3":
            answer=eval(ex)**3

        elif value == "x\u00B2":
            answer=eval(ex)**2

        elif value =="ln":
            answer = math.log2(eval(ex))
        
        elif value =="deg":
            answer = math.degrees(eval(ex))
 
        elif value =="rad":
            answer = math.radians(eval(ex))
        
        elif value =="e":
            answer = math.e
        
        elif value =="log10":
            answer = math.log10(eval(ex))
        
        elif value =="log10":
            answer = math.log10(eval(ex))
        
        elif value == 'x!':
            answer=math.factorial(ex)

        elif value == chr(247):
            enteryfield.insert(END, '/')
            return
        elif value == "=":
            answer = eval(ex)

        else:
            enteryfield.insert(END, value)
            return
        
        enteryfield.delete(0,END)
        enteryfield.insert(0,answer)
        
    except SyntaxError:
        pass

root = Tk()
root.title("scientific calculator")
root.config(bg='dodgerblue3')
root.geometry('680x486+100+100')
enteryfield = Entry(root, font=('arial', 20, 'bold'), bg='dodgerblue3', fg='white', bd=10, relief=SUNKEN, width=30)
enteryfield.grid(row=0, column=0, columnspan=8)

button_text_list = ['C', 'CE', '√', '+', 'π', 'cosθ','tanθ', 'sinθ', 
                    '1', '2', '3', '-', '2π', 'cosh', 'tanh', 'sinh', 
                    '4', '5', '6', '*', chr(8731), 'x\u02b8', 'x\u00b3', 'x\u00B2',
                    '7', '8', '9', chr(247), 'ln', 'deg', 'rad', 'e',
                    '0', '.', '%', '=', 'log10', '(', ')', 'x!']

rowvalue = 1
columnsvalue = 0

for i in button_text_list:

    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='dodgerblue3',fg='white',
                font=('arial', 18, 'bold'), activebackground='dodgerblue3', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnsvalue)
    columnsvalue+=1
    if columnsvalue> 7:
        rowvalue +=1
        columnsvalue=0
root.mainloop()



#+=
