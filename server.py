import socket


# KONEKSI MELALUI TCP 
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# konfigurai server
s.connect(('8.8.8.8',80))

SERVER_IP = s.getsockname()[0] # get
SERVER_PORT = 4451 # open port 4451
SERVER_SIZE = 1024 # 1 MB

# gabungkan socket ke alamat ip dan port server
print("IP SERVER : ",SERVER_IP)
server_socket.bind((SERVER_IP,SERVER_PORT))

# LISTEN KONEKSI MAKSIMUM 1 CLIENT
server_socket.listen(1)
print("menunggu koneki dari klien")


# terima koneksi dari klien
conn, add = server_socket.accept()
# print(f"{add}")
print(f"Terhubung ke  client {add}")

while True:
    try:
        # terima data dari klien
        data = conn.recv(SERVER_SIZE)
        if not data:
            break
        
        # kirim ulang data 
        conn.sendall(b"Server menerima : "+ data)
    except KeyboardInterrupt:
        print("Server berhenti oleh klien")
        break


# menutuo koneki
conn.close()
server_socket.close()
print("koneksi ditutup")