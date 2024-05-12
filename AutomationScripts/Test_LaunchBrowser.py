import allure_pytest.listener
import pytest
from selenium import webdriver


class LaunchBrowser ( object ) :
    def choosebrowser ( Str ) :
        # Beginning of the condition to choose browser for execution
        if Str == "Chrome" :
            # Need to import Chrome Driver as a service
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager

            driver1 = webdriver.Chrome ( service = Service ( ChromeDriverManager ( ).install ( ) ) )
            Link = "http://www.google.com"
            driver1.get ( Link )
            print ( "The opened browser link is" + " " + Link )
            driver1.close ( )

        elif Str == "Firefox" :
            # No need to import as a Service for Firefox
            Link = "http://www.google.com"
            webdriver.Firefox ( ).get ( Link )
            print ( "The opened browser link is" + " " + Link )
            webdriver.Firefox.close ( )
        else :
            print ( "No browser entered" )


def test_first () :
    LaunchBrowser.choosebrowser ( Str = "Chrome" )
    pytest.TestShortLogReport
    pytest.TestReport


def test_Second () :
    LaunchBrowser.choosebrowser ( Str = "Chrome" )
    pytest.TestShortLogReport
    pytest.TestReport


def test_Third () :
    LaunchBrowser.choosebrowser ( Str = "Chrome" )
    pytest.TestShortLogReport
    pytest.TestReport


def test_Four () :
    LaunchBrowser.choosebrowser ( Str = "Chrome" )
    pytest.TestShortLogReport
    pytest.TestReport


def test_Five () :
    LaunchBrowser.choosebrowser ( Str = "Chrome" )
    pytest.TestShortLogReport
    pytest.TestReport


def test_Six () :
    LaunchBrowser.choosebrowser ( Str = "Chrome" )
    pytest.TestShortLogReport
    pytest.TestReport
