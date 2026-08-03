#base source : https://github.com/LittleViewer/WeakSignalFinder/blob/main/libCore/config_tool_class.py in AGPLv3
import tomllib
import utils_class as utC

class config_toml_tool:

    def key_return(self, table,key, sub_table = None):
        if self.utC_.is_string(table) != True or self.utC_.is_string(key) != True:
            self.utC_.error_with_reason("An error occurred with the configuration file!")
            return False
        if sub_table == None:
            return self.config[table][key]
        else:
            if self.utC_.is_string(sub_table) != True:
                self.utC_.error_with_reason("An error occurred with the configuration file!")
                return False
            return self.config[table][sub_table][key]

    def __init__(self, path = "config_sensor.toml"):
        self.utC_ = utC.utils()
        handle = open(self.utC_.absolute_link(path),"rb")
        self.config = tomllib.load(handle)