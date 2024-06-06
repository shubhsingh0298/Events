import os
import time
from playwright.sync_api import sync_playwright
import pymysql
from datetime import date
def get_visitor_id(page):
    visitor_id_element = page.query_selector('input[name="rpt_com_visitor_id"]')
    if visitor_id_element:
        visitor_id = visitor_id_element.get_attribute('value')
        return visitor_id
    else:
        return None

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.raptorsupplies.com/pd/morse-drum/86")
    time.sleep(1)
    page.wait_for_selector('#eve_38').click()
    time.sleep(2)
    visitor_id = get_visitor_id(page)
    if visitor_id:
        print("Visitor ID:", visitor_id)
    element = page.wait_for_selector("//*[@id='eve_294']/a", state='visible')
    element.click()
    time.sleep(12)
    page.fill("#customer-email","rahul@raptorsupplies.co.uk")
    firstname_input = page.wait_for_selector('input[name="firstname"]')
    firstname_input.fill('Rahul')
    page.fill('input[name="lastname"]', 'Singh')
    page.fill('input[name="company"]', 'Raptor ')
    page.fill('input[name="street[0]"]', 'Mohan Estate')
    page.fill('input[name="city"]', 'Delhi')
    page.select_option('select[name="country_id"]', 'India')
    page.select_option('select[name="region_id"]', 'Delhi')
    # page.fill('input[name="region_id"]', 'Delhi')
    page.fill('input[name="postcode"]', '110021')
    page.fill('input[name="telephone"]', '1234567890')
    time.sleep(4)
    page.get_by_label("Billing / Delivery Same").uncheck()
    page.get_by_label("Billing / Delivery Same").check()
    print('Same day delivery check !!')
    page.evaluate('document.querySelector("#eve_200").removeAttribute("disabled")')
    page.wait_for_selector('#eve_200').click()
    page.wait_for_selector("//*[@class='edit_shipping_info']").click()
    time.sleep(8)
    page.select_option('select[name="region_id"]', 'Goa')
    page.evaluate('document.querySelector("#eve_200").removeAttribute("disabled")')
    page.wait_for_selector('#eve_200').click()
    page.get_by_text("Shipping Information Edit Shipping Details Edit Payment").click()
    page.get_by_label("Economy (6 - 10 days)").check()
    page.get_by_role("row", name="Express (5 - 7 days) $").click()
    page.get_by_label("Ex-Works Pickup").check()
    page.get_by_text("FedEx - International Priority").click()
    page.get_by_placeholder("xxxxxxxxx").click()
    page.get_by_placeholder("xxxxxxxxx").fill("4325665")
    page.get_by_role("button", name="Proceed to Payment").click()
    page.get_by_text("NET30 Payment").click()
    purschase_no = "//*[@id='eve_209']"

    page.fill(purschase_no, '6547685')
    # Click on checkbox of credit card
    net_payment_Checkbox = "//*[@id='net_check']"
    page.locator(net_payment_Checkbox).check()
    page.get_by_text("Proforma Invoice").click()
    time.sleep(2)
    page.get_by_role("textbox", name="Purchase Order # (Optional)").click()
    time.sleep(2)
    page.get_by_role("textbox", name="Purchase Order # (Optional)").fill("123456")
    time.sleep(2)
    page.get_by_role("textbox", name="Purchase Order # (Optional)").click()
    time.sleep(2)
    page.locator("#performa_check").check()
    page.locator('#performa_real').click()
    print('Performa Invoice Payment!!!')
    time.sleep(10)
    browser.close()


conn = pymysql.connect(host="production-cms.c5tedj3txtxy.eu-west-1.rds.amazonaws.com", user="raptoradmin", password="Raptorcms2022", database='events', port=3306)
cursor = conn.cursor()
today = date.today()
formatted_date = today.strftime("raptor_browser_fingerprinting_transaction_%Y_%m_%d")
table_name = formatted_date
cursor.execute("SELECT * FROM "+table_name+" WHERE visitor_id = %s", (visitor_id,))
results = cursor.fetchall()

strings = {"eve_192": "BP1", "eve_193": "BP1", "eve_194": "BP1", "eve_195": "BP1", "eve_196": "BP1", "eve_197": "BP1",
           "eve_198": "BP1", "eve_199": "BP1", "eve_200": "BPN1", "eve_201": "BP1",
           "eve_203": "BP1", "eve_204": "BP1", "eve_205": "BPN", "eve_206": "BP1", "eve_207": "BPN1", "eve_209": "BP1",
           "eve_210": "BP", "eve_211": "BPN1", "eve_334": "BPN1", "eve_396": "BP1"}

def update_event(cursor, eve_id, status_mark, base_origin_url, prev_url, next_url, value1, value2):
    cursor.execute("""
        UPDATE `event_file`
        SET status_mark = %s, base_origin_url = %s, prev_url = %s, next_url = %s, value1 = %s, value2 = %s 
        WHERE Event_ID = %s
    """, (status_mark, base_origin_url, prev_url, next_url, value1, value2, eve_id))

for x in results:
    eve_id = 'eve_' + str(x[-2])
    print(eve_id)

    if eve_id in strings:
        print("yes")
        con = (strings[eve_id])  # Print the corresponding value
        if con == 'BPN':
            if (x[9] != '' and x[11] != '') or x[10] != '':
                print("Working")
                update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
            else:
                print("Error")
                update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
        elif con == 'BPN1':
            if (x[9] != '' and x[11] != '' and x[5] != '') or x[10] != '':
                print("Working")
                update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
            else:
                print("Error")
                update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
        elif con == 'BP1':
            if (x[9] != '' and x[5] != '') or x[10] != '':
                print("Working")
                update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
            else:
                print("Error")
                update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
        elif con == 'BP':
            if (x[9] != '') or x[10] != '':
                print("Working")
                update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
            else:
                print("Value Error")
                update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
    else:
        print("no")

conn.commit()
cursor.close()
conn.close()