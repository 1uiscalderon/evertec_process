from datetime import datetime
from dotenv import dotenv_values
import base64
import hashlib
import random
import json


ENV = dotenv_values('.env')
LOGIN = ENV.get('LOGIN')
TRAN_KEY = ENV.get('TRAN_KEY')


class Authreq:
    def __init__(self, login=LOGIN, tran_key=TRAN_KEY):
        """ Initializing class """
        self.login = login
        self.tran_key = tran_key
        self.nonce = str(random.random())
        self.seed = datetime.now().isoformat()

    # https://placetopay.github.io/web-checkout-api-docs/#redirectrequest
    def generate_key(self):
        """ Create values for key """
        tran_key = str(self.nonce + self.seed + self.tran_key)
        return base64.b64encode(hashlib.sha1(tran_key.encode('utf-8')).digest())

    def get_nonce(self):
        """ Generating nonce """
        return base64.b64encode(self.nonce.encode('utf-8'))

    def get_auth(self):
        """ Setting information """
        auth = {'login': self.login,
                'tranKey': self.generate_key().decode('utf-8'),
                'nonce': self.get_nonce().decode('utf-8'),
                'seed': self.seed
                }
        return auth
