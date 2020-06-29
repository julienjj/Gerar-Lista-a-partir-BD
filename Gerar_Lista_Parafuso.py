import os, re, shutil
import tkinter as tk
from tkinter import ttk
from tkinter import *
root = tk.Tk()
root.geometry("200x200")
root.title("Gerar Lista")

with open ('P:/Julien/Prog5 - Parafusos/bitola.txt',"r") as file1:
    bitola=[]
    bitola=file1.readlines()
file1.close()

with open ('P:/Julien/Prog5 - Parafusos/comprimento.txt',"r") as file2:
    comp=[]
    comp=file2.readlines()
file2.close()


with open ('P:/Julien/Prog5 - Parafusos/qualidade.txt',"r") as file3:
    qual=[]
    qual=file3.readlines()
file3.close()





ttk.Label(root, text='Parafusos', font="25")

n=tk.StringVar()

def add_par():
    f = open("c:/parafusos.xsr", "a+")


    f.write("          ")
    bit=combo.get()
    bit1=bit.split(";")
    bit2=bit1[0]
    f.write(bit2)
    f.write("	 ")
    qu=combo3.get()
    qu1=qu.split(";")
    qu2=qu1[0]
    f.write(qu2)
    f.write("                           ")

    com=combo2.get()
    com1=com.split(";")
    com2=com1[0]
    f.write(com2)
    f.write("	          ")
    f.write(quantidade.get())
    
    f.write("\n")
    
    f.close()

bt = ttk.Button(root, text = '+Add',command=add_par)

bt.pack(side='bottom')
texto1=ttk.Label(root,text='Bitola')
texto1.pack(side='top')
combo = ttk.Combobox(root,width=27)

combo2 = ttk.Combobox(root,width=27)
combo.pack(side='top')
bt.pack(side='bottom')
texto2=ttk.Label(root,text='Comprimento')
texto2.pack(side='top')
combo2.pack(side='top')

combo3 = ttk.Combobox(root,width=27)
texto3=ttk.Label(root,text='Qualidade')
texto3.pack(side='top')
combo3.pack(side='top')


combo['values']=(bitola)


combo.current()

combo2['values']=(comp)


combo2.current()

combo3['values']=(qual)


combo3.current()

texto4=ttk.Label(root,text='Quantidade')
texto4.pack(side='top')
quantidade = ttk.Entry(root)
quantidade.pack(side='top')

root.mainloop()

