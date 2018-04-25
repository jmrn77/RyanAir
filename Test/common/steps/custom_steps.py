# -*- coding: utf-8 -*-

from behave import step, given, when, then
from page_object_definitions.home import HomePage


@step('I navigate to "{resource}"')
def navigate_url(context, resource):
    context.driver.get(context.data['Pages'][resource]['url'])
    context.driver.maximize_window()
    exec ('context.page = {}(context)'.format(resource))
    context.page.init_page_elements(context)

