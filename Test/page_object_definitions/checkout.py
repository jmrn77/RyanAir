# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators(object):
    TITLE_SELECT          = (By.XPATH,      "//div[@class='pax-form-element'][1]/*//select")
    FIRSTNAME_INPUT       = (By.XPATH,      "//input[contains(@id, 'firstName')]")
    SURNAME_INPUT         = (By.XPATH,      "//input[contains(@id, 'lastName')]")

    PHONECOUNTRY_SELECT   = (By.XPATH,      "//select[contains(@class, 'phone-number-country--select')]")
    PHONENUMBER_INPUT     = (By.XPATH,      "//div[@class='phone-number']/input")

    METHOD_RADIO          = (By.ID,         'CC')
    CARDNUMBER_INPUT      = (By.NAME,       'cardNumber')
    CARDTYPE_SELECT       = (By.NAME,       'cardType')
    EXPIRYMONTH_SELECT    = (By.NAME,       'expiryMonth')
    EXPIRYYEAR_SELECT     = (By.NAME,       'expiryYear')
    SECURITYCODE_INPUT    = (By.NAME,       'securityCode')
    HOLDERNAME_INPUT      = (By.NAME,       'cardHolderName')

    ADDRESSLINE1_INPUT    = (By.ID,         'billingAddressAddressLine1')
    ADDRESSLINE2_INPUT    = (By.ID,         'billingAddressAddressLine2')
    CITY_INPUT            = (By.ID,         'billingAddressCity')
    POSTCODE_INPUT        = (By.ID,         'billingAddressPostcode')
    ADDRESSCOUNTRY_SELECT = (By.ID,         'billingAddressCountry')

    TERMS_CHECK           = (By.XPATH,      "//div[@class='cta']/*/label")
    PAYNOW_BUTTON         = (By.XPATH,      "//div[@class='cta']/button")

    ERROR_TITLE_TEXT      = (By.CLASS_NAME, 'info-title')
    ERROR_DESC_TEXT       = (By.XPATH,      "//*[contains(@class, 'error')]/div[@class='info-text']/span")


class CheckoutPage(object):

    def __init__(self,context):
        pass

    def init_page_elements(self, context):
        context.page.title_select = context.driver.find_element(*Locators.TITLE_SELECT)
        context.page.firstName_input = context.driver.find_element(*Locators.FIRSTNAME_INPUT)
        context.page.surname_input = context.driver.find_element(*Locators.SURNAME_INPUT)
        WebDriverWait(context.driver, 10).until(EC.visibility_of(context.page.title_select))

    def extended1_page_elements(self, context):
        self.scroll_to_top(context)
        context.page.phoneCountry_select = context.driver.find_element(*Locators.PHONECOUNTRY_SELECT)
        context.page.phoneNumber_input = context.driver.find_element(*Locators.PHONENUMBER_INPUT)
        WebDriverWait(context.driver, 10).until(EC.visibility_of(context.page.phoneCountry_select))

    def extended2_page_elements(self, context):
        self.scroll_to_top(context)
        context.page.method_radio = context.driver.find_element(*Locators.METHOD_RADIO)
        context.page.cardNumber_input = context.driver.find_element(*Locators.CARDNUMBER_INPUT)
        context.page.cardType_select = context.driver.find_element(*Locators.CARDTYPE_SELECT)
        context.page.expiryMonth_select = context.driver.find_element(*Locators.EXPIRYMONTH_SELECT)
        context.page.expiryYear_select = context.driver.find_element(*Locators.EXPIRYYEAR_SELECT)
        context.page.securityCode_input = context.driver.find_element(*Locators.SECURITYCODE_INPUT)
        context.page.holderName_input = context.driver.find_element(*Locators.HOLDERNAME_INPUT)
        WebDriverWait(context.driver, 10).until(EC.visibility_of(context.page.cardType_select))

    def extended3_page_elements(self, context):
        self.scroll_to_top(context)
        context.page.addressLine1_input = context.driver.find_element(*Locators.ADDRESSLINE1_INPUT)
        context.page.addressLine2_input = context.driver.find_element(*Locators.ADDRESSLINE2_INPUT)
        context.page.city_input = context.driver.find_element(*Locators.CITY_INPUT)
        context.page.postCode_input = context.driver.find_element(*Locators.POSTCODE_INPUT)
        context.page.addressCountry_select = context.driver.find_element(*Locators.ADDRESSCOUNTRY_SELECT)
        context.page.terms_check = context.driver.find_element(*Locators.TERMS_CHECK)
        context.page.payNow_button = context.driver.find_element(*Locators.PAYNOW_BUTTON)
        WebDriverWait(context.driver, 10).until(EC.visibility_of(context.page.addressCountry_select))

    def extendedError_page_elements(self, context):
        context.page.errorTitle_text = context.driver.find_element(*Locators.ERROR_TITLE_TEXT)
        WebDriverWait(context.driver, 10).until(EC.visibility_of(context.page.errorTitle_text))
        context.page.errorDesc_text = context.driver.find_element(*Locators.ERROR_DESC_TEXT)
        WebDriverWait(context.driver, 10).until(EC.visibility_of(context.page.errorDesc_text))

    def scroll_to_top(self, context):
        context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
