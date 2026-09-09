import tkinter as tk
from tkinter import messagebox
import re

# Función para validar el formulario
def enviar_formulario():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    password = entry_password.get()

    # Validaciones básicas
    if nombre == "" or correo == "" or password == "":
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    # Validación simple de correo
    patron_correo = r"[^@]+@[^@]+\.[^@]+"
    if not re.match(patron_correo, correo):
        messagebox.showerror("Error", "Correo electrónico no válido")
        return

    if len(password) < 4:
        messagebox.showerror("Error", "La contraseña debe tener al menos 4 caracteres")
        return

    messagebox.showinfo("Éxito", "Formulario enviado correctamente")

    # Limpiar campos
    entry_nombre.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Registro")
ventana.geometry("350x300")
ventana.resizable(False, False)

# Título
titulo = tk.Label(ventana, text="Formulario de Registro", font=("Arial", 14))
titulo.pack(pady=10)

# Nombre
tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.pack(pady=5)

# Correo
tk.Label(ventana, text="Correo").pack()
entry_correo = tk.Entry(ventana, width=30)
entry_correo.pack(pady=5)

# Contraseña
tk.Label(ventana, text="Contraseña").pack()
entry_password = tk.Entry(ventana, width=30, show="*")
entry_password.pack(pady=5)

# Botón enviar
btn_enviar = tk.Button(ventana, text="Enviar", command=enviar_formulario)
btn_enviar.pack(pady=15)

# Ejecutar aplicación
ventana.mainloop()