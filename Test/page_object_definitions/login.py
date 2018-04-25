# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Locators(object):
    USERNAME_TEXT   = (By.XPATH, "//li[@id='myryanair-auth-login']/*/span" )
    USERNAME_BUTTON = (By.XPATH, "//button[@ui-sref='login']"              )
    EMAIL_INPUT     = (By.XPATH, "//input[@name='emailAddress']"           )
    PASSWORD_INPUT  = (By.XPATH, "//input[@name='password'][1]"            )
    LOGIN_BUTTON    = (By.XPATH, "//button[@type='submit'][1]"             )


class LoginPage(object):

    def __init__(self,context):
        pass

    def init_page_elements(self, context):
        context.page.username_text = context.driver.find_element(*Locators.USERNAME_TEXT)
        context.page.username_button = context.driver.find_element(*Locators.USERNAME_BUTTON)
        WebDriverWait(context.driver, 10).until(EC.visibility_of(context.page.username_button))

    def extended_page_elements(self, context):
        time.sleep(3)
        context.page.email_input = context.driver.find_elements(*Locators.EMAIL_INPUT)[1]
        context.page.password_input = context.driver.find_element(*Locators.PASSWORD_INPUT)
        context.page.login_button = context.driver.find_element(*Locators.LOGIN_BUTTON)
        WebDriverWait(context.driver, 10).until(EC.visibility_of(context.page.login_button))
