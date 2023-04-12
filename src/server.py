import socket
import client
import threading as t
import log

class Server:
    '''
    Creates an instance of translator server.

    :param ip: ip address of the server
    :param port: port which will the server listen on
    '''
    def __init__(self, ip: str = '127.0.0.1', port: int = 65525):
        self._socket: socket.socket = socket.socket()
        self._inet_addr: tuple = (ip, port)
        self._running = False
        self._dictionary = {
            'table': 'stůl',
            'run': 'běžet',
            'connection': 'připojení',
            'user': 'uživatel',
            'end': 'konec'
        }
        self.client_timeout = 10000

    '''
    Binds the ip and port to the socket and starts listening. Ip address and port will be loged.
    This function calls the loop function.
    '''
    def start(self):
        try:
            self._socket.bind(self._inet_addr)
            self._socket.setblocking(0)
            self._socket.listen()
            self._running = True
            log.log('Server started, ip:{ip}, on port: {port}'.format(ip=self._inet_addr[0], port=self._inet_addr[1]))
            self.loop()
        except Exception as err:
            log.log('Error: {err}'.format(err=str(err)))
        except KeyboardInterrupt:
            log.log('Server stoped, ip: {ip}, port: {port}'.format(ip=self._inet_addr[0], port=self._inet_addr[1]))
        finally:
            self.stop()
    '''
    Closes the socket used be the server and stops it.
    '''
    def stop(self):
        self._socket.close()
        self._running = False

    '''
    Accept new clients while the server is running.
    '''
    def loop(self):
        while self._running:
            try:
                client_socket, client_inet_addr = self._socket.accept()
                client_socket.settimeout(self.client_timeout / 1000)
                client1 = client.Client(client_socket, client_inet_addr, self)
                thread = t.Thread(target=client1.handle_client)
                thread.start()
            except OSError:
                pass
        