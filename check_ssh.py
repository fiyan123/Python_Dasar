import paramiko
import socket

def is_ssh_address(address, timeout=5):
    try:
        # Pisahkan hostname dan port jika ada
        if ':' in address:
            hostname, port = address.split(':')
            port = int(port)
        else:
            hostname = address
            port = 22
        
        # Buat objek SSHClient
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Coba untuk melakukan koneksi SSH
        ssh.connect(hostname, port=port, timeout=timeout)
        
        # Jika koneksi berhasil, maka alamat tersebut adalah alamat SSH
        ssh.close()
        return True
    except (paramiko.SSHException, socket.error):
        # Jika ada kesalahan, maka alamat tersebut bukan alamat SSH
        return False

# Contoh penggunaan
address = '192.168.4.28'
if is_ssh_address(address):
    print(f"{address} adalah alamat SSH.")
else:
    print(f"{address} bukan alamat SSH.")
