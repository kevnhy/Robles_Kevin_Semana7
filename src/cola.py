class Cola:
    """Cola FIFO manual, sin queue.Queue ni collections.deque."""

    def __init__(self):
        self._elementos = []
        self._frente = 0

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def eliminar(self):
        if self.esta_vacia():
            raise IndexError("No se puede eliminar: la cola está vacía.")
        elemento = self._elementos[self._frente]
        self._frente += 1
        return elemento

    def siguiente(self):
        if self.esta_vacia():
            raise IndexError("No hay elementos en la cola.")
        return self._elementos[self._frente]

    def esta_vacia(self):
        return self._frente >= len(self._elementos)

    def cantidad(self):
        return len(self._elementos) - self._frente

    def obtener_todos(self):
        return self._elementos[self._frente:]
