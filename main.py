import tkinter
from tkinter import ttk

window = tkinter.Tk()

lista = ['Opcion1', 'Opcion2', 'Opcion3', 'Opcion4']
lista_it = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, listvariable=lista_it, height=10)

listbox.grid(column=0, row=1, sticky=tkinter.W)

label = ttk.Label(text='Hola', )
label.grid(column=0, row=2)

window.mainloop()
