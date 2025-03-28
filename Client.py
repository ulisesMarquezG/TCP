import socket

HOST = '127.0.0.1'
PORT = 5000  

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))


    client_socket.sendall("hola servidor".encode('utf-8'))
    respuesta = client_socket.recv(1024).decode('utf-8')

    print(f"Respuesta del servidor: {respuesta}")
    print("Conectado al servidor. Puedes empezar a enviar mensajes.")

    while True:
        mensaje = input("Escribe un mensaje (o 'DESCONEXION' para terminar): ").strip()
        
        if mensaje.lower() == 'desconexion':
            client_socket.sendall(mensaje.encode('utf-8'))

        try:
            client_socket.sendall(mensaje.encode('utf-8'))
            respuesta = client_socket.recv(1024).decode('utf-8')
            if not respuesta:
                print("El servidor cerró la conexión.")
                break
            print(f"Respuesta del servidor: {respuesta}")
        except socket.error:
            print("Error al enviar/recibir datos.")
            break
except ConnectionRefusedError:
    print("No se pudo conectar al servidor. Asegúrate de que está en ejecución.")
except Exception as e:
    print(f"Error inesperado: {e}")
finally:
    client_socket.close()
    print("Conexión cerrada.")
