import config as conf
import net_scan
import connection
import re

class Command:
    def __init__(self, client) -> None:
        self._client = client
    
    '''
    Code which will be executed when server recieves the command form a client.

    :param arg: command argument
    '''
    def execute(self, arg):
        raise NotImplementedError

class TranslateLoclCommand(Command):
    def __init__(self, client) -> None:
        super().__init__(client)

    '''
    Translates word and sends the translation to the client.

    :param arg: word which will be translated
    '''
    def execute(self, arg):
        if arg in self._client.get_dict():
            translation = self._client.get_dict()[arg]
            self._client.send('TRANSLATEDSUC"{trans}"'.format(trans=translation))
        else:
            self._client.send('TRANSLATEDERR"Not found"')

class TranslatePingCommand(Command):
    def __init__(self, client) -> None:
        super().__init__(client)

    '''
    This command responds to the TRANSLATEPING"" command with TRANSLATEPONG"<name_of_the_program>."
    '''
    def execute(self, arg):
        config = conf.Config.get_instance()
        self._client.send('TRANSLATEPONG"{name}"'.format(name=config['server']['name']))

class TranslateScanCommand(Command):
    def __init__(self, client) -> None:
        super().__init__(client)

    '''
    This command translates a word. Frist it checks local dictionary,
    if it's not there it scans range of ips and ports.
    '''
    def execute(self, arg):
        if arg in self._client.get_dict():
            translation = self._client.get_dict()[arg]
            self._client.send('TRANSLATEDSUC"{trans}"'.format(trans=translation))
            return
        config = conf.Config.get_instance()
        found = net_scan.scan()
        translation = None
        for server in found:
            conn = connection.Connection(server[0], server[1], 'TRANSLATELOCL"{word}"'.format(word=arg), int(config['server']['translate_locl_timeout']))
            response = conn.connect()
            match = re.match(r'^TRANSLATEDSUC"(.+)"$', response)
            if match is not None:
                translation = match.group(1)
                break
        if translation is not None:
            self._client.send('TRANSLATEDSUC"{trans}"'.format(trans=translation))
        else:
            self._client.send('TRANSLATEDERR"Not found"')