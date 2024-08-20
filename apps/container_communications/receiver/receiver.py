import socket


def run_server():
    host, port = "0.0.0.0", 52525
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)

    response: str = "{\"type\": \"request\", \"data\": \"PONG\"}"
    print(f'Starting up on {host}: 52525')
    while True:
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)
            while True:  # Read the data in small chunks and retransmit it
                data: bytes = connection.recv(1024)
                request: str = data.decode('utf-8')
                if data:
                    print(request)
                    connection.sendall(bytes(response, 'utf-8'))
                else:
                    print('no data from', client_address)
                    break
        finally:  # Clean up the connection
            connection.close()


if __name__ == "__main__":
    run_server()

