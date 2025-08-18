from test_utils.conftest import *
from playwright.sync_api import expect, Page
import time
import pytest

test_name = None

@pytest.mark.skip
def test_login(test_open_browser, request):
    page = test_open_browser
    global test_name
    test_name = request.node.name
    expect(page.get_by_placeholder("Username")).to_be_visible(timeout=10000)
    save_screenshot(page, test_name, "login_page")
    page.get_by_placeholder("Username").type("Admin")
    page.get_by_placeholder("Password").fill("nagaraju99@")
    text = page.get_by_role("button", name="Login").text_content()
    print("The Text of the Button is : ",text)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="HR Administration")).to_be_visible(timeout=10000)
    time.sleep(2)

@pytest.mark.skip
def test_HR_Admin(test_open_browser):
    page = test_open_browser
    text = page.locator("a.name").text_content()
    print("\nThe HR Manager Name is : ",text)
    expect(page.get_by_role("link", name="HR Administration")).to_be_visible(timeout=10000)
    page.get_by_role("link", name="HR Administration").click()
    save_screenshot(page, test_name, "HR_Administration")

@pytest.mark.skip
def test_Add_User_HR_Admin(test_open_browser):
    page = test_open_browser
    page.wait_for_load_state("networkidle")
    expect(page.locator("//div[@data-tooltip='Add User']")).to_be_visible(timeout=10000)
    page.locator("//div[@data-tooltip='Add User']").click()
    save_screenshot(page, test_name, "Add_User_HR_Admin")
    expect(page.get_by_placeholder("Enter Password")).to_be_visible(timeout=10000)
    save_screenshot(page, test_name, "Add_User_HR_Admin_popup")
    page.get_by_role()

@pytest.mark.launch
def test_rahul_shetty_login(test_open_browser, request):
    global test_name
    test_name = request.node.name
    page = test_open_browser
    expect(page.get_by_label("username")).to_be_visible(timeout=10000)
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox").check()
    page.locator("#signInBtn").click()
    time.sleep(2)
    expect(page.locator('//h1[text()="Shop Name"]')).to_be_visible(timeout=10000)
    time.sleep(2)
    page.evaluate("window.scrollBy(0, 1000)")
    page.locator("//p[text()='Copyright © ProtoCommerce 2018']").scroll_into_view_if_needed()
    time.sleep(2)
    page.locator('//h1[normalize-space()="Shop Name"]').scroll_into_view_if_needed()
    time.sleep(2)


@pytest.mark.skip
def test_scrollup_scrolldown_based_on_locator(test_open_browser):
    page = test_open_browser
    page.locator("//a[normalize-space()='Medianh Consulting']").scroll_into_view_if_needed()
    time.sleep(2)
    page.locator("//h1[normalize-space()='Practice Page']").scroll_into_view_if_needed()
    time.sleep(2)

@pytest.mark.skip
def test_child_page_validation(test_open_browser):
    page = test_open_browser
    with page.expect_popup() as new_page_tab:
        page.locator(".blinkingText").click()
        new_page = new_page_tab.value
        ste = new_page.locator(".red").text_content()
        print(f"\nComplete Text from UI : {ste}")
        ste = ((ste.split("at"))[1].split(" "))[1]
        print(f"The Email is : {ste} \n")
        assert ste == "mentor@rahulshettyacademy.com"
        