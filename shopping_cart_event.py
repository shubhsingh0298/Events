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
    time.sleep(1)
    visitor_id = get_visitor_id(page)
    if visitor_id:
        print("Visitor ID:", visitor_id)
    page.get_by_role("link", name="View Cart").click()
    time.sleep(8)
    page.evaluate('document.querySelector("#eve_179").click()')
    time.sleep(2)
    page.wait_for_selector('#eve_38').click()
    time.sleep(1)
    page.get_by_role("link", name="View Cart").click()
    page.reload()
    time.sleep(2)
    page.wait_for_selector("#eve_180").click()
    print('Quantity Increased!!')
    time.sleep(10)
    page.wait_for_selector("#eve_181").click()
    time.sleep(5)
    print('Quantity Decreased!!')
    page.get_by_label("Country").select_option("India")
    time.sleep(5)
    # page.get_by_text("Economy (6 - 10 days) $558.49 Economy (6 - 10 days) Pickup from our US").click()
    # time.sleep(1)
    page.get_by_label("Economy (6 - 10 days)").check()
    time.sleep(1)
    print('Select country & shipping !')
    page.wait_for_selector("#eve_180").click()
    time.sleep(1)
    page.get_by_role("link", name="Remove item").click()
    time.sleep(1)
    page.get_by_role("button", name="cancel").click()
    time.sleep(1)
    print('Remove , Cancel !!')
    # try:
    #     page.frame_locator('iframe[title="Find more information here"]').get_by_label("Minimize widget").click()
    # except:
    #     pass
    page.get_by_text("FAB5 :").click()
    time.sleep(4)
    page.locator("#maincontent").get_by_role("link").nth(4).click()
    page.get_by_role("button", name="Remove").click()
    print("Apply and remove coupon!!")
    time.sleep(5)
    # page.frame_locator('iframe[title="Find more information here"]').get_by_label("Minimize widget").click()
    page.get_by_text("Print Quote").click()
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Save as PDF").click()
    download = download_info.value
    page.locator("#print").get_by_role("link").first.click()
    print('Clicked on Print quote and Save pdf!!')
    page.get_by_role("button", name="Checkout").click()
    print('Clicked on checkout!')
    page.go_back()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="See our 765 reviews on").click()
    page1 = page1_info.value
    print('Clicked on Trust Pilot!!')

    browser.close()

conn = pymysql.connect(host="production-cms.c5tedj3txtxy.eu-west-1.rds.amazonaws.com", user="raptoradmin", password="Raptorcms2022", database='events', port=3306)
cursor = conn.cursor()
today = date.today()
formatted_date = today.strftime("raptor_browser_fingerprinting_transaction_%Y_%m_%d")
table_name = formatted_date
cursor.execute("SELECT * FROM "+table_name+" WHERE visitor_id = %s", (visitor_id,))
results = cursor.fetchall()

strings = {"eve_179": "BPN12", "eve_180": "BP12", "eve_181": "BP12", "eve_182": "BP1", "eve_184": "BP12", "eve_185": "BP12",
           "eve_186": "BP12", "eve_187": "BPN2", "eve_350": "BP", "eve_352": "BP12",
           "eve_97": "BPN", "eve_399": "BP", "eve_400": "BP1"}

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
        elif con == 'BPN2':
            if (x[9] != '' and x[11] != '' and x[6] != '') or x[10] != '':
                print("Working")
                update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
            else:
                print("Error")
                update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
        elif con == 'BPN12':
            if (x[9] != '' and x[11] != '' and x[5] != '' and x[6] != '') or x[10] != '':
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
        elif con == 'BP12':
            if (x[9] != '' and x[5] != '' and x[6] != '') or x[10] != '':
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
