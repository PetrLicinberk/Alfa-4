import config as conf
import datetime

'''
Logs a message and current time to the log file defined in config file.

:param text: text which will be saved to log file
'''
def log(text: str):
    config = conf.Config.get_instance()
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(config['log']['log_file'], 'a', encoding='utf-8') as log_file:
        log_file.write('[{time}] {text}\n'.format(time=current_time, text=text))