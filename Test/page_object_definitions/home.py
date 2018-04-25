# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Locators(object):
    FLIGHTS_TAB         = (By.CLASS_NAME, 'flights-tab')
    ONEWAY_RADIO        = (By.ID,         'lbl-flight-search-type-one-way')
    DEPARTURE_INPUT     = (By.XPATH,      "//input[@placeholder='Departure airport']")
    DESTINATION_INPUT   = (By.XPATH,      "//input[@placeholder='Destination airport']")
    CONTINUE_BUTTON     = (By.XPATH,      "//div[@class='col-flight-search-right']/button[1]")

    ONEWAY_DD_INPUT     = (By.XPATH,      "//input[@aria-label='Fly out: - DD']")
    ONEWAY_MM_INPUT     = (By.XPATH,      "//input[@aria-label='Fly out: - MM']")
    ONEWAY_YYYY_INPUT   = (By.XPATH,      "//input[@aria-label='Fly out: - YYYY']")
    STARTDAY_DD_INPUT   = (By.XPATH,      "//input[@aria-label='Fly out: - DD']")
    STARTDAY_MM_INPUT   = (By.XPATH,      "//input[@aria-label='Fly out: - MM']")
    STARTDAY_YYYY_INPUT = (By.XPATH,      "//input[@aria-label='Fly out: - YYYY']")
    BACKDAY_DD_INPUT    = (By.XPATH,      "//input[@aria-label='Fly back: - DD']")
    BACKDAY_MM_INPUT    = (By.XPATH,      "//input[@aria-label='Fly back: - MM']")
    BACKDAY_YYYY_INPUT  = (By.XPATH,      "//input[@aria-label='Fly back: - YYYY']")
    TERMS_CHECK         = (By.CLASS_NAME, 'terms-conditions-checkbox-span')
    LETSGO_BUTTON       = (By.XPATH,      "//div[@class='col-flight-search-right']/button[2]")


class HomePage(object):

    def __init__(self,context):
        pass

    def init_page_elements(self, context):
        context.page.flights_tab = context.driver.find_element(*Locators.FLIGHTS_TAB)
        context.page.oneWay_radio = context.driver.find_element(*Locators.ONEWAY_RADIO)
        context.page.departure_input = context.driver.find_element(*Locators.DEPARTURE_INPUT)
        context.page.destination_input = context.driver.find_element(*Locators.DESTINATION_INPUT)
        context.page.continue_button = context.driver.find_element(*Locators.CONTINUE_BUTTON)
        WebDriverWait(context.driver, 10).until(EC.visibility_of(context.page.destination_input))

    def extended_page_elements(self, context):
        context.page.onewayDayDD_input = context.driver.find_element(*Locators.ONEWAY_DD_INPUT)
        context.page.onewayDayMM_input = context.driver.find_element(*Locators.ONEWAY_MM_INPUT)
        context.page.onewayDayYYYY_input = context.driver.find_element(*Locators.ONEWAY_YYYY_INPUT)
        context.page.startDayDD_input = context.driver.find_element(*Locators.STARTDAY_DD_INPUT)
        context.page.startDayMM_input = context.driver.find_element(*Locators.STARTDAY_MM_INPUT)
        context.page.startDayYYYY_input = context.driver.find_element(*Locators.STARTDAY_YYYY_INPUT)
        context.page.backDayDD_input = context.driver.find_element(*Locators.BACKDAY_DD_INPUT)
        context.page.backDayMM_input = context.driver.find_element(*Locators.BACKDAY_MM_INPUT)
        context.page.backDayYYYY_input = context.driver.find_element(*Locators.BACKDAY_YYYY_INPUT)
        context.page.terms_check = context.driver.find_element(*Locators.TERMS_CHECK)
        context.page.letsgo_button = context.driver.find_element(*Locators.LETSGO_BUTTON)
        WebDriverWait(context.driver, 10).until(EC.visibility_of(context.page.letsgo_button))
