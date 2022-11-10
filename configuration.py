'''
    This module abstracts the information that all of the stock and tickers
    require as well as the configuration for the actual program.
'''
import os, sys

class _configuration(object):
    '''
    This class is a private singleton data container.
    '''

class Config(object):

    def load(self):
        self._load_config(self._find_config())

    def save(self):
        self._save_config(self._find_config())

    def _find_config(self):
        fname = os.path.join(os.environ['HOME'], 'stocks_config.data')
        if not os.file_exists(fname):
            self._create_config(fname)
        return fname

    def _load_config(self, fname):
        print("load configuration:", fname)

    def _save_config(self, fname):
        print("save configuration:", fname)

    def _create_config(self, fname):
        print("create configuration:", fname)

