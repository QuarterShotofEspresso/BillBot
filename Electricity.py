from selenium import webdriver
from NavigationStrat import NavigationStrat
import time

class PublicUtilities(NavigationStrat):

    #variables 
    __encrypted_login_data = 0      # store excrypted login as [b'<username/email>', b'<password>']


    # function implementation
    def fetch_total(self, password):
        # load and decrypt user login data
        self.__encrypted_login_data = self.load_login_dictionary()['PUBLIC_UTIL']
        decrypted_login_data = self.decrypt_login(self.__encrypted_login_data, password)

        # create firefox driver
        driver = webdriver.Firefox()
        driver.get('https://billpay.riversideca.gov/')

        # wait for the page to load
        time.sleep(10)

        try:
            # find username entry element and fill in data
            element = driver.find_element_by_id('login:usernamedec:username')
            element.send_keys( decrypted_login_data[0] ) # send username
        
            # find password entry element and fill in data
            element = driver.find_element_by_id('login:j_id155:password')
            element.send_keys( decrypted_login_data[1] ) # send password

            # find 'Sign In' button and click
            driver.find_element_by_id('login:j_id163').click()

            # wait for the page to load
            time.sleep(10)

            # return 'balance' string
            balance = driver.find_element_by_id('j_id161:j_id315').text #NOTE: The ID seems to have changed for this element.
                                                                        #TODO: Check to see if this script fails this site again

            #close driver
            driver.close()

            balance_numeric = float(balance[1:])

            return 'Public Util:\t' + balance, balance_numeric

        except:
            return 'Public Util ERR access fail', 0.00
