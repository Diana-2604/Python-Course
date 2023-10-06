import logging
import time

import yaml
from testpage import OperationsHelper
from os import getcwd

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info('Test1 Starting - Login invalid')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401', 'test1 failed'


def test_step2(browser):
    logging.info('Test2 Starting - Login valid')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['username'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    assert testpage.get_login_text() == f'Hello, {testdata["username"]}', 'test2 failed'

def test_step3(browser):
    logging.info('Test3 Starting - Open About page')
    testpage = OperationsHelper(browser)
    testpage.click_about_button()
    
    time.sleep(2)

    assert testpage.get_about_title_text() == "About Page", 'Неверный заголовок страницы'

def test_step4(browser):
    logging.info('Test3 Starting - Inspect title')
    testpage = OperationsHelper(browser)
    testpage.click_about_button()
    
    time.sleep(2)

    assert testpage.get_about_title_font_size() == "32px", 'Размер шрифта заголовка не равен 32px'


# def test_step4(browser):
#     logging.info('Test4 Starting')
#     testpage = OperationsHelper(browser)
#     testpage.click_home_step1_btn()
#     testpage.click_home_step2_btn()
#     testpage.click_create_post_btn()
#     time.sleep(1)
#     testpage.enter_post_title(testdata['test_title'])
#     testpage.enter_post_description(testdata['test_description'])
#     testpage.enter_post_content(testdata['test_content'])
#     testpage.click_save_btn()
#     time.sleep(2)
#     assert testpage.get_added_post_title() == testdata['test_title'], 'test4 failed'

