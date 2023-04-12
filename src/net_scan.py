import ipaddress
import connection
import config as conf
import re

def scan():
    '''
    Scans range of ips and ports defined in configuration file and checks,
    whether there is another translator.
    
    :return: list of found servers (ip, port)
    '''
    config = conf.Config.get_instance()
    ip_start = ipaddress.IPv4Address(config['scan']['ip_scan_start'])
    ip_end = ipaddress.IPv4Address(config['scan']['ip_scan_end'])
    port_start = int(config['scan']['port_scan_start'])
    port_end = int(config['scan']['port_scan_end'])
    timeout = int(config['scan']['scan_timeout'])
    prog_name = config['server']['name']

    found = []
    if ip_start > ip_end or port_start > port_end:
        return found
    ip = ip_start
    while ip <= ip_end:
        for port in range(port_start, port_end + 1):
            if str(ip) == config['server']['ip_addr'] and port == int(config['server']['port']):
                continue
            try:
                conn = connection.Connection(str(ip), port, 'TRANSLATEPING"{name}"'.format(name=prog_name), timeout)
                response = conn.connect()
                if re.match(r'^TRANSLATEPONG"(.*)"$', response) is not None:
                    found.append((str(ip), port))
            except:
                pass
        ip += 1
    return found