from src.cola import Cola

class PedidoRepository:
    """Repository que centraliza la gestión de pedidos."""

    def __init__(self):
        self._cola = Cola()

    def guardar(self, pedido):
        self._cola.agregar(pedido)

    def obtener_siguiente(self):
        return self._cola.siguiente()

    def atender(self):
        return self._cola.eliminar()

    def esta_vacio(self):
        return self._cola.esta_vacia()

    def cantidad(self):
        return self._cola.cantidad()
