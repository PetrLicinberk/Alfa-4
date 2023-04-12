import socket

class Connection:
    '''
    Prepares an connection.

    :param ip_address: ip_address of the server
    :param port: port which the server is listening on
    :param message: message which will be sent to the server
    :param timeout: connection timeout
    '''
    def __init__(self, ip_address, port, message, timeout) -> None:
        self._ip_addr = ip_address
        self._port = port
        self._message = message
        self._timeout = timeout

    '''
    Connects to a server, send the message, recieves an answer and returns it.
    If conection fails emty string will be returned.

    :return: response from the server
    '''
    def connect(self):
        response = ''
        soc = socket.socket()
        soc.settimeout(self._timeout / 1000.0)
        err = soc.connect_ex((self._ip_addr, self._port))
        if err == 0:
            soc.send(bytes(self._message, 'utf-8'))
            response = soc.recv(128).decode().strip()
        soc.close()
        return response