from tkinter import *
import math as m
window = Tk()
window.title()
window.geometry("383x570+70+40")
window.config(bg ="gray11")
window.resizable(False, False)

def close():
    window.destroy()

def clear():
    entry.delete(0, "end")


def back():
    last_number = len(entry.get())-1
    entry.delete(last_number)

def press(input):
    length = len(entry.get())
    entry.insert(length, input)

def add(a,b):
    return float(a) + float(b)
def subtract (a,b):
    return float(a) - float(b)
def multiply(a,b):
    return float(a) * float(b)
def devide  (a,b):
    return float(a) / float(b)

    def expression_break(sign, expression):
        values = expression.split(sign,1)
        return values

    def scientific(expression):
        data = expression_break("(", expression)
        if data[0] =="tan":
            result = m.tan(float(data[1]))
        elif data[0] =="cos":
            result = m.cos(float(data[1]))
        elif data[0] =="sin":
            result = m.sin(float(data[1]))
        elif data[0] =="sqrt":
            result = m.sqrt(float(data[1]))
        elif data[0] =="log":
            result = m.log10(float(data[1]))
        elif data[0] =="ln":
            result = m.log(float(data[1]))
        elif data[0] =="deg":
            result = m.degrees(float(data[1]))
        elif data[0] =="rad":
            result = m.radians(float(data[1]))
        elif data[0] =="fac":
            result = m.factorial(float(data[1]))  
            return result

    
def equal():
    expression = entry.get()
    clear()
    try:

        if expression.find("(") > 0:
            result = scientific(expression)  

        elif expression.find("pow") > 0:
            data = expression_break("pow", expression)
            result = m.pow(float(data[0]), float(data[1]))

        elif expression.find("rem") >0:
            data = expression_break("rem", expression)
            result = m.remainder(float(data[0]), float(data[1]))

        elif expression.find("x") >0:
            data = expression_break("x", expression)
            result = m.multiply(data[0], data[1])

        elif expression.find("/") >0:
            data = expression_break("/", expression)
            result = m.divide(data[0], data[1])

        elif expression.find("+") >0:
            first = expression.find("+")
            second = expression.find("+", first+1, first+5 )
            if first > second:
                data = expression_break("+", expression)
                result = m.add(data[0], data[1])
            else:
                result = add(expression[0,second], expression[second+1:])
        elif expression.rindex("-") > 0:
            sign = expression.rindex("-")
            result = subtract(expression[0, sign], expression[sign + 1:])
        entry.insert(0, result)
    except:
        entry.insert(0, "error")


entry_string = StringVar()
entry = Entry(window, textvariable = entry_string, foreground="white", background="gray20",
              border=0, font=("bahnschrift semiBold", 26))
entry.grid(columnspan=4, ipady=15)
font_value = ("calibari", 18)
btn_tan = Button(window, text="tan", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID, 
                 command= lambda: press("tan("))
btn_tan.grid(row =1, column=0, sticky=E+W, ipady = 5)

btn_cos = Button(window, text="cos", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                 command= lambda: press("cos("))
btn_cos.grid(row =1, column=1, sticky=E+W, ipady = 5)

btn_sin = Button(window, text="sin", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                 command= lambda: press("sin("))
btn_sin.grid(row =1, column=2, sticky=E+W, ipady = 5)

btn_sqrt = Button(window, text="sqrt", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                 command= lambda: press("sqrt("))
btn_sqrt.grid(row =1, column=3, sticky=E+W, ipady = 5)


btn_log = Button(window, text="log", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                 command= lambda: press("log("))
btn_log.grid(row =2, column=0, sticky=E+W, ipady = 5)

btn_ln = Button(window, text="ln", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID)
btn_ln.grid(row =2, column=1, sticky=E+W, ipady = 5)

btn_deg = Button(window, text="deg", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID)
btn_deg.grid(row =2, column=2, sticky=E+W, ipady = 5)

btn_rad = Button(window, text="rad", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                 command= lambda: press("rad("))
btn_rad.grid(row =2, column=3, sticky=E+W, ipady = 5)


btn_fac = Button(window, text="fec", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                 command= lambda: press("fac"))
btn_fac.grid(row =3, column=0, sticky=E+W, ipady = 5)

btn_pow = Button(window, text="pow", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                 command= lambda: press("pow"))
btn_pow.grid(row =3, column=1, sticky=E+W, ipady = 5)

btn_rem = Button(window, text="rem", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                 command= lambda: press("rem"))
btn_rem.grid(row =3, column=2, sticky=E+W, ipady = 5)

btn_pai = Button(window, text="π", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                 command= lambda: press(3.141592))
btn_pai.grid(row =3, column=3, sticky=E+W, ipady = 5)



btn_clear = Button(window, text="C", background="gray5", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID, command=clear)
btn_clear.grid(row =4, columnspan=2, column=0, sticky=E+W, ipady = 5)

btn_backspace = Button(window, text="<", background="gray5", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID, command=back)
btn_backspace.grid(row =4, columnspan=2, column=2, sticky=E+W, ipady = 5)



btn_seven= Button(window, text="7", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                  command= lambda: press(7))
btn_seven.grid(row =5, column=0, sticky=E+W, ipady = 5)

btn_eight= Button(window, text="8", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID, 
                  command= lambda: press(7))
btn_eight.grid(row =5, column=1, sticky=E+W, ipady = 5)

btn_nine= Button(window, text="9", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                 command= lambda: press(9))
btn_nine.grid(row =5, column=2, sticky=E+W, ipady = 5)

btn_divide = Button(window, text="/", background="gray5", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                    command= lambda: press("/"))
btn_divide.grid(row =5, column=3, sticky=E+W, ipady = 5)



btn_sex= Button(window, text="6", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                command= lambda: press("6"))
btn_sex.grid(row =6, column=0, sticky=E+W, ipady = 5)

btn_five= Button(window, text="5", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID, 
                 command= lambda: press("5"))
btn_five.grid(row =6, column=1, sticky=E+W, ipady = 5)

btn_four= Button(window, text="4", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                 command= lambda: press("4"))
btn_four.grid(row =6, column=2, sticky=E+W, ipady = 5)

btn_mul = Button(window, text="*", background="gray5", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                 command= lambda: press("*"))
btn_mul.grid(row =6, column=3, sticky=E+W, ipady = 5)




btn_three= Button(window, text="3", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID, 
                  command= lambda: press("3"))
btn_three.grid(row =7, column=0, sticky=E+W, ipady = 5)

btn_two= Button(window, text="2", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                command= lambda: press("2"))
btn_two.grid(row =7, column=1, sticky=E+W, ipady = 5)

btn_one= Button(window, text="1", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                command= lambda: press("1"))
btn_one.grid(row =7, column=2, sticky=E+W, ipady = 5)

btn_plus = Button(window, text="+", background="gray5", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                   command= lambda: press("+"))
btn_plus.grid(row =7, column=3, sticky=E+W, ipady = 5)



btn_dot= Button(window, text=".", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                command= lambda: press("."))
btn_dot.grid(row =8, column=0, sticky=E+W, ipady = 5)

btn_zero= Button(window, text="0", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                 command= lambda: press("0"))
btn_zero.grid(row =8, column=1, sticky=E+W, ipady = 5)

btn_exponancial= Button(window, text="e", background="gray11", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                        command= lambda: press("2.71823"))
btn_exponancial.grid(row =8, column=2, sticky=E+W, ipady = 5)

btn_minus = Button(window, text="-", background="gray5", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID,
                   command= lambda: press("-"))
btn_minus.grid(row =8, column=3, sticky=E+W, ipady = 5)




btn_equal= Button(window, text="=", background="DarkOrange1", foreground="white", font= font_value, borderwidth=1, relief=SOLID,
                  command = equal)
btn_equal.grid(row =9, columnspan=3, column=0, sticky=E+W, ipady = 5)

btn_close = Button(window, text="close", background="gray5", foreground="DarkOrange1", font= font_value, borderwidth=1, relief=SOLID, 
                   command= close)
btn_close.grid(row =9, column=3, sticky=E+W, ipady = 5)
mainloop()