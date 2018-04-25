# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators(object):
    FIRST_FARE_BUTTON       = (By.XPATH,      "(//div[contains(@class,'flight-header__min-price')]/*//span[contains(text(),'from')])[1]")
    STANDARD_FARE_BUTTON    = (By.XPATH,      "//div[contains(@class,'flights-table-fares__fare') and contains(@class,'standard')]")
    CONTINUE_BUTTON         = (By.ID,         'continue')
    NO_SEAT_BUTTON          = (By.XPATH,      "//div[@class='footer-message-content__buttons']/button[contains(@class,'core-btn-link')]")
    CHECKOUT_BUTTON         = (By.XPATH,      "//div[@class='extras-panel__button-wrapper']/button")
#    CHECKOUT_BUTTON         = (By.XPATH,      "//div[@class='trips-basket trips-cnt']/button")
    BAGSCLOSE_BUTTON        = (By.CLASS_NAME, 'popup-msg__close')


class FaresPage(object):

    def __init__(self,context):
        pass

    def init_page_elements(self, context):
        context.page.firstFare_button = context.driver.find_element(*Locators.FIRST_FARE_BUTTON)
        WebDriverWait(context.driver, 10).until(EC.visibility_of(context.page.firstFare_button))

    def extended_1_page_elements(self, context):
        context.page.standardFare_button = context.driver.find_element(*Locators.STANDARD_FARE_BUTTON)
        WebDriverWait(context.driver, 10).until(EC.visibility_of(context.page.standardFare_button))

    def extended_2_page_elements(self, context):
        context.page.continue_button = context.driver.find_element(*Locators.CONTINUE_BUTTON)
        WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'continue')))

    def extended_3_page_elements(self, context):
        context.page.checkout_button = context.driver.find_element(*Locators.CHECKOUT_BUTTON)
        WebDriverWait(context.driver, 10).until(EC.visibility_of(context.page.checkout_button))
        context.page.noSeat_button = context.driver.find_element(*Locators.NO_SEAT_BUTTON)
        WebDriverWait(context.driver, 10).until(EC.visibility_of(context.page.noSeat_button))

    def extended_4_page_elements(self, context):
        context.page.bagsClose_button = context.driver.find_element(*Locators.BAGSCLOSE_BUTTON)
        WebDriverWait(context.driver, 10).until(EC.visibility_of(context.page.bagsClose_button))
