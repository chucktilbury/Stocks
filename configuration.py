'''
    This module abstracts the information that all of the stock and tickers
    require as well as the configuration for the actual program.
'''
import os, sys
import pickle

class Config(object):

    class _configuration(object):
        '''
        This class is a private singleton data container.
        '''
        def __init__(self):
            # add config items here, along with getter and setter.
            self.sym_list = {}
            self.default_period = 'max'
            self.default_interval = '1m'

        def add_symbol(self, name, sym):
            self.sym_list[name] = sym

        def get_symbol(self, name):
            if name in self.sym_list:
                return self.sym_list[name]
            else:
                raise Exception("Symbol '%s' is not found in the configuration"%name)

        def get_symbol_list(self):
            return self.sym_list

        def set_default_period(self, val):
            self.default_period = val

        def get_default_period(self):
            return self.default_period

        def set_default_interval(self, val):
            self.default_interval = val

        def get_default_interval(self):
            return self.default_interval

    __instance = None

    def __init__(self):
        print(">>>>>> create config constructor")
        if Config.__instance is None:
            print(">>>>> here")
            Config.__instance = self
        else:
            raise Exception("Config class is a singleton. Use get_config() instead of creating an instance.")
        print(">>>>> here1")
        self.config = self.load()

    @staticmethod
    def get_config():
        if Config.__instance is None:
            print(">>>>>> create config")
            Config()
        return Config.__instance

    def load(self):
        return self._load_config(self._find_config())

    def save(self):
        self._save_config(self._find_config())

    def _find_config(self):
        if os.name == 'nt':
            fname = os.path.join(os.environ['UserProfile'], 'stocks_config.data')
        else:
            fname = os.path.join(os.environ['HOME'], 'stocks_config.data')
        if not os.path.exists(fname):
            self._create_config(fname)
        return fname

    def _load_config(self, fname):
        with open(fname, "rb") as fh:
            self.config = pickle.load(fh, fix_imports=True)

    def _save_config(self, fname):
        with open(fname, "wb") as fh:
            pickle.dump(self.config, fh, fix_imports=True)

    def _create_config(self, fname):
        self.config = Config._configuration()
        self._save_config(fname)

    # below here, add the api getter and setter for configuration items.
    def add_symbol(self, name, symbol):
        '''
        Store a symbol object to the configuration
        '''
        self.config.add_symbol(name, symbol)

    def get_symbol(self, name):
        '''
        Return a symbol object from the configuration.
        '''
        return self.config.get_symbol(name)

    def set_default_period(self, val):
        self.config.default_period = val

    def default_period(self):
        print("default period = %s"%self.config.default_period)
        return self.config.default_period

    def set_default_interval(self, val):
        self.config.default_interval = val

    def default_interval(self):
        return self.config.default_interval
