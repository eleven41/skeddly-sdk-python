import configparser

from pathlib import Path

def load_config(section = None):
    if (section is None):
        section = "default"

    configFile = str(Path(Path.home(), ".skeddlyrc"))
    #print("Config File: " + configFile)

    config = configparser.ConfigParser()
    config.read(configFile)

    return {
        "accessKey": config[section]["accessKey"]
    }
