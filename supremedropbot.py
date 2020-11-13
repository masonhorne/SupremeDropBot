import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Supreme site data
mainUrl = 'https://www.supremenewyork.com/shop/all'
baseUrl = 'https://www.supremenewyork.com'
checkoutUrl = 'https://www.supremenewyork.com/checkout'
productUrl = None

# This is an application that preforms web scraping to purchase product from Supreme website


class Application:
    # This function shuts down the browser in case product cannot be found
    def cancel_search(self):
        self.browser.quit()

    # This searches for the product on the website
    def search_product(self):
        # This gets a request for the page of the items category
        response = requests.get(mainUrl + '/' + self.itemCategory).text
        soup = BeautifulSoup(response, 'html.parser')
        # This loops through each container of item on the website
        for div in soup.find_all('ul', 'turbolink_scroller'):
            # This searches through the information in the items container
            for item in div.find_all('div', {'class': 'inner-article'}):
                name_flag = False
                # This loops to see if the item has the correct name
                # If it is it sets the name_flag to true
                for productname in item.find_all('div', {'class': 'product-name'}):
                    the_name = productname.find('a', {'class', 'name-link'}).text
                    if the_name == self.itemName:
                        name_flag = True
                # This executes when the item has been found so the color can be selected
                if name_flag:
                    # This loops through the styles and checks if the color is correct
                    for productStyle in item.find_all('div', {'class': 'product-style'}):
                        color = productStyle.find('a', {'class', 'name-link'}).text
                        # If the color is correct the url is saved and the search returns true
                        if color == self.itemColor:
                            a = productStyle.find('a')
                            global productUrl
                            productUrl = (baseUrl + '/' + a['href'])
                            return True
        return False

    # This adds product to cart and leaves browser on checkout page
    def add_product(self):
        # This opens the found URL
        self.browser.get(productUrl)
        # This selects the items size
        select = Select(self.browser.find_element_by_id('s'))
        select.select_by_visible_text(self.itemSize)
        # This adds the item to the shopping cart
        addbutton = self.browser.find_element_by_xpath('//*[@id="add-remove-buttons"]/input')
        addbutton.click()
        # This moves to the check out page
        checkoutbutton = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                                           '//*[@id="cart"]/a[2]')))
        checkoutbutton.click()

    # Completes check out information leaving CAPTCHA and terms for user
    def checkout(self):
        # Sets name field
        namefield = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID, 'order_billing_name')))
        namefield.send_keys(self.name)
        # Sets email field
        emailfield = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID, 'order_email')))
        emailfield.send_keys(self.email)
        # Sets telephone field
        telefield = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID, 'order_tel')))
        telefield.send_keys(self.tele)
        # Sets address field
        addressfield = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID, 'bo')))
        addressfield.send_keys(self.address)
        # Sets zip field
        zipfield = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID, 'order_billing_zip')))
        zipfield.send_keys(self.zip)
        # Sets city field
        cityfield = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID, 'order_billing_city')))
        cityfield.send_keys(self.city)
        # Sets state field
        selectstate = Select(
            WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID, 'order_billing_state'))))
        selectstate.select_by_visible_text(self.state)
        # Sets country field
        selectcountry = Select(
            WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID, 'order_billing_country'))))
        selectcountry.select_by_visible_text(self.country)
        # Sets credit card number field
        ccnfield = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID, 'rnsnckrn')))
        ccnfield.send_keys(self.ccn)
        # Sets expiration month field for credit card
        selectexpmonth = Select(
            WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID, 'credit_card_month'))))
        selectexpmonth.select_by_visible_text(self.ccem)
        # Sets expiration year field for credit card
        selectexpyear = Select(
            WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID, 'credit_card_year'))))
        selectexpyear.select_by_visible_text(self.ccey)
        # Sets security code for credit card
        securityfield = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID, 'orcer')))
        securityfield.send_keys(self.cvv)

    # Initializes all variables needed from dictionary provided by GUI info
    def __init__(self, kwargs):
        self.keydict = kwargs
        self.browser = webdriver.Safari()
        self.name = self.keydict.get('name')
        self.email = self.keydict.get('email')
        self.tele = self.keydict.get('tele')
        self.address = self.keydict.get('address')
        self.zip = self.keydict.get('zip')
        self.city = self.keydict.get('city').lower().capitalize()
        self.state = self.keydict.get('state').upper()
        self.country = self.keydict.get('country')
        self.ccn = self.keydict.get('ccn')
        self.ccem = self.keydict.get('ccem')
        self.ccey = self.keydict.get('ccey')
        self.cvv = self.keydict.get('cvv')
        self.itemSize = self.keydict.get('itemSize').lower().capitalize()
        self.itemColor = self.keydict.get('itemColor')
        self.itemName = self.keydict.get('itemName')
        self.itemCategory = self.keydict.get('itemCategory')
        self.itemCategory = self.itemCategory.lower()
