# Semana 7 - Cola de pedidos con Repository y pruebas unitarias

**Estudiante:** Kevin Robles

## Descripción
Sistema sencillo para administrar pedidos pendientes. Se utiliza una **cola FIFO**:
el primer pedido que llega es el primero en ser atendido.

La cola fue implementada manualmente, sin `queue.Queue` ni `collections.deque`.

## Estructura
- `src/pedido.py`: clase Pedido.
- `src/cola.py`: implementación manual de la cola.
- `src/pedido_repository.py`: Repository.
- `main.py`: ejemplo de funcionamiento.
- `tests/test_cola_repository.py`: pruebas con pytest.

## Operaciones
Agregar, eliminar/atender, consultar siguiente, comprobar si está vacía y consultar cantidad.

## Repository
`PedidoRepository` separa la gestión de los pedidos de la lógica principal.

## Instalación
```bash
pip install pytest
```

## Ejecutar
```bash
python main.py
```

## Pruebas
```bash
pytest -v
```

## GitHub
https://github.com/kevnhy/Robles_Kevin_Semana7
