from selenium import webdriver
from NavigationStrat import NavigationStrat
import time

class Spectrum(NavigationStrat):

    #variables
    
    # store excrypted login as [b'<username/email>', b'<password>']
    __encrypted_login_data = [b'gAAAAABey0bs2nhXKVwK_PeYkiCAcVZUM-HBZWC6R259PlbIvvS71WYcdNh5KbEXqfAxsr9alBwfHa7nwopAbDuey73bqZgVNeb1pjzD_zSmPzY3xALhtmI=', b'gAAAAABey0bsdeD6RDNyhdFLNALEQwi6TmynbC8mOoVSBGUnfxgZbBu5yaSi8t-jkbEq-RbMWWya-DfKsOQ31aa9fgekuAQ2qJ7zQ0pDy2Y_T0XFmjbgHZU=']

    # function implementation
    def fetch_total(self):
        
        # decrypt user login data
        decrypted_login_data = self.decrypt_login( self.__encrypted_login_data )

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

        return 'Spectrum:\t' + balance
