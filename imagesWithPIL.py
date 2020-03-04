from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Imagenes con Pillow")


def nextPhoto(image_number):
    global my_label
    global button_back
    global button_next
    global index
    my_label.grid_forget()
    my_label = Label(image=my_img_list[image_number-1])
    my_label.grid(row=0, column=0, columnspan=3)
    button_back = Button(
        root, text="<<", command=lambda: previusPhoto(image_number-1))
    button_exit = Button(
        root, text=">>", command=lambda: nextPhoto(image_number+1))
    if image_number == 5:
        button_back = Button(root, text="<<", state=DISABLED)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=1)
    index = index+1
    return


def previusPhoto(image_number):
    global my_label
    global button_back
    global button_next
    global index
    my_label.grid_forget()
    my_label = Label(image=my_img_list[image_number-1])
    my_label.grid(row=0, column=0, columnspan=3)
    button_back = Button(
        root, text="<<", command=lambda: previusPhoto(image_number-1))
    button_exit = Button(
        root, text=">>", command=lambda: nextPhoto(image_number+1))
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=1)
    index = index-1

    return


index = 0
my_img = ImageTk.PhotoImage(Image.open("./screenshots/add.png"))
my_img1 = ImageTk.PhotoImage(Image.open("./screenshots/checkbox.png"))
my_img2 = ImageTk.PhotoImage(Image.open("./screenshots/editor.png"))
my_img3 = ImageTk.PhotoImage(Image.open("./screenshots/entry.png"))
my_img4 = ImageTk.PhotoImage(Image.open("./screenshots/entryLarge.png"))

my_img_list = [my_img, my_img1, my_img2, my_img3, my_img4]


my_label = Label(image=my_img)
# my_label.pack()
my_label.grid(row=0, column=0, columnspan=3)
button_back = Button(root, text="<<", command=lambda: previusPhoto(index))
button_next = Button(root, text="Salir", command=root.quit)
button_exit = Button(root, text=">>", command=lambda: nextPhoto(index))
button_back.grid(row=1, column=0)
button_next.grid(row=1, column=1)
button_exit.grid(row=1, column=2)


root.mainloop()
