# Sistema de Pedidos - Cola FIFO

**Estudiante:** Kevin Robles  
**Lenguaje:** Python

## Descripción

Este proyecto es un sistema sencillo para administrar pedidos pendientes utilizando una **cola FIFO**, donde el primer pedido que llega es el primero que se atiende.

El proyecto continúa el desarrollo realizado durante las semanas 5, 6 y 7 e incorpora programación orientada a objetos, una estructura de datos tipo cola, el patrón Repository, pruebas unitarias, persistencia de datos e interfaz gráfica.

## Objetivo

Desarrollar una aplicación que permita registrar, consultar y atender pedidos de manera ordenada, manteniendo la información guardada aunque el programa se cierre.

## Principales funcionalidades

- Registrar pedidos con código, cliente y descripción.
- Mantener los pedidos en una cola FIFO.
- Consultar la cantidad de pedidos pendientes.
- Atender el primer pedido de la cola.
- Guardar los pedidos en un archivo JSON.
- Recuperar automáticamente los pedidos al iniciar el programa.
- Interfaz gráfica desarrollada con Tkinter.
- Pruebas unitarias con pytest.

## Persistencia

La información se almacena en el archivo `pedidos.json` en formato JSON. Cada vez que se agrega o atiende un pedido, el Repository actualiza el archivo. Al iniciar nuevamente la aplicación, los datos son cargados automáticamente.

## Interfaz gráfica

La interfaz fue desarrollada con **Tkinter**, una biblioteca incluida con Python. Permite registrar pedidos, visualizar la cola y atender el primer pedido mediante botones.

## Estructura del proyecto

```text
Robles_Kevin_Examen_Final/
├── main.py
├── requirements.txt
├── README.md
├── pedidos.json
├── src/
│   ├── __init__.py
│   ├── pedido.py
│   ├── cola.py
│   └── pedido_repository.py
└── tests/
    └── test_cola_repository.py
```

## Archivos principales

- `pedido.py`: contiene la clase `Pedido` y la conversión a/desde diccionario para la persistencia.
- `cola.py`: implementa manualmente la cola FIFO.
- `pedido_repository.py`: centraliza las operaciones y la persistencia en JSON.
- `main.py`: contiene la interfaz gráfica y conecta la GUI con el Repository.
- `test_cola_repository.py`: contiene las pruebas unitarias.

## Ejecución

1. Tener Python 3 instalado.
2. Abrir una terminal en la carpeta del proyecto.
3. Instalar pytest:

```bash
pip install -r requirements.txt
```

4. Ejecutar la aplicación:

```bash
python main.py
```

5. Ejecutar las pruebas:

```bash
python -m pytest -v
```

## Demostración

Para comprobar la persistencia, se puede registrar un pedido, cerrar el programa y volver a ejecutarlo. El pedido continuará apareciendo en la lista porque fue almacenado en `pedidos.json`.

## Repositorio

El proyecto debe estar publicado en la rama `main` del repositorio de GitHub.
