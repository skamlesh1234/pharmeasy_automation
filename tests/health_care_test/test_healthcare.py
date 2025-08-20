from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.health_care import Health_care

def test_check_title_by_name(driver_setup):

    try:
        driver= driver_setup
        driver.get("https://pharmeasy.in/health-care")

        # Initialize the Page Object
        healthcare = Health_care(driver)

        # Act: Get title from card
        title = healthcare.get_card_title("monsoon store")

        # Assert: Make sure it exists
        assert title is not None, "Card title not found"
        print
        assert "monsoon" in title.lower(), f"Unexpected title: {title}"

        print("✅ Found card title:", title)

    except:
        print(Exception.with_traceback)




def test_check_no_of_cards(driver_setup):
    try:
        driver= driver_setup
        driver.get("https://pharmeasy.in/health-care")
        cards = driver.find_elements(By.CSS_SELECTOR,'a[role= button]')
        assert len(cards) ==16 ,f"card no. not matched expected 16 got {len(cards)}"
        print("✅ Found card length:", len(cards))
    except:
        print(Exception.with_traceback)
    
def test_cards_are_clickable_or_not(driver_setup):
    try:
        driver= driver_setup
        driver.get("https://pharmeasy.in/health-care")
        titles = driver.find_elements(By.CSS_SELECTOR,'a[role= button] h2')
        for title in titles:
            print(title.text)
    except:
        print(Exception.with_traceback)








        

