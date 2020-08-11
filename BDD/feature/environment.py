from selenium import webdriver
import json

from tasks.setUpDriver import Initiate


def before_all(context):
    with open("configuartionFiles/config.json") as config_file:
        data = json.load(config_file)

    if data['browser'] == "Chrome":
        url = data["url"]
        driver = Initiate.tear_up(url)
        context.driver = driver
    else:
        print("select a browser")


def after_all(context):
    Initiate.tear_down(context.driver)

