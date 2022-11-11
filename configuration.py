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

        def add_symbol(self, name, sym):
            self.sym_list[name] = sym

        def get_symbol(self, name):
            if name in self.sym_list:
                return self.sym_list[name]
            else:
                raise Exception("Symbol '%s' is not found in the configuration"%name)

        def get_symbol_list(self):
            return self.sym_list

    __instance = None

    def __init__(self):
        if Config.__instance is None:
            Config.__instance = self
        else:
            raise Exception("Config class is a singleton. Use get_config() instead of creating an instance.")
        self.config = self.load()

    @staticmethod
    def get_config():
        if Config.__instance == None:
            Config()
        else:
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

