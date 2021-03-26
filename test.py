from tkinter import *

root = Tk()
root.geometry("300x300")

b1 = None
b2 = None
b3 = None

def pro():
    global lt_b

    for i in range(len(lt_b)):
        lt_b[i]['state']='disabled'

lt_b=[b1,b2,b3]
lt_txt=['b1','b2','b3']

for i in range(len(lt_b)):
    lt_b[i] = Button(root, text = lt_txt[i])
    lt_b[i].grid(row=0, column=i)

Button(root, text = 'press me', command=pro).grid(row=1, column=0)

root.mainloop()