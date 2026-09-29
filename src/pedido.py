class Pedido:
    def __init__(self, codigo, cliente, descripcion):
        self._codigo = codigo
        self._cliente = cliente
        self._descripcion = descripcion

    @property
    def codigo(self): return self._codigo

    @property
    def cliente(self): return self._cliente

    @property
    def descripcion(self): return self._descripcion

    def __str__(self):
        return f"{self.codigo} - {self.cliente}: {self.descripcion}"
