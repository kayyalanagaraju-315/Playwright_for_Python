from test_utils.conftest import *
from playwright.sync_api import expect
import time
import pytest


@pytest.mark.ui_valid
def test_UI_Validation(test_open_browser):
    page = test_open_browser
    page.locator("//a[normalize-space()='Medianh Consulting']").scroll_into_view_if_needed()
    time.sleep(1)
    page.locator("//h1[normalize-space()='Practice Page']").scroll_into_view_if_needed()
    time.sleep(1)
    page.locator('//input[@value="radio2"]').click()
    time.sleep(1)
    page.get_by_placeholder("Type to Select Countries").fill("India")
    time.sleep(2)
    page.locator("//div[normalize-space()='India']").click()
    time.sleep(1)
    page.get_by_role("combobox").select_option("option3")
    time.sleep(1)
    page.locator("#checkBoxOption2").check()
    time.sleep(1)
    with page.expect_popup() as new_page_tab:
        page.locator("#openwindow").click()
        new_page = new_page_tab.value
        ste = new_page.locator("//div[@class='cont']/span[contains(text(),'.com')]").text_content()
        print("\nNew Window Opened")
        print(f"Complete Text from UI New Window : {ste}")
        time.sleep(2)
        new_page.close()
        print("New Window Closed\n")
    time.sleep(2)
    expect(page.locator("#openwindow")).to_be_visible(timeout=5)
    print("\nBack to First Window\n")
    page.get_by_placeholder("Type to Select Countries").clear()
    page.get_by_placeholder("Type to Select Countries").fill("US")
    time.sleep(1)
    page.get_by_placeholder("Type to Select Countries").fill("US")
    time.sleep(2)
    page.locator("//div[normalize-space()='United States (USA)']").click()
    time.sleep(1)

    print("\n===============Handled JavaScript Here===============\n")
    page.on('dialog', lambda dialog: dialog.dismiss())
    page.locator("#confirmbtn").click()
    time.sleep(5)

    page.on('dialog', lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(5)

    page.on('dialog', lambda dialog: dialog.dismiss())
    page.get_by_role("button", name='Alert').click()
    time.sleep(5)
    print("\n===============Handled JavaScript END===============\n")

    with page.expect_popup() as new_page_tabs:
        page.get_by_role("link", name="Open Tab").click()
        new_page = new_page_tabs.value
        ste = new_page.locator('//div[@class="button float-left"]/a[@class="main-btn"]').text_content()
        print("\nNew Tab Opened")
        print(f"Complete Text from UI New Tab : {ste}")
        time.sleep(2)
        new_page.close()
        print("New Tab Closed\n")
    time.sleep(2)
    expect(page.locator("#openwindow")).to_be_visible(timeout=5)
    print("\nBack to First Tab\n")

    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    time.sleep(2)
    page.get_by_role("button", name="Hide").click()
    time.sleep(2)
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    print("Successfully Hidden")
    time.sleep(2)
    page.locator("#show-textbox").click()
    time.sleep(2)
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    print("Successfully Un-Hide")
    time.sleep(2)

    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").scroll_into_view_if_needed()
    time.sleep(4)
    pageFrame.locator("//div[@class='price-title']/h2").scroll_into_view_if_needed()
    time.sleep(5)

@pytest.mark.network_validation
def test_network_validation(test_open_browser):
    page = test_open_browser

    #Declared the empty list to append the OTP value
    otp_container = []
    # Attach network response listener early
    def log_response(response):
        if "check-credentials" in response.url:
            print(f"\n✅ Intercepted URL: {response.url}")
            print(f"Status Code: {response.status}")
            try:
                json_data = response.json()
                print("🧾 JSON Response:")
                print(json_data)
                otp_value = json_data.get('otp')
                print("Getting OTP From JSON Data is: ", otp_value, type(otp_value))
                otp_container.append(otp_value)
            except Exception as e:
                print("⚠️ Could not parse JSON:", e)
    page.on("response", log_response)

    # Simulate login flow
    page.locator('//a[text()="Login"]').scroll_into_view_if_needed()
    page.locator('//a[text()="Login"]').click()
    expect(page.locator('//a[@id="loginTypeCheck"]')).to_be_visible()
    page.locator('//a[@id="loginTypeCheck"]').click()
    page.locator('//input[@name="vcEmail"]').fill("testingtanla@yopmail.com")
    page.keyboard.press("Tab")
    page.locator('//input[@name="vcPassword"]').fill("Tanla@123")
    time.sleep(1)
    page.locator('//button[@id="login"]').click()

    page.wait_for_timeout(10000)
    print("The Final of Final OTP is:", otp_container[0])
    expect(page.locator('//input[@id="Loginotp"]')).to_be_visible()
    page.locator('//input[@id="Loginotp"]').fill(str(otp_container[0]))
    expect(page.locator('//button[@id="verifyotp"]')).to_be_visible()
    page.locator('//button[@id="verifyotp"]').click()

    expect(page.locator('//div[text()="Dashboard "]')).to_be_visible()
    page.locator("#dropdownMenu1").click()
    page.locator('//a[text()="Logout"]').click()

    expect(page.locator('//a[text()="Login"]')).to_be_visible()
    page.locator('//a[text()="Login"]').scroll_into_view_if_needed()
    # page.wait_for_timeout(10000)


