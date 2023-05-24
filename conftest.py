import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='Chrome', help='Choose the browser for tests from the list in the following format: \nChrome \nFirefox\n-----\nDefault browser is Chrome.')
    parser.addoption('--language', action='store', default='en', help='Choose a language from the list in the following format: \nen\nru\nes\nfr\n-----\nDefault language is English (en).\n')

def browser_setup(browser_name, user_language):
    if browser_name == 'Chrome':
        user_options = Options()
        user_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        return webdriver.Chrome(options=user_options)
    elif browser_name == 'Firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        return webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser should be either Chrome of Firefox')

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('browser')
    user_language = request.config.getoption('language')
    browser = browser_setup(browser_name, user_language)

    print(f'\nBooting up {browser_name}...')
    
    yield browser
    
    print(f'\nClosing {browser_name}...')
    browser.quit()