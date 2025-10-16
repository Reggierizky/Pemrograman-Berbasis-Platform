import socket
import threading

# Konfigurasi server
HOST = '127.0.0.1'
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

username = input("Masukkan username Anda: ")
client_socket.send(username.encode('utf-8'))

print("Terhubung ke server. Ketik 'exit' untuk keluar.\n")

# Terima pesan dari server
def terima_pesan():
    while True:
        try:
            pesan = client_socket.recv(1024).decode('utf-8')
            if not pesan:
                break
            print(pesan)
        except:
            print("Koneksi ke server terputus.")
            client_socket.close()
            break

threading.Thread(target=terima_pesan, daemon=True).start()

# Kirim pesan
while True:
    pesan = input("")
    if pesan.lower() == "exit":
        client_socket.send(pesan.encode('utf-8'))
        print("Keluar dari chat...")
        client_socket.close()
        break

    print(f"You ({username}): {pesan}")
    client_socket.send(pesan.encode('utf-8'))