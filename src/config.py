import configparser as cp

class Config:
    _instance = None
    def __init__(self):
        self._config_file = None
        self._config = cp.ConfigParser()
    
    def __getitem__(self, key):
        return self.get_config()[key]
    
    '''
    If an instance of Config does not exist, new one will be created.

    :return: Config instance
    '''
    def get_instance():
        if Config._instance is None:
            Config._instance = Config()
        return Config._instance

    '''
    Sets the location of the config file.

    :param config_file: path to the config file
    '''
    def set_config_file(self, config_file:str):
        if type(config_file) != str:
            raise TypeError
        self._config_file = config_file
    
    '''
    :return: configparser
    '''
    def get_config(self):
        return self._config
    
    '''
    Reads contents of the config file.
    '''
    def read(self):
        self._config.read(self._config_file)