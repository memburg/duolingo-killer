import sys
from utils.Setup import Setup
from poms.HomePage import HomePage


def main():
    setup = Setup()
    driver = setup.get_driver()
    homePage = HomePage(driver)

    try:
        homePage.navigate_to_this_page()
        homePage.click_get_started_button()
    except:
        print('Something went wrong!', sys.exc_info()[0])
    finally:
        print('Closing driver...')
        driver.close()


if __name__ == "__main__":
    main()
