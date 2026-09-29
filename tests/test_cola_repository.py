import pytest
from src.cola import Cola
from src.pedido import Pedido
from src.pedido_repository import PedidoRepository

def test_cola_inicia_vacia():
    cola = Cola()
    assert cola.esta_vacia()
    assert cola.cantidad() == 0

def test_agregar_aumenta_cantidad():
    cola = Cola()
    cola.agregar("A")
    cola.agregar("B")
    assert cola.cantidad() == 2

def test_siguiente_muestra_el_primero():
    cola = Cola()
    cola.agregar("A")
    cola.agregar("B")
    assert cola.siguiente() == "A"

def test_cola_respeta_orden_fifo():
    cola = Cola()
    cola.agregar("A")
    cola.agregar("B")
    cola.agregar("C")
    assert cola.eliminar() == "A"
    assert cola.eliminar() == "B"
    assert cola.eliminar() == "C"
    assert cola.esta_vacia()

def test_eliminar_cola_vacia_lanza_error():
    cola = Cola()
    with pytest.raises(IndexError):
        cola.eliminar()

def test_repository_guarda_y_atiente_pedidos():
    repo = PedidoRepository()
    p1 = Pedido("P001", "Ana", "Laptop")
    p2 = Pedido("P002", "Pedro", "Monitor")
    repo.guardar(p1); repo.guardar(p2)
    assert repo.cantidad() == 2
    assert repo.obtener_siguiente() == p1
    assert repo.atender() == p1
    assert repo.obtener_siguiente() == p2
    assert repo.cantidad() == 1
