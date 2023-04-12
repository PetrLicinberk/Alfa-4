import socket
import commands
import re
import time
import log

class Client:
    '''
    Creates an instance of client.

    :param connection: client's socket
    :param inet_addr: client's ipv4 address and port
    :param server: Server object reference
    '''
    def __init__(self, connection, inet_addr, server):
        self._socket: socket.socket = connection
        self._inet_addr: tuple = inet_addr
        self._server = server
        self._commands = {
            'TRANSLATELOCL': commands.TranslateLoclCommand(self),
            'TRANSLATEPING': commands.TranslatePingCommand(self),
            'TRANSLATESCAN': commands.TranslateScanCommand(self)
        }

    '''
    Function handle_client handles communication with client. It recieves and executes
    command from the client then closes the socket.
    '''
    def handle_client(self):
        try:
            cmd = self.recv().strip()
            result = re.match(r'^([A-Z]+)"(.*)"$', cmd)
            if result is not None and result.group(1) in self._commands:
                self._commands[result.group(1)].execute(result.group(2))
                log.log('Client: {ip}, on port: {port}, executed: {cmd}'.format(ip=self._inet_addr[0], port=self._inet_addr[1], cmd=cmd))
            else:
                self.send('TRANSLATEDERR"Invalid command"')
        except TimeoutError:
            pass
        finally:
            time.sleep(0.001)
            self._socket.close()

    '''
    Sends a message to the client with utf-8 encoding.

    :param message: message, which will be sent
    '''
    def send(self, message):
        msg_bytes = bytes(message, 'utf-8')
        self._socket.send(msg_bytes)

    '''
    Recieves a message from the client and decodes it.

    :param num_bytes: number of bytes recieved
    :return: decoded message
    '''
    def recv(self, num_bytes = 64):
        msg: bytes = self._socket.recv(num_bytes)
        return msg.decode()

    '''
    Gets dictionary from the server.

    :return: dictionary
    '''
    def get_dict(self):
        return self._server._dictionary