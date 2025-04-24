
import socket
# server.py
host = '172.19.3.236'
port='0101'
with socket.socket() as s:
    s.bind((host, port))
    s.listen()
    print("Menunggu koneksi dari pengirim...")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Terkoneksi dengan {addr}")

            file_name_size = int.from_bytes(conn.recv(4), 'big')
            file_name = conn.recv(file_name_size).decode()
            print(f"Menerima file: {file_name}")

            with open(file_name, 'wb') as f:
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    f.write(data)

            print("File selesai diterima. Menunggu file berikutnya...\n")
 