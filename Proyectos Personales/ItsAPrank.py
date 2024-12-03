import tkinter as tk
window=tk.Tk()
window.title("Prueba de amistad")
window.geometry("920x480")
window.configure(background="light blue")

weight=tk.Label(window, text="Weight", width=10, height=1)
weight.grid(row=0, column=0)
height=tk.Label(window, text="Height", width=10, height=1)
height.grid(row=1, column=0)

window.mainloop()