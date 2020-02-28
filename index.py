from tkinter import *


def hola():
    print("Hola mundo!")


# Configuración de la raíz
root = Tk()
root.title("Primer Programa con Tkinter")
root.resizable(0, 0)
label = Label(root, text="Nombre de usuario")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right", state="normal")

label2 = Label(root, text="Contraseña")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="center", show="*")

label3 = Label(root, text="Ingresa un párrafo")
label.grid(row=4, column=0, padx=16, pady=16)
texto = Text(root)
texto.grid(row=5, column=0, padx=16, pady=16)
texto.config(width=30, height=10, font=("Consolas", 12),
             padx=15, pady=15, selectbackground="red")


# Finalmente bucle de la aplicación
root.mainloop()
