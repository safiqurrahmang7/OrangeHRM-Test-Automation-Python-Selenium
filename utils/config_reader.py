import configparser
import os


class ConfigReader:
    CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), "config.properties")

    @staticmethod
    def get_property(property_name):
        config = configparser.ConfigParser()
        config.read(ConfigReader.CONFIG_FILE_PATH)

        # Properties file does not support sections, so add a default section header in memory
        section = "CONFIG"
        config.read_dict({section: dict(config.items(section))})

        return config.get(section, property_name, fallback=None)
