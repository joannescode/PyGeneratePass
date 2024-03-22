import tkinter as tk

def click():
    label.config(text="Botão clicado!")
root = tk.Tk()
root.title("Tkinter")
label = tk.Label(root, text="Olá Mundo!")
label.pack
button = tk.Button(root, text="Clique Aqui", command=click)

root.mainloop()