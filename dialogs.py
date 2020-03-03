from tkinter import filedialog as FileDialog
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser


def test():
    MessageBox.showinfo("Hola!", "Hola mundo")  # título, mensaje


def alerta():
    MessageBox.showwarning("Alerta",
                           "Sección sólo para administradores.")


def errorshow():
    MessageBox.showerror("Error",
                         "Ha ocurrido un error inesperado.")


def testColor():
    color1 = ColorChooser.askcolor(title="Elige un color")
    color.config(text=str(color1))


def testFile():
    fichero1 = FileDialog.askopenfilename(filetypes=(
        ("Ficheros de texto para escoger!!!", "*.txt"),
        ("Todos los ficheros", "*.*")
    ),
        title="Abre tu documento!!!!!")
    file.config(text=str(fichero1))


def testSave():
    fichero = FileDialog.asksaveasfile(
        title="Guardar un fichero", mode='w', defaultextension=".txt")

    if fichero is not None:
        fichero.write("Hola!")
        fichero.close()


def testAskRetry():
    resultado = MessageBox.askretrycancel("Reintentar",
                                          "No se puede conectar")
    if resultado == True:
        MessageBox.showinfo("Felicidades", "Todo esta bien")
    else:
        MessageBox.showerror("Error",
                             "Ha ocurrido un error inesperado.")


def testAskQuestion():
    resultado = MessageBox.askquestion("Salir", "¿Estás seguro de continuar?")
    if resultado == "yes":
        MessageBox.showinfo("Felicidades", "Saliste del sistema")
    else:
        MessageBox.showerror("Adios :( ",
                             "Saliste del sistema.")


root = Tk()
root.resizable(1, 1)
Button(root, text="Clícame", command=test).pack()
Button(root, text="Alerta", command=alerta).pack()
Button(root, text="Error", command=errorshow).pack()
Button(root, text="Color", command=testColor).pack()
Button(root, text="Open", command=testFile).pack()
Button(root, text="Save", command=testSave).pack()
Button(root, text="Test Ask Retry", command=testAskRetry).pack()
Button(root, text="Test Ask Question", command=testAskQuestion).pack()

imag = PhotoImage()
color = Label(root)
file = Label(root)
color.pack()
file.pack()
Label(root, image=imag).pack(side="left")
root.mainloop()
