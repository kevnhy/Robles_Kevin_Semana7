import json
from pathlib import Path
from src.cola import Cola
from src.pedido import Pedido

class PedidoRepository:
    """Centraliza la gestión y persistencia de los pedidos."""

    def __init__(self, archivo="pedidos.json"):
        self._cola = Cola()
        self._archivo = Path(archivo)
        self.cargar()

    def guardar(self, pedido):
        self._cola.agregar(pedido)
        self._persistir()

    def obtener_siguiente(self):
        return self._cola.siguiente()

    def atender(self):
        pedido = self._cola.eliminar()
        self._persistir()
        return pedido

    def esta_vacio(self):
        return self._cola.esta_vacia()

    def cantidad(self):
        return self._cola.cantidad()

    def obtener_todos(self):
        return self._cola.obtener_todos()

    def _persistir(self):
        datos = [pedido.to_dict() for pedido in self._cola.obtener_todos()]
        with open(self._archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def cargar(self):
        if not self._archivo.exists():
            return
        try:
            with open(self._archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            for dato in datos:
                self._cola.agregar(Pedido.from_dict(dato))
        except (json.JSONDecodeError, KeyError):
            self._cola = Cola()
