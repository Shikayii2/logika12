import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("localhost",12345))

client.send("hi".encode())


responce =client.recv(1024).decode()


print(f"ВІДПОВІТЬ ВІД SERVERAAA: {responce}")

client.close()