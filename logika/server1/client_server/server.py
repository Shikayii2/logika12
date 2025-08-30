import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)




server.bind(("localhost", 12345))




server.listen(1)
print("сервер очікує на клієнта")


connection, adress = server.accept()

print(f"Підключився клієнт: {adress}")

data = connection.recv(1024).decode()
print(f"Отримано: {data}")


connection.send("Hi".encode())
connection.close()
server.close()