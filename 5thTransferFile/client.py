import socket
import os

def send_file(filepath):
    host = '127.0.0.1'  # Server IP
    port = 12346

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    filename = os.path.basename(filepath)
    filename_bytes = filename.encode()
    filename_size = len(filename_bytes)

    # Send filename size (2 bytes) and filename
    client_socket.send(filename_size.to_bytes(2, 'big'))
    client_socket.send(filename_bytes)

    # Send file content in chunks
    with open(filepath, 'rb') as f:
        while True:
            bytes_read = f.read(4096)
            if not bytes_read:
                break
            client_socket.sendall(bytes_read)

    print("File sent successfully.")
    client_socket.close()

if __name__ == "__main__":
    # Change filepath to any small text file
    filepath = "testfile.txt"

    # If a file with this name exists next to the script, prefer it.
    script_dir = os.path.dirname(__file__)
    script_local = os.path.join(script_dir, filepath)
    if os.path.exists(script_local):
        filepath = script_local

    # Helpful diagnostics if the file is missing
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        print(f"Current working directory: {os.getcwd()}")
        print("Possible fixes:")
        print("  - Put the file in the current working directory before running the script.")
        print("  - Place the file next to this script (we also check that location automatically).")
        print("  - Use an absolute path for `filepath`.")
    else:
        send_file(filepath)
