from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from client.interface import IClient

class ClientCommand:
    pass

class ClientEncrypt:
    pass


class ClientDecrypt:
    pass


class TCP_Client(IClient):

    def __init__(self, **kwargs):
        if "host" in kwargs.keys() and "port" in kwargs.keys():
            pass
        else:
            raise ValueError(f"Host or Port not supplied to TCP client!")

    def connect(self, host=None, port=None):
        conn = ClientConnect()
        conn.connect(host, port)
        self.sock = conn()


class ClientConnect:
    sock: "socket"

    def __init__(self, sock=None):

        if sock is None:
            self.sock = socket(AF_INET, SOCK_STREAM)
        else:
            self.sock = sock


    def connect(self, host=None, port=None):
        if host is None:
            raise ValueError(f"Host can not be None")
        if port is None:
            raise ValueError(f"Port cannot be None")
        self.sock.connect((host, port))

    def __call__(self, *args, **kwargs):
        return self.sock