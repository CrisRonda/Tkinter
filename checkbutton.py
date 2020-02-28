from tkinter import *


def seleccionar():
    cadena = ""
    if (leche.get()):
        cadena += "Con leche"
    else:
        cadena += "Sin leche"

    if (azucar.get()):
        cadena += " y con azúcar"
    else:
        cadena += " y sin azúcar"

    monitor.config(text=cadena)


# Configuración de la raíz
root = Tk()
root.title("Cafetería")
root.config(bd=15)
menubar = Menu(root)
root.config(menu=menubar)

# Submenus sin elementos sin defecto
filemenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar, tearoff=0)
helpmenu = Menu(menubar, tearoff=0)

# Añadir submenus
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

# Opciones del submenu filemenu o Archivo
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

# Opciones en Editar
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

# Opciones en Ayuda
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

leche = IntVar()    # 1 si, 0 no
azucar = IntVar()   # 1 si, 0 no
imag = PhotoImage(file='/home/cristian/Documentos/Python/Interfaces/image.gif')
# Canvas con Imagen Descomentar y comentar el Label
# canvas = Canvas(width=300, height=200, bg='yellow')
# pack the canvas into a frame/form
# canvas.pack(expand=YES, fill=BOTH)
# canvas.create_image(50, 10, image=imag, anchor=NW)

Label(root, image=imag).pack(side="left")

frame = Frame(root)
frame.pack(side="left", )

Label(frame, text="¿Cómo quieres el café?").pack(anchor="w")
Checkbutton(frame, text="Con leche", variable=leche, onvalue=1,
            offvalue=0, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="Con azúcar", variable=azucar, onvalue=1,
            offvalue=0, command=seleccionar).pack(anchor="w")

monitor = Label(frame)
monitor.pack()

# Finalmente bucle de la aplicación
root.mainloop()
