import socket


def send_get_response():
    host, port = "0.0.0.0", 52525
    data = "{\"type\": \"request\", \"data\": \"PING\"}"

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host, port))
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))


if __name__ == "__main__":
    send_get_response()
