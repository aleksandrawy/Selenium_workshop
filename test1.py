from selenium.webdriver import Ie
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


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
    match = re.search('\d+', total_text.text)
    #print(match.group())
    assert int(match.group()) == 95

    choose_tshirt =  driver.find_element_by_xpath('.//img[@title="Hugo Boss, Herren T-Shirt, Teeos, Medium Grey"]')
    choose_tshirt.click()

    choose_size = driver.find_element_by_class_name('arrow_btn')
    choose_size.click()

    size_selectbox = Select(driver.find_element_by_name('variantChooser:variantChooserSelect'))
    size_selectbox.select_by_visible_text('XXL')

    #WebDriverWait(driver, timeout=5).until(EC.element_to_be_clickable((By.XPATH, './/a/span[text()="Add to shopping cart"]')))
    # add_to_cart = driver.find_element_by_xpath('.//a/span[text()="Add to shopping cart"]')  #[@class="AddToCartLink"]')
    WebDriverWait(driver, timeout=5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'AddToCartLink')))
    add_to_cart = driver.find_element_by_class_name('AddToCartLink')
    add_to_cart.click()

    WebDriverWait(driver, timeout=5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'CartMessageBox')))
    pop_up = driver.find_element_by_class_name('CartMessageBox')

    assert pop_up.is_displayed()

    continue_button = driver.find_element_by_xpath('.//img[@src="/medias/sys_master/button_en_primary_cockpit_localized-global-buy-moreHD_mw164.png?1476853411000"]')
    continue_button.click()

    amount = driver.find_element_by_class_name('Quantity')
    assert int(amount.text) == 1

    price1 = driver.find_element_by_class_name('PriceCashValue')
    price2 = driver.find_element_by_xpath('.//div[@class="Total"]/ol/li[1]/span[@class="Value"]')
    match_price1 = re.search('\d+', price1.text)
    match_price2 = re.search('\d+', price2.text)
    assert int(match_price1.group()) == int(match_price2.group())

    
#test_selenium()