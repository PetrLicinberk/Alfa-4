import server
import configparser
import config as conf

def main():
    config = conf.Config.get_instance()
    config.set_config_file('config/config.ini')
    config.read()
    s = server.Server(ip=config['server']['ip_addr'], port=int(config['server']['port']))
    s.client_timeout = int(config['server']['client_timeout'])
    s.start()

if __name__ == '__main__':
    main()