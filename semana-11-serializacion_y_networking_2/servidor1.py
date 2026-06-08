# Implementación del servidor que recibe datos y los envía de vuelta.
# Esto comúnmente se denomina como 'echo server'.

import socket


host = 'localhost'   # Usar nuestro computador como host
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
print("Listo para recibir. Ahora voy a esperar que me hablen...")
sock.listen()

sock_cliente, (host_cliente, puerto_cliente) = sock.accept()
print("Conexión desde", host_cliente, puerto_cliente)

while True:
    data = sock_cliente.recv(4096)
    print(f"Recibí estos bytes: {data}")
    if not data:
        break
    print("Los enviaré de vuelta")
    sock_cliente.sendall(data)

sock_cliente.close()
