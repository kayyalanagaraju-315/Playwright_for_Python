import time

import pytest
import os
from datetime import datetime


_cleaned_folders = set()
screenshot_counter = {}

@pytest.fixture(scope="session")
def launch_browser(playwright):
    browser = playwright.chromium.launch(
        headless=False,
        args=[
            "--start-maximized",            # Maximizes the window
            "--force-device-scale-factor=.90",  # Sets scale factor
            # "--fast-start",
            # "--incognito"
        ],
          # Ensures it uses actual Chrome, not Chromium
    )
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    tc_start_time = datetime.now().time()
    tc_start_time = tc_start_time.strftime("%H:%M:%S")
    print("\ntest_functionality Case Start Time:", tc_start_time)
    yield page
    tc_end_time = datetime.now().time()
    tc_end_time = tc_end_time.strftime("%H:%M:%S")
    print("\ntest_functionality Case End Time:", tc_end_time)
    start_time = datetime.strptime(tc_start_time, "%H:%M:%S")
    end_time = datetime.strptime(tc_end_time, "%H:%M:%S")
    execution_time = end_time - start_time
    print("\ntest_functionality Case Execution Time:", execution_time)

@pytest.fixture(scope="session")
def test_open_browser(launch_browser):
    page = launch_browser
    # page.goto("https://nagarajukayyala-trials7161.orangehrmlive.com")
    # page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # page.goto("https://qaportal.vilpower.in/")
    return page



def save_screenshot(page, test_name, screenshot_name):
    # Base path: ./Results/<test_name>/
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    screenshot_dir = os.path.join(base_dir, "Results", test_name)

    # Clear .png files once per test_name
    if test_name not in _cleaned_folders:
        if os.path.exists(screenshot_dir):
            for file in os.listdir(screenshot_dir):
                if file.endswith(".png"):
                    os.remove(os.path.join(screenshot_dir, file))
        else:
            os.makedirs(screenshot_dir)
        _cleaned_folders.add(test_name)
    else:
        os.makedirs(screenshot_dir, exist_ok=True)

    count = screenshot_counter.get(test_name, 0) + 1
    screenshot_counter[test_name] = count

    # Save new screenshot with timestamp
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    filename = f"{count}_{screenshot_name}_{timestamp}.png"
    path = os.path.join(screenshot_dir, filename)
    page.screenshot(path=path)
    # print(f"✅ Screenshot saved to: {path}")

