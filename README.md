# pharmeasy_automation
Pharmeasy_Aut0mati0n is a fully-fledged UI automation framework for the PharmEasy web platform. Built with Python, Selenium WebDriver, and pytest, and featuring Allure reports, this project ensures end-to-end test automation that’s scalable, maintainable, and CI/CD-ready.
# PharmEasy_Aut0mati0n

## Overview
Automation framework for testing the PharmEasy web application using Python, Selenium, pytest, and Allure reporting.

## Features
- Headless cross-browser testing (Chrome, Firefox, Edge)
- Environment-based configuration (`--env` flag)
- Screenshot, logs & page source attachments on test failure
- Clean test structure with Page Object Model
- Docker and CI/CD (Jenkins) ready

## Tech Stack
- Python 3.x
- Selenium
- pytest
- Allure
- PyYAML
- Docker (optional)
- Jenkins (optional)

## Project Structure
selenium_project/
├── config/
│ ├── config_dev.yaml
│ ├── config_stage.yaml
│ └── config_prod.yaml
├── pages/
├── tests/
├── utils/
├── reports/
│ ├── allure-results/
│ └── allure-report/
├── conftest.py
├── Dockerfile
├── pytest.ini
└── README.md
