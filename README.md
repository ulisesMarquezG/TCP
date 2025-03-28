# Cliente-Servidor con Sockets en Python

Este proyecto implementa una comunicación básica cliente-servidor utilizando sockets en Python. El servidor escucha en un puerto y el cliente puede enviar mensajes al servidor. El servidor responde al cliente con el mismo mensaje en mayúsculas.

## Requisitos

- Python 3.x (se recomienda la versión más reciente).
- No se requieren dependencias externas.

## Archivos

- **Server.py**: Código del servidor que escucha las conexiones de los clientes y responde con el mensaje en mayúsculas.
- **Client.py**: Código del cliente que se conecta al servidor y envía mensajes.
  
## Cómo Ejecutar

### 1. Ejecutar el Servidor

Primero, debes iniciar el servidor. En una terminal, navega a la carpeta donde se encuentran los archivos y ejecuta el siguiente comando:

python Server.py

### 2. Ejecutar el Cliente

En otra terminal, navega a la misma carpeta donde están los archivos y ejecuta el cliente:

python Client.py
