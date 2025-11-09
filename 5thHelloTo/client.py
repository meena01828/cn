import socket

def start_client():
    host = '127.0.0.1'  # Server IP
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Send hello to server
    client_socket.sendall("Hello from client!".encode())

    # Receive reply from server
    reply = client_socket.recv(1024).decode()
    print(f"Server says: {reply}")

    client_socket.close()
    print("Hello message exchange completed.")

if __name__ == "__main__":
    start_client()
