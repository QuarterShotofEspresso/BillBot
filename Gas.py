from selenium import webdriver
from NavigationStrat import NavigationStrat
import time

class SoCalGas(NavigationStrat):

    #variables 
    __encrypted_login_data = 0      # store excrypted login as [b'<username/email>', b'<password>']


    # function implementation
    def fetch_total(self, password):

        try:
            # load and decrypt user login data
            self.__encrypted_login_data = self.load_login_dictionary()['SOCALGAS']
            decrypted_login_data = self.decrypt_login(self.__encrypted_login_data, password)

            # create firefox driver
            driver = webdriver.Firefox()
            driver.get('https://myaccount.socalgas.com/')

            # wait for the page to load
            time.sleep(10)

            # find username entry element and fill in data
            element = driver.find_element_by_id('pt1:pli1:loginid::content')
            element.send_keys( decrypted_login_data[0] ) # send username
            
            # find password entry element and fill in data
            element = driver.find_element_by_id('pt1:pwli:pwd::content')
            element.send_keys( decrypted_login_data[1] ) # send password

            # find 'Sign In' button and click
            driver.find_element_by_id('pt1:cb1').click()

            # wait for the page to load
            time.sleep(10)

            # return 'balance' string
            balance = driver.find_element_by_class_name('rma-cur-balance').text

            #close driver
            driver.close()

            balance_numeric = float(balance[1:])

            return 'SoCalGas:\t' + balance, balance_numeric

        except:
            return 'SoCalGas ERR access fail', 0.00
