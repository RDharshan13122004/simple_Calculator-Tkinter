#builting basic calculator

from tkinter import * 

root = Tk()

#bachground color to GUI

root.configure(bg='#424141')

#title
title = root.title("simple calculator")

#input field and view

content_box = Entry(root,borderwidth=5,width=45)
content_box.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#functions

def button_click(number):
    current = content_box.get()
    content_box.delete(0,END)
    content_box.insert(0, current + str(number))

def addition():
    first_input = content_box.get()
    global first_number
    global operation 
    operation = "Addition"
    first_number = float(first_input)
    content_box.delete(0,END)

def subraction():
    first_input = content_box.get()
    global first_number
    global operation
    operation = "Subraction"
    first_number = float(first_input)
    content_box.delete(0,END)

def multiplication():
    first_input = content_box.get()
    global first_number
    global operation
    operation = "Multiplication"
    first_number = float(first_input)
    content_box.delete(0,END)

def division():
    first_input = content_box.get()
    global first_number
    global operation
    operation = "Division"
    first_number = float(first_input)
    content_box.delete(0,END)

def equallto():
    second_number = content_box.get()
    content_box.delete(0,END)

    
    if operation == "Addition":
        content_box.insert(0, first_number + float(second_number))

    if operation == "Subraction":
        content_box.insert(0, first_number - float(second_number))
    
    if operation == "Multiplication":
        content_box.insert(0, first_number * float(second_number))
    
    if operation == "Division":
        content_box.insert(0, first_number / float(second_number))


def clear():
    content_box.delete(0,END)


#defining box

button_1 = Button(root,text="1",padx=40,pady=20,background='#2e2e2e',fg='#FFFFFF',command= lambda: button_click(1))
button_2 = Button(root,text="2",padx=40,pady=20,background='#2e2e2e',fg='#FFFFFF',command= lambda: button_click(2))
button_3 = Button(root,text="3",padx=40,pady=20,background='#2e2e2e',fg='#FFFFFF',command= lambda: button_click(3))
button_4 = Button(root,text="4",padx=40,pady=20,background='#2e2e2e',fg='#FFFFFF',command= lambda: button_click(4))
button_5 = Button(root,text="5",padx=40,pady=20,background='#2e2e2e',fg='#FFFFFF',command= lambda: button_click(5))
button_5 = Button(root,text="5",padx=40,pady=20,background='#2e2e2e',fg='#FFFFFF',command= lambda: button_click(5))
button_6 = Button(root,text="6",padx=40,pady=20,background='#2e2e2e',fg='#FFFFFF',command= lambda: button_click(6))
button_7 = Button(root,text="7",padx=40,pady=20,background='#2e2e2e',fg='#FFFFFF',command= lambda: button_click(7))
button_8 = Button(root,text="8",padx=40,pady=20,background='#2e2e2e',fg='#FFFFFF',command= lambda: button_click(8))
button_9 = Button(root,text="9",padx=40,pady=20,background='#2e2e2e',fg='#FFFFFF',command= lambda: button_click(9))
button_0 = Button(root,text="0",padx=40,pady=20,background='#2e2e2e',fg='#FFFFFF',command= lambda: button_click(0))

#operation button

button_addition = Button(root,text="+",padx=40,pady=20,background='#2e2e2e',fg='#FFFFFF',command=addition)
button_subraction = Button(root,text="-",padx=40,pady=20,background='#2e2e2e',fg='#FFFFFF',command=subraction)
button_multiplication = Button(root,text="*",padx=40,pady=20,background='#2e2e2e',fg='#FFFFFF',command=multiplication)
button_division = Button(root,text="/",padx=40,pady=20,background='#2e2e2e',fg='#FFFFFF',command=division)
button_equalto = Button(root,text="=",padx=39,pady=54,background='#2e2e2e',fg='#FFFFFF',command=equallto)
button_clear = Button(root,text="Clear",padx=79,pady=20,command=clear)

#put the button into the screen in grid format

button_9.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_7.grid(row=1,column=2)

button_6.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_4.grid(row=2,column=2)

button_3.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_1.grid(row=3,column=2)

button_addition.grid(row=4,column=0)
button_subraction.grid(row=4,column=1)
button_equalto.grid(row=4,column=2,rowspan=2)

button_multiplication.grid(row=5,column=0)
button_division.grid(row=5,column=1)

button_0.grid(row=6,column=0)
button_clear.grid(row=6,column=1,columnspan=2)

root.mainloop()