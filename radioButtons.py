from tkinter import *


def seleccionar():
    monitor.config(text="{}".format(opcion.get()))


def reset():
    opcion.set(None)
    leche.set(None)
    azucar.set(None)
    monitor.config(text="")


# Configuración de la raíz
root = Tk()

opcion = IntVar()
root.title("Radio Buttons")
root.geometry("360x480")
Radiobutton(root, text="Opción 1", variable=opcion,
            value=1, command=seleccionar).pack()
Radiobutton(root, text="Opción 2", variable=opcion,
            value=2, command=seleccionar).pack()
Radiobutton(root, text="Opción 3", variable=opcion,
            value=3, command=seleccionar).pack()

monitor = Label(root, )
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()
leche = IntVar()      # 1 si, 0 no
azucar = IntVar()    # 1 si, 0 no

Label(root, text="¿Cómo quieres el café?").pack()
Checkbutton(root, text="Con leche", variable=leche,
            onvalue=1, offvalue=0).pack()
Checkbutton(root, text="Con azúcar", variable=leche,
            onvalue=1, offvalue=0).pack()

# Finalmente bucle de la aplicación
root.mainloop()
