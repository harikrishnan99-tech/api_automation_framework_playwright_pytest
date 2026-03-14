import configparser

def get_config_data(section, key):
    config = configparser.ConfigParser()
    config.read('data/config_data.ini')
    return config[section][key]
