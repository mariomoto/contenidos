# Este es el receptor del archivo.
import socket


host = 'localhost'
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()
print("Escuchando...")

# Aceptamos un cliente.
sock_cliente, (host_cliente, port_cliente) = sock.accept()
print("Conexión entrante aceptada.")

# Leemos la información y la guardamos en un archivo.
datos = sock_cliente.recv(4096)
with open('files/recibido.bin', 'wb') as binfile:
    binfile.write(datos)

print("¡Archivo recibido!")
# Le enviamos una respuesta a la contraparte.
sock_cliente.sendall("Gracias.".encode('utf-8'))

# Cerramos los sockets.
sock_cliente.close()
sock.close()