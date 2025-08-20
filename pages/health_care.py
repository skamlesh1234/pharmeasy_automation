from selenium.webdriver.common.by import By

class Health_care:

    # Selects all h2 inside <a role="button">
    card_titles = (By.CSS_SELECTOR, "a[role='button'] h2")

    def __init__(self, driver):
        self.driver = driver

    def get_card_title(self, card_name):
        # Use correct locator
        card_elements = self.driver.find_elements(*self.card_titles)
        for card in card_elements:
            if card_name.lower() in card.text.lower():
                return card.text
        return None

    def click_card(self, card_name):
        cards = self.driver.find_elements(*self.card_titles)
        for card in cards:
            if card_name.lower() in card.text.lower():
                card.click()
                return
        raise Exception(f"Card with name '{card_name}' not found.")
