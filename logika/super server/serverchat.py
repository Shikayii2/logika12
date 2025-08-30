import socket
import threading




server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(("0.0.0.0", 12345))

server.listen()

clients = {}


def broatcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                client.close()
                del clients[client]



def handle_client(client):
    try:
        name = client.recv(1024).decode().strip()
        print(f"Отримано імя: {name}")
        if name:
            clients[client] = name
            print(f"{name} join server")
            broatcast(f"{name} join server", client)


            while True:
                message = client.recv(1024).decode()
                if not message:
                    break
                broatcast(f"{name}:{message}", client)
        else:
            client.send("Імя не може бит порожнім".encode())
            client.close()
            return
    except Exception as e:
        print(f"Error: {e}")

    print(f"{clients.get(client)} client покинув чат")
    broatcast(f"{clients.get(client)} client покинув чат")
    del  clients[client]
    client.close()


def accept_client():
    print("Сервер очікує клієнтів")
    while True:
        client, adress = server.accept()
        thread = threading.Thread(target= handle_client, args=(client))
        thread.start()

accept_client()



