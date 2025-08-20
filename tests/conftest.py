from selenium import webdriver
import yaml
import os
import pytest
from utils.yaml_reader import read_yaml
import allure
import os
import pytest



def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="Environment: dev/stage/prod"
    )


@pytest.fixture(scope="session")
def config(pytestconfig):
    """Load config.yaml dynamically based on --env option"""
    env = pytestconfig.getoption("env")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "config", f"config_{env}.yaml")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")

    return read_yaml(config_path)


@pytest.fixture(scope= "function")
def driver_setup(config):
    browser = config.get("browser").lower()
    driver = None
    if browser =='chrome':  
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        
    elif browser =='firefox':  
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
      
    elif browser =='edge':  
        options = webdriver.EdgeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
     
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    
    yield driver

    driver.quit()

# ...........  ()()()()()()()()()()()()()
# Hook to take screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only add screenshot for failed test calls
    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name=f"screenshot_{item.name}",
                attachment_type=allure.attachment_type.PNG
            )