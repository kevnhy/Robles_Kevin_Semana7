from src.pedido import Pedido
from src.pedido_repository import PedidoRepository

def main():
    repositorio = PedidoRepository()
    repositorio.guardar(Pedido("P001", "Carlos", "Teclado"))
    repositorio.guardar(Pedido("P002", "María", "Mouse"))
    repositorio.guardar(Pedido("P003", "Luis", "Audífonos"))

    print("=== SISTEMA DE PEDIDOS ===")
    print(f"Pedidos en espera: {repositorio.cantidad()}")
    print(f"Siguiente pedido: {repositorio.obtener_siguiente()}")

    atendido = repositorio.atender()
    print(f"Pedido atendido: {atendido}")
    print(f"Siguiente pedido: {repositorio.obtener_siguiente()}")
    print(f"Pedidos restantes: {repositorio.cantidad()}")

if __name__ == "__main__":
    main()
