# -*- coding: utf-8 -*-

from behave import step

from page_object_definitions.fares import FaresPage
from page_object_definitions.login import LoginPage
from page_object_definitions.checkout import CheckoutPage

from datetime import datetime, timedelta
from selenium.webdriver.support.ui import Select

import time

def select_trip(context, departure, destination, date, duration=-1):
    if date == "today":
        start_date = datetime.now()
    elif date == "tomorrow":
        start_date = datetime.now() + timedelta(days=1)
    else:
        try:
            datetime.strptime(date, '%d/%m/%Y')
            start_date = datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            assert False, "Start date must be in format DD/MM/YYYY. Another valid values: 'today' and 'tomorrow'"

    context.page.flights_tab.click()

    one_way = False
    if duration < 0:
        one_way = True
        context.page.oneWay_radio.click()
    else:
        back_date = start_date + timedelta(days=duration)

    context.page.departure_input.clear()
    context.page.departure_input.send_keys(departure)
    context.page.destination_input.clear()
    context.page.destination_input.send_keys(destination)
    context.page.continue_button.click()
    context.page.extended_page_elements(context)
    if one_way:
        context.page.onewayDayDD_input.send_keys(start_date.day)
        context.page.onewayDayMM_input.clear()
        context.page.onewayDayMM_input.send_keys(start_date.month)
        context.page.onewayDayYYYY_input.clear()
        context.page.onewayDayYYYY_input.send_keys(start_date.year)
    else:
        context.page.startDayDD_input.send_keys(start_date.day)
        context.page.startDayyMM_input.clear()
        context.page.startDayMM_input.send_keys(start_date.month)
        context.page.startDayYYYY_input.clear()
        context.page.startDayYYYY_input.send_keys(start_date.year)
        context.page.backDayDD_input.send_keys(back_date.day)
        context.page.backDayMM_input.clear()
        context.page.backDayMM_input.send_keys(back_date.month)
        context.page.backDayYYYY_input.clear()
        context.page.backDayYYYY_input.send_keys(back_date.year)

    context.page.letsgo_button.click()


def select_fare(context):
    del context.page
    context.page = FaresPage(context)
    context.page.init_page_elements(context)
    context.page.firstFare_button.click()
    context.page.extended_1_page_elements(context)
    context.page.standardFare_button.click()
    context.page.extended_2_page_elements(context)
    context.page.continue_button.click()
    context.page.extended_3_page_elements(context)
    context.page.noSeat_button.click()
    time.sleep(3)
    context.page.checkout_button.click()
    try:
        context.page.extended_4_page_elements(context)
        if context.page.bagsClose_button.is_displayed():
            context.page.bagsClose_button.click()
    except:
        pass

def login(context, user):
    del context.page
    context.page = LoginPage(context)
    context.page.init_page_elements(context)
    if context.page.username_text.text == "Log in":
        context.page.username_button.click()
        context.page.extended_page_elements(context)
        context.page.email_input.send_keys(context.data['Users'][user]['email'])
        context.page.password_input.send_keys(context.data['Users'][user]['password'])
        context.page.login_button.click()


def checkout_cc(context, user, card):
    del context.page
    context.page = CheckoutPage(context)
    context.page.init_page_elements(context)

    time.sleep(2)
    Select(context.page.title_select).select_by_visible_text(context.data['Users'][user]['title'])
    context.page.firstName_input.send_keys(context.data['Users'][user]['name'])
    context.page.surname_input.send_keys(context.data['Users'][user]['surname'])

    context.page.extended1_page_elements(context)
    Select(context.page.phoneCountry_select).select_by_visible_text(context.data['Users'][user]['phone']['country'])
    context.page.phoneNumber_input.send_keys(context.data['Users'][user]['phone']['number'])

    context.page.extended2_page_elements(context)
    context.page.method_radio.click()
    context.page.cardNumber_input.send_keys(context.data['Users'][user]['cards'][card]['number'])
    Select(context.page.cardType_select).select_by_visible_text(context.data['Users'][user]['cards'][card]['type'])
    Select(context.page.cardType_select).select_by_visible_text(context.data['Users'][user]['cards'][card]['type'])
    Select(context.page.expiryMonth_select).select_by_visible_text(str(context.data['Users'][user]['cards'][card]['expiry']['month']))
    Select(context.page.expiryYear_select).select_by_visible_text('20' + str(context.data['Users'][user]['cards'][card]['expiry']['year']))
    context.page.securityCode_input.send_keys(context.data['Users'][user]['cards'][card]['securityCode'])
    context.page.holderName_input.send_keys(context.data['Users'][user]['cards'][card]['name'])

    context.page.extended3_page_elements(context)
    context.page.addressLine1_input.send_keys(context.data['Users'][user]['adresses']['main']['line1'])
    context.page.city_input.send_keys(context.data['Users'][user]['adresses']['main']['city'])
    context.page.postCode_input.send_keys(context.data['Users'][user]['adresses']['main']['postCode'])
    Select(context.page.addressCountry_select).select_by_visible_text(context.data['Users'][user]['adresses']['main']['country'])

    if not context.page.terms_check.is_selected():
        context.page.terms_check.click()
    context.page.payNow_button.click()


@step(u'I make a booking from "{departure}" to "{destination}" for {date}')
@step(u'I make a booking from "{departure}" to "{destination}" from {date} by {duration:d} days')
def make_booking(context, departure, destination, date, duration=-1):
    select_trip(context, departure, destination, date, duration)
    select_fare(context)


@step(u'I pay for booking with data of "{user}" and credit card "{card}"')
def checkout_creditcard(context, user, card):
    login(context, user)
    checkout_cc(context, user, card)


@step(u'I should get "{message}" message')
def get_message(context, message):
    context.page.extendedError_page_elements(context)
    if message == "payment declined":
        assert context.page.errorTitle_text.text == context.language['Messages'][message]['title']['en'], \
            """Expected value: {expected}
               Given value: {given}""".format(expected=context.language['Messages'][message]['title']['en'],
                                              given=context.page.errorTitle_text.text)
        assert context.page.errorDesc_text.text == context.language['Messages'][message]['description']['en'], \
            """Expected value: {expected}
               Given value: {given}""".format(expected = context.language['Messages'][message]['description']['en'],
                                              given = context.page.errorDesc_text.text)
