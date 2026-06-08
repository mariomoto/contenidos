import socket


host_receptor = 'localhost'
puerto_receptor = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Nos conectamos al receptor del archivo, que ya debería estar escuchando.
sock.connect((host_receptor, puerto_receptor))
print("Conexión establecida.")

# Leemos el archivo y lo enviamos.
with open('files/enviar.bin', 'rb') as binfile:
    datos = binfile.read()
    largo_archivo = len(datos)
    print(f"Voy a enviar {largo_archivo} bytes")
    # 1. Enviar el tamaño del archivo.
    # (int.to_bytes transforma un entero en una cantidad de bytes por el primer parámetro)
    sock.sendall(largo_archivo.to_bytes(4, byteorder='big'))

    # 2. Enviar el archivo. Para esto haremos uso del método send en vez de sendall, para asegurarnos
    # que todo se envíe correctamente
    bytes_enviados = 0
    while bytes_enviados < largo_archivo:
        # Enviaremos el mensaje cortado desde el último punto efectivamente enviado.
        bytes_enviados += sock.send(datos[bytes_enviados:])


print("¡Archivo enviado!")

# Imprimimos lo que nos responda la contraparte.
print("Respuesta:", sock.recv(4096).decode('utf-8'))

# Cerramos el socket.
sock.close()