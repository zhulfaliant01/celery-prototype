import socket
import os
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()
def send_file_to_remote_host(file_path, target_ip, target_port=9999):
    
    file_name = os.path.basename(file_path)
    encoded_file_name = file_name.encode()
    name_length = len(encoded_file_name)

    with socket.socket() as s:
        s.connect((target_ip, target_port))
        # 1. Kirim panjang nama file (4 bytes)
        s.sendall(name_length.to_bytes(4, 'big'))
        # 2. Kirim nama file
        s.sendall(encoded_file_name)

        # 3. Kirim isi file
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                s.sendall(data)

    logger.info(f"File {file_name} berhasil dikirim ke {target_ip}")
 