import socket
import threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("5.tcp.eu.ngrok.io", 14678))

name = input("name:")
client.send(name.encode())
print("Тепер ви можете надсилати повідомлення нижче!")


def recive_mess():
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                print(message)
        except Exception as e:
            print(f"Error:{e}")
            print("Зєднання закрите")
            client.close()
            break   


def send_mes():
    while True:
        message = input()
        client.send(message.encode())




recive_theard = threading.Thread(target=recive_mess)
send_theard = threading.Thread(target=send_mes)

recive_theard.start()
send_theard.start()
