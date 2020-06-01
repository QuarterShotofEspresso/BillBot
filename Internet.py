from selenium import webdriver
from NavigationStrat import NavigationStrat
import time

class Spectrum(NavigationStrat):

    #variables 
    __encrypted_login_data = 0      # store excrypted login as [b'<username/email>', b'<password>']


    # function implementation
    def fetch_total(self):
       
        try:
            # load and decrypt user login data
            self.__encrypted_login_data = self.load_login_dictionary()['SPECTRUM']
            decrypted_login_data = self.decrypt_login(self.__encrypted_login_data, 'Spectrum Password: ')

            # create firefox driver
            driver = webdriver.Firefox()
            driver.get('https://www.spectrum.net')

            # wait for the page to load
            time.sleep(10)

            # find username entry element and fill in data
            element = driver.find_element_by_id('cc-username')
            element.send_keys( decrypted_login_data[0] ) # send username
        
            # find password entry element and fill in data
            element = driver.find_element_by_id('cc-user-password')
            element.send_keys( decrypted_login_data[1] ) # send password

            # find 'Sign In' button and click
            driver.find_element_by_class_name('kite-btn.kite-btn-lg.kite-btn-primary.kite-btn-light.dialog_button').click()

            # wait for the page to load
            time.sleep(10)

            # return 'balance' string
            balance = driver.find_element_by_class_name('balance').text

            #close driver
            driver.close()

            balance_numeric = float(balance[2:])

            return 'Spectrum:\t' + balance, balance_numeric

        except:
            return 'Spectrum ERR access fail', 0.00
