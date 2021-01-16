from utils.Setup import Setup
from poms.HomePage import HomePage


def main():
    setup = Setup()
    driver = setup.get_driver()
    homePage = HomePage(driver)

    try:
        homePage.navigate_to_this_page()
        homePage.click_get_started_button()
        homePage.click_spanish_card()
        homePage.click_family_card()
        homePage.click_continue_button()
        homePage.click_intense_option()
        homePage.click_continue_button()
        homePage.click_create_profile_button()
        homePage.fill_create_profile_form()
    except:
        print('Something went wrong!')
    finally:
        print('Closing driver...')
        driver.close()


if __name__ == "__main__":
    main()
