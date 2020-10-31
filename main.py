#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from tkinter import *
import tkinter.messagebox as tm

from poem_data import *


my_poem = Tk()
my_poem.title('hello world')
my_poem.geometry('800x500')

def first_poem():
    tm.showinfo('h', data[0])
def sencond_poem():
    tm.showinfo('e', data[1])
def third_poem():    
    tm.showinfo('l', data[2])
def fourth_poem():   
    tm.showinfo('l', data[3])
def fifth_poem():    
    tm.showinfo('o', data[4])
def sixth_poem():    
    tm.showinfo('w', data[5])
def seventh_poem():  
    tm.showinfo('o', data[6])
def eighth_poem():   
    tm.showinfo('r', data[7])
def ninth_poem():    
    tm.showinfo('l', data[8])
def tenth_poem():    
    tm.showinfo('d', data[9])




Button(my_poem, text='h', command=first_poem,   relief=GROOVE,   width=6, bg='FloralWhite', fg='black', font=('YouYuan', 10, 'bold')).grid(row=1, column=1, padx=50, pady=125)
Button(my_poem, text='e', command=sencond_poem, relief=GROOVE, width=6, bg='FloralWhite',   fg='black', font=('YouYuan', 10, 'bold')).grid(row=1, column=2, padx=50, pady=125)
Button(my_poem, text='l', command=third_poem,   relief=GROOVE,   width=6, bg='FloralWhite', fg='black', font=('YouYuan', 10, 'bold')).grid(row=1, column=3, padx=50, pady=125)
Button(my_poem, text='l', command=fourth_poem,  relief=GROOVE,  width=6, bg='FloralWhite',  fg='black', font=('YouYuan', 10, 'bold')).grid(row=1, column=4, padx=50, pady=125)
Button(my_poem, text='o', command=fifth_poem,   relief=GROOVE,   width=6, bg='FloralWhite', fg='black', font=('YouYuan', 10, 'bold')).grid(row=1, column=5, padx=50, pady=125)
Button(my_poem, text='w', command=sixth_poem,   relief=GROOVE,   width=6, bg='FloralWhite', fg='black', font=('YouYuan', 10, 'bold')).grid(row=2, column=1, padx=50, pady=125)
Button(my_poem, text='o', command=seventh_poem, relief=GROOVE, width=6, bg='FloralWhite',   fg='black', font=('YouYuan', 10, 'bold')).grid(row=2, column=2, padx=50, pady=125)
Button(my_poem, text='r', command=eighth_poem,  relief=GROOVE,  width=6, bg='FloralWhite',  fg='black', font=('YouYuan', 10, 'bold')).grid(row=2, column=3, padx=50, pady=125)
Button(my_poem, text='l', command=ninth_poem,   relief=GROOVE,   width=6, bg='FloralWhite', fg='black', font=('YouYuan', 10, 'bold')).grid(row=2, column=4, padx=50, pady=125)
Button(my_poem, text='d', command=tenth_poem,   relief=GROOVE,   width=6, bg='FloralWhite', fg='black', font=('YouYuan', 10, 'bold')).grid(row=2, column=5, padx=50, pady=125)
                                                                         

#hw =['h', 'e', 'l', 'l', 'o'
#     'w', 'o', 'r', 'l', 'd']
#for x in range(1,3):
#    for y in range(1,6):
#        Button(my_poem, text=hw[x,y], command=first_poem , ).grid(row=1, column=1, padx=20, pady=20)
#这里我在想有什么办法将函数放进一个列表里



my_poem.mainloop()
