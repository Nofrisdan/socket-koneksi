import socket


# konfigurasi klien 
SERVER_IP = input(str("Masukkan IP Address Client : "))
SERVER_PORT = 4451
BUFFER_SIZE = 1024 # 1 MB


# MEMBUAT SOCKET tcp 
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    
    # connect ke server
    client_socket.connect((SERVER_IP,SERVER_PORT))
    print("Terhubung ke server")

    while True:
        # mengirim data ke server
        data = input("Ketik pesan mengirim ke server (exit untuk keluar)").encode('utf-8')
        client_socket.sendall(data)

        if data.decode('utf-8').lower() == 'exit':
            break

        # menerima dan mencetak balasan dari server
        response = client_socket.recv(BUFFER_SIZE)
        print("Balasan dari server : ",response.decode('utf-8'))

except KeyboardInterrupt:
    print("Koneksi ditutup oleh pengguna")

finally:
    # menutup koneksi
    client_socket.close()
    print("koneksi ditutup")