from selenium import webdriver
from BeautifulSoup import BeautifulSoup


import NavigationStrat



class Internet(NavigationStrat):

    #variables
    password
    username
    stieURL
    
    #constructor
    def __init__(self, passwrd, usr, url):
        self.password = passwrd
        self.username = usr
        self.siteURL = url

    # function implementation
    def fetchTotal(self):
        driver = webdriver.Chrome("")
        driver.get("https://www.spectrum.net")
        content = drvier.page_source()
        soup = BeautifulSoup(content)
        
        return 0.0
