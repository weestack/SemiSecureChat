class IClient:
    sock: "socket"
    host: str
    port: str

    def send(self): pass
    def connect(self): pass
    def receive(self): pass
    def __init__(self, **kwargs): pass