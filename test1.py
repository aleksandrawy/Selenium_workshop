from selenium.webdriver import Ie
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def test_selenium():
    caps = DesiredCapabilities.INTERNETEXPLORER
    caps['nativeEvents'] = False #zeby przyspieszyc wpisywanie
    driver = Ie(capabilities=caps)
    driver.get('http://www.worldshop.eu')
   # driver.implicitly_wait() #czekanie w sekundach
    search_text_box = driver.find_element_by_name('term')
    search_text_box.send_keys('t-shirt')
    search_button = driver.find_element_by_name('searchButton')
    search_button.click()
    total_text = driver.find_element_by_xpath('.//div[@class="ProductNumber"]/span')
    print(total_text.text)


test_selenium()