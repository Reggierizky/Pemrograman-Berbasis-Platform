import socket
import threading

# Konfigurasi server
HOST = '127.0.0.1'
PORT = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Server berjalan di {HOST}:{PORT}")

clients = []
usernames = {}

# Kirim pesan ke semua client KECUALI pengirim
def broadcast(message, sender_conn=None):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                if client in clients:
                    clients.remove(client)

# Tangani masing-masing client
def handle_client(conn, addr):
    username = conn.recv(1024).decode('utf-8')
    usernames[conn] = username
    clients.append(conn)
    print(f"{username} bergabung dari {addr}")

    broadcast(f"{username} bergabung ke chat!", conn)

    while True:
        try:
            pesan = conn.recv(1024).decode('utf-8')
            if not pesan or pesan.lower() == "exit":
                broadcast(f"{username} keluar dari chat.", conn)
                print(f"{username} keluar dari chat.")
                conn.close()
                clients.remove(conn)
                break

            full_msg = f"[{username}]: {pesan}"
            print(full_msg)
            broadcast(full_msg, conn)

        except:
            conn.close()
            if conn in clients:
                clients.remove(conn)
            break

# Loop utama server
while True:
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    