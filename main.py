from socket import socket, AF_INET, SOCK_STREAM
from client.application import ChatApplication
from client.client import TCP_Client


def main():
    host = "pmikkelsen.com"
    port = "50733"
    client = ChatApplication(TCP_Client(host, port))
    client.run()


if __name__ == '__main__':
    main()