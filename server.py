import json
import threading
import socket
import hou
from .meta import AssetFactory
import os

class MyServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_running = True

    def start(self):
        print("server is running baby!")
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        pass
        while self.is_running:
            try:
                client, address = self.socket.accept()
                threading.Thread(target=self.handle_client, args=(client,)).start()
            except OSError as e:
                if self.is_running:
                    raise e
                else:
                    pass

    def handle_client(self, client_socket):
        with client_socket:
            total_data = b""
            while True:
                data = client_socket.recv(4096)
                if not data:
                    break
                total_data += data
            json_data = json.loads(total_data.decode('ascii'))
            AssetFactory.GenerateAsset(json_data)
            

    def stop(self):
        print("We are stopped")
        self.is_running = False
        self.socket.close()



