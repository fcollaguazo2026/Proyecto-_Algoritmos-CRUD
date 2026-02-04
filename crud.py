import tkinter as tk
from tkinter import messagebox #ventanas emergentes
import random

tuplita = ([], [], [], [], [], [], [])
mostrarLista = list(tuplita)

usuarios = ([], []) 
listaUsuarios = list(usuarios)

def registrar():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()
    direccion = entry_direccion.get()
    opcion = paquete_var.get()

    if nombre == "" or apellido == "" or telefono == "" or direccion == "":
        messagebox.showerror("Error", "Completa todos los campos")
        return

    if telefono.isdigit() == False:
        messagebox.showerror("Error", "Teléfono solo debe tener números")
        return

    mostrarLista[0].append(nombre)
    mostrarLista[1].append(apellido)
    mostrarLista[2].append(int(telefono))
    mostrarLista[3].append(direccion)

    if opcion == "PC + Monitor":
        precio = 500
    elif opcion == "PC + Monitor 4K":
        precio = 2000
    elif opcion == "Laptop Pro IA":
        precio = 1500
    else:
        precio = 3000

    mostrarLista[4].append(precio)
    mostrarLista[5].append(precio * 1.15)
    mostrarLista[6].append(random.randint(1, 1000))

    messagebox.showinfo("Registro", "Registro guardado con éxito")

    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)

def mostrar_pedidos():
    if len(mostrarLista[0]) == 0:
        messagebox.showinfo("Pedidos", "No existen pedidos registrados")
        return

    texto = ""

    for i in range(len(mostrarLista[0])):
        texto += f"""
Pedido #{i + 1}
Índice: {i}   (usa este número para actualizar/eliminar)
Código: {mostrarLista[6][i]}
Nombre: {mostrarLista[0][i]} {mostrarLista[1][i]}
Teléfono: {mostrarLista[2][i]}
Dirección: {mostrarLista[3][i]}
Total sin IVA: ${mostrarLista[4][i]}
Total con IVA: ${mostrarLista[5][i]:.2f}
Paquete: {paquete_var.get() if False else ""}
------------------------------
"""

    messagebox.showinfo("Lista de pedidos", texto)

def actualizar_pedido():
    if len(mostrarLista[0]) == 0:
        messagebox.showinfo("Actualizar", "No existen pedidos registrados")
        return


    indice = entry_indice.get()

    if indice == "":
        messagebox.showerror("Error", "Ingresa el índice del pedido")
        return

    if indice.isdigit() == False:
        messagebox.showerror("Error", "El índice debe ser un número")
        return

    indice = int(indice)

    if indice < 0 or indice >= len(mostrarLista[0]):
        messagebox.showerror("Error", "Índice fuera de rango")
        return

    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()
    direccion = entry_direccion.get()
    opcion = paquete_var.get()

    if nombre == "" or apellido == "" or telefono == "" or direccion == "":
        messagebox.showerror("Error", "Completa todos los campos para actualizar")
        return

    if telefono.isdigit() == False:
        messagebox.showerror("Error", "Teléfono solo debe tener números")
        return

    mostrarLista[0][indice] = nombre
    mostrarLista[1][indice] = apellido
    mostrarLista[2][indice] = int(telefono)
    mostrarLista[3][indice] = direccion

    if opcion == "PC + Monitor":
        precio = 500
    elif opcion == "PC + Monitor 4K":
        precio = 2000
    elif opcion == "Laptop Pro IA":
        precio = 1500
    else:
        precio = 3000

    mostrarLista[4][indice] = precio
    mostrarLista[5][indice] = precio * 1.15

    messagebox.showinfo("Actualizar", "Pedido actualizado con éxito")

    entry_indice.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)

def eliminar_pedido():
    if len(mostrarLista[0]) == 0:
        messagebox.showinfo("Eliminar", "No existen pedidos registrados")
        return

    indice = entry_indice.get()

    if indice == "":
        messagebox.showerror("Error", "Ingresa el índice del pedido")
        return

    if indice.isdigit() == False:
        messagebox.showerror("Error", "El índice debe ser un número")
        return

    indice = int(indice)

    if indice < 0 or indice >= len(mostrarLista[0]):
        messagebox.showerror("Error", "Índice fuera de rango")
        return

    if messagebox.askyesno("Confirmar", f"¿Eliminar el pedido con índice {indice}?") == False:
        return

    mostrarLista[0].pop(indice)
    mostrarLista[1].pop(indice)
    mostrarLista[2].pop(indice)
    mostrarLista[3].pop(indice)
    mostrarLista[4].pop(indice)
    mostrarLista[5].pop(indice)
    mostrarLista[6].pop(indice)

    messagebox.showinfo("Eliminar", "Pedido eliminado con éxito")
    entry_indice.delete(0, tk.END)

def registrar_usuario():
    user = entry_user.get()
    password = entry_pass.get()

    if user == "" or password == "":
        messagebox.showerror("Error", "Completa usuario y contraseña")
        return

    if user in listaUsuarios[0]:
        messagebox.showerror("Error", "Ese usuario ya existe")
        return

    listaUsuarios[0].append(user)
    listaUsuarios[1].append(password)

    messagebox.showinfo("Usuario", "Usuario registrado con éxito")

    entry_user.delete(0, tk.END)
    entry_pass.delete(0, tk.END)

def iniciar_sesion():
    user = entry_user.get()
    password = entry_pass.get()

    if user == "" or password == "":
        messagebox.showerror("Error", "Completa usuario y contraseña")
        return

    if user in listaUsuarios[0]:
        pos = listaUsuarios[0].index(user)
        if listaUsuarios[1][pos] == password:
            messagebox.showinfo("Login", "Inicio de sesión correcto")
            frame_login.pack_forget()
            frame_crud.pack()
            return

    messagebox.showerror("Login", "Usuario o contraseña incorrectos")

def cerrar_sesion():
    frame_crud.pack_forget()
    frame_login.pack()
    entry_user.delete(0, tk.END)
    entry_pass.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Caja Registradora - CRUD + Login")
ventana.geometry("420x520")

frame_login = tk.Frame(ventana)
frame_login.pack()

tk.Label(frame_login, text="LOGIN / REGISTRO", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(frame_login, text="Usuario").pack()
entry_user = tk.Entry(frame_login)
entry_user.pack()

tk.Label(frame_login, text="Contraseña").pack()
entry_pass = tk.Entry(frame_login, show="*")
entry_pass.pack()

tk.Button(frame_login, text="Registrar Usuario", command=registrar_usuario, bg="blue", fg="white").pack(pady=8)
tk.Button(frame_login, text="Iniciar Sesión", command=iniciar_sesion, bg="green", fg="white").pack(pady=8)

frame_crud = tk.Frame(ventana)

tk.Label(frame_crud, text="CAJA REGISTRADORA", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(frame_crud, text="Nombre").pack()
entry_nombre = tk.Entry(frame_crud)
entry_nombre.pack()

tk.Label(frame_crud, text="Apellido").pack()
entry_apellido = tk.Entry(frame_crud)
entry_apellido.pack()

tk.Label(frame_crud, text="Teléfono").pack()
entry_telefono = tk.Entry(frame_crud)
entry_telefono.pack()

tk.Label(frame_crud, text="Dirección").pack()
entry_direccion = tk.Entry(frame_crud)
entry_direccion.pack()

tk.Label(frame_crud, text="Paquete").pack()

paquete_var = tk.StringVar()
paquete_var.set("PC + Monitor")

opciones = [
    "PC + Monitor",
    "PC + Monitor 4K",
    "Laptop Pro IA",
    "Servidor Potente"
]

tk.OptionMenu(frame_crud, paquete_var, *opciones).pack()

tk.Button(
    frame_crud,
    text="Registrar",
    command=registrar,
    bg="green",
    fg="white"
).pack(pady=8)

tk.Button(
    frame_crud,
    text="Mostrar pedidos",
    command=mostrar_pedidos,
    bg="blue",
    fg="white"
).pack(pady=8)

tk.Label(frame_crud, text="Índice del pedido (para actualizar/eliminar)").pack(pady=(10, 0))
entry_indice = tk.Entry(frame_crud)
entry_indice.pack()

tk.Button(
    frame_crud,
    text="Actualizar pedido",
    command=actualizar_pedido,
    bg="orange",
    fg="white"
).pack(pady=8)

tk.Button(
    frame_crud,
    text="Eliminar pedido",
    command=eliminar_pedido,
    bg="red",
    fg="white"
).pack(pady=8)

tk.Button(
    frame_crud,
    text="Cerrar sesión",
    command=cerrar_sesion,
    bg="gray",
    fg="white"
).pack(pady=10)

ventana.mainloop()
