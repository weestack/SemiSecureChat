class ChatApplication:
    client: "IClient"

    def run(self):
        pass

    def command(self):
        pass

    def encrypt(self):
        pass

    def decrypt(self):
        pass

    def connect(self):
        response = self.client.connect()
        if not response:
            raise ConnectionError(f"Could not connect to the Client")

