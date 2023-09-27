import tkinter as tk
from PIL import ImageTk, Image

def saludar():
    print("Adiós, {}!".format(textbox.get()))

ventana = tk.Tk()
ventana.title("Hola mundo")

textbox = tk.Entry(ventana)
textbox.grid(row=0, column=0)

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.grid(row=1, column=0)

# Importa la imagen
imagen = Image.open('C:/ehzr/14.OPENCV/opencv-course-master/Resources/Photos/cats.jpg')

# Crea un ImageTk a partir de la imagen
imagenTk = ImageTk.PhotoImage(imagen)

# Crea un Label para mostrar la imagen
label = tk.Label(ventana, image=imagenTk)

# Coloca el Label debajo del botón "Saludar"
label.grid(row=2, column=0)

ventana.mainloop()