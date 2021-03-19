from tkinter import *
from tkinter import messagebox

main_w = Tk()

#Config the window app
main_w.geometry('800x500') # Size
main_w.configure(bg = 'white') # Background color
main_w.title('Proyecto | Computer Vision') # Title

def hola():

    #print("Si")
    msg = messagebox.showinfo("Botón", "Button test")
    
#Botones
B = Button(
    
    main_w,
    text = "Tomar foto",
    command = lambda: hola(),
    width= 50,
    justify = CENTER,
    relief = FLAT,
    font = "Arial",

    activebackground = "WHITE",
    activeforeground = "BLACK",

    background = "BLACK",
    foreground = "WHITE",
    
    ).place(x = 170, y = 250)

#Labels

L = Label(
    main_w,
    text = "Clasificador de números con bordes",
    bg = "white",
    pady = 40,
    font = ("Bebas Neue", 30)
)


L.pack()

main_w.mainloop()