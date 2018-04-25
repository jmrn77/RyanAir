# -*- coding: utf-8 -*-

from selenium import webdriver
from os import getcwd, path, makedirs, chdir
from datetime import *
import yaml


def before_all(context):
    with open(getcwd() + "/resources/data/data.yaml", 'r') as cfgfile:
        context.data = yaml.load(cfgfile)
    with open(getcwd() + "/resources/language/messages.yaml", 'r') as langfile:
        context.language = yaml.load(langfile)


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(getcwd() + '/resources/browser_drivers/chromedriver')
    context.driver.set_page_load_timeout(15)
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
        if scenario.status == "failed":
            screenshot_dir = getcwd() + "/_output/screenshots/" + scenario.name.replace(" ", "_")
            if not path.exists(screenshot_dir):
                makedirs(screenshot_dir)
            chdir(screenshot_dir)
            context.driver.save_screenshot(datetime.now().strftime('%Y%m%d-%H%M%S') + ".png")
            context.driver.quit()
