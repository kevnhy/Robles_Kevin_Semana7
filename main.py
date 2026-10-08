import tkinter as tk
from tkinter import ttk, messagebox
from src.pedido import Pedido
from src.pedido_repository import PedidoRepository

class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Pedidos - Cola FIFO")
        self.ventana.geometry("720x500")
        self.repositorio = PedidoRepository()
        self.crear_interfaz()
        self.actualizar_lista()

    def crear_interfaz(self):
        titulo = ttk.Label(self.ventana, text="SISTEMA DE PEDIDOS", font=("Arial", 18, "bold"))
        titulo.pack(pady=15)

        formulario = ttk.Frame(self.ventana)
        formulario.pack(pady=5)

        ttk.Label(formulario, text="Código:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(formulario, text="Cliente:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(formulario, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)

        self.codigo = ttk.Entry(formulario, width=35)
        self.cliente = ttk.Entry(formulario, width=35)
        self.descripcion = ttk.Entry(formulario, width=35)
        self.codigo.grid(row=0, column=1)
        self.cliente.grid(row=1, column=1)
        self.descripcion.grid(row=2, column=1)

        botones = ttk.Frame(self.ventana)
        botones.pack(pady=10)
        ttk.Button(botones, text="Agregar pedido", command=self.agregar_pedido).grid(row=0, column=0, padx=5)
        ttk.Button(botones, text="Atender primero", command=self.atender_pedido).grid(row=0, column=1, padx=5)
        ttk.Button(botones, text="Actualizar", command=self.actualizar_lista).grid(row=0, column=2, padx=5)

        self.tabla = ttk.Treeview(self.ventana, columns=("codigo", "cliente", "descripcion"), show="headings", height=10)
        self.tabla.heading("codigo", text="Código")
        self.tabla.heading("cliente", text="Cliente")
        self.tabla.heading("descripcion", text="Descripción")
        self.tabla.column("codigo", width=100)
        self.tabla.column("cliente", width=160)
        self.tabla.column("descripcion", width=350)
        self.tabla.pack(padx=15, pady=10, fill="both", expand=True)

        self.estado = ttk.Label(self.ventana, text="")
        self.estado.pack(pady=5)

    def agregar_pedido(self):
        codigo = self.codigo.get().strip()
        cliente = self.cliente.get().strip()
        descripcion = self.descripcion.get().strip()

        if not codigo or not cliente or not descripcion:
            messagebox.showwarning("Datos incompletos", "Complete todos los campos.")
            return

        self.repositorio.guardar(Pedido(codigo, cliente, descripcion))
        self.codigo.delete(0, tk.END)
        self.cliente.delete(0, tk.END)
        self.descripcion.delete(0, tk.END)
        self.actualizar_lista()
        messagebox.showinfo("Correcto", "Pedido agregado y guardado.")

    def atender_pedido(self):
        if self.repositorio.esta_vacio():
            messagebox.showwarning("Cola vacía", "No hay pedidos para atender.")
            return

        pedido = self.repositorio.atender()
        self.actualizar_lista()
        messagebox.showinfo("Pedido atendido", f"Se atendió: {pedido}")

    def actualizar_lista(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for pedido in self.repositorio.obtener_todos():
            self.tabla.insert("", tk.END, values=(pedido.codigo, pedido.cliente, pedido.descripcion))

        self.estado.config(text=f"Pedidos pendientes: {self.repositorio.cantidad()}")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Aplicacion(ventana)
    ventana.mainloop()
