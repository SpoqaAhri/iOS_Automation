import unittest
from appium.webdriver import webdriver
from appium import webdriver


class ConfigSet(unittest.TestCase):

    def testConfig(content):
        desiredCaps = {
            "platformName": "iOS",
            "appium:platformVersion": "14.6",
            "appium:deviceName": "iPhone12ProMax",
            "appium:udid": "00008101-001E6C411A11001E",
            "appium:bundleId": "com.spoqa.dodocart.qa",
            "appium:noReset": "false",
            "appium:usePrebuiltWDA": "true",
            "appium:wdaBaseUrl": "http://169.254.43.42:8100",
            "appium:xcodeSigningId": "iPhone Developer"
        }
        content.driver = webdriver.Remote(f'http://127.0.0.1:4001/wd/hub', desiredCaps)

