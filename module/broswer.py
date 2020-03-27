# coding=utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Driver(object):
    def __init__(self, is_mobile=False):
        if is_mobile:
            mobileEmulation = {'deviceName': 'iPhone 8'}
            desired = DesiredCapabilities.CHROME
            desired['loggingPrefs'] = {'performance': 'ALL'}
            options = webdriver.ChromeOptions()
            options.add_experimental_option('mobileEmulation', mobileEmulation)
            self.driver = webdriver.Chrome(chrome_options=options, desired_capabilities=desired)
        else:
            self.driver = webdriver.Chrome()

    def get_item(self, kind, selector):
        try:
            item = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((kind, selector)))
        except Exception as ex:
            import traceback
            traceback.print_exc()
            return None
        return item

    def open_page(self, url):
        self.driver.get(url)

    def click_btn(self, kind, selector):
        item = self.get_item(kind, selector)
        if not item:
            return False
        self.driver.execute_script('arguments[0].click();', item)
        return True

    def input_value(self, kind, selector, value):
        item = self.get_item(kind, selector)
        if not item:
            return False
        item.clear()
        item.send_keys(value)
        return True

    def get_text(self, kind, selector):
        item = self.get_item(kind,selector)
        if not item:
            return None
        return item.text

    def get_attr(self, kind, selector, attr):
        item = self.get_item(kind, selector)
        if not item:
            return None
        return item.get_attribute(attr)

    def __del__(self):
        self.driver.close()
