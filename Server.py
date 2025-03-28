import socket
import threading

HOST = '0.0.0.0'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Servidor iniciado en {HOST}:{PORT}")
clientes = []

def handle_client(client_socket, address):
    print(f"Nueva conexión desde {address}")
    clientes.append(client_socket)
    first_message = True

    try:
        while True:
            mensaje = client_socket.recv(1024).decode('utf-8')

            if not mensaje:
                break
            if mensaje.lower() == 'desconexion':
                print(f"Cliente {address} solicitó desconexión.")
                break

            print(f"Mensaje de {address}: {mensaje}")
            
            if first_message and mensaje.lower() == 'hola servidor':
                client_socket.send("HOLA CLIENTE".encode('utf-8'))
                first_message = False
            else:
                client_socket.send(mensaje.upper().encode('utf-8'))

    except ConnectionResetError:
        print(f"Cliente {address} se desconectó abruptamente.")
    except Exception as e:
        print(f"Error con cliente {address}: {e}")
    finally:
        print(f"Cliente {address} desconectado.")
        clientes.remove(client_socket)
        client_socket.close()

while True:
    try:
        client_socket, addr = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True)
        client_handler.start()
    except KeyboardInterrupt:
        print("\nServidor cerrando...")
        break
    except Exception as e:
        print(f"Error en la conexión: {e}")

for cliente in clientes:
    cliente.close()
server_socket.close()
print("Servidor cerrado.")