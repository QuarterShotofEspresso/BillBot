import base64
import json
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class NavigationStrat:

    # private varaibles
    __salt = b'h1\xf7\xdb\xf5\xebA(e\xa9\xf2\x9c\xde\x01\xb1\x9d'
    __LOGIN_DATA_FILEPATH = './input/login_data.json' # file path to loginin data 

    def fetch_total(self, password):
        raise NotImplementedError


    def load_login_dictionary(self):
        fio_suite = open(self.__LOGIN_DATA_FILEPATH, 'r')
        return json.load(fio_suite)


    @classmethod
    def fetch_key(cls, password_string):

        # stetch password 
        kdf = PBKDF2HMAC(
                algorithm = hashes.SHA256(),
                length = 32,
                salt = cls.__salt,
                iterations = 100000,
                backend = default_backend()
        )

        # extend the password and encode in b64
        key =  base64.urlsafe_b64encode(kdf.derive(password_string.encode()))

        return key


    # called by strategies
    def decrypt_login(self, encrypted_user_login_bytes = [], password = ''):
        
        decrypted_user_login = []

        # retrieve password from user
        # password = getpass(password_prompt)
        
        # tranlsate password into key
        key = self.fetch_key( password )

        # use key to generate Fernet encryption suite
        encryption_suite = Fernet( key )

        # return decrypted user login
        for user_login_element in encrypted_user_login_bytes:
            decrypted_user_login.append(encryption_suite.decrypt(user_login_element.encode()).decode())

        return decrypted_user_login


    # easier to encrypt login information
    @classmethod
    def encrypt_login(cls, user_login = []):

        # retrieve password from user
        password = getpass()

        # extend the password and encode in b64
        key = cls.fetch_key( password )
        
        # use password to make encryption_suite with Fernet
        encryption_suite = Fernet( key )

        encrypted_login = []

        # decrypt user_login
        for user_login_element in user_login:
            encrypted_login.append(encryption_suite.encrypt(user_login_element.encode()).decode())

        print(encrypted_login)



