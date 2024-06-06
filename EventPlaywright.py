import time
from datetime import date
import pymysql
from playwright.sync_api import TimeoutError, Error
from playwright.sync_api import sync_playwright


class EventAutomation:

    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        # self.page.set_viewport_size({"width": 1920, "height": 1080})  # Simulates maximized window
        self.exceptions = {}

    def finds_elements(self, xpath, key=''):
        try:
            if key != '':
                # print("yes")
                try:
                    self.page.fill(xpath, key)
                except:
                    if key != '':
                        try:
                            self.page.wait_for_selector(xpath, timeout=10000)
                            self.page.fill(xpath, key)
                        except:
                            self.page.select_option(xpath,key)
            else:
                try:
                    self.page.wait_for_selector(xpath).click()
                    # self.logs()
                except:
                    print("yes")
                    try:
                        self.page.locator(xpath).click()
                    except:

                        pass

        except:
            print("Element Not Clicked .........", xpath)




    def logs(self):
        return

    def back(self):
        self.page.go_back()
        time.sleep(1)

    def disable_element(self, xpath):
        try:
            print(xpath)
            self.page.evaluate(f'document.querySelector("{xpath}").removeAttribute("disabled")')
            self.page.click(xpath)
            print("Element attribute 'disabled' removed successfully.")
        except Exception as e:
            print(f"Error disabling element: {e}")
    def get_by_label(self,xpath):
        self.page.get_by_label(xpath).check()
    def reload(self):
        self.page.reload()
        time.sleep(1)
    def request_func(self, url):
        self.page.goto(url)  # Navigate to the URL
        time.sleep(1)  # Sleep for 1 second

    def select_option_by_text(self,page, select_locator, option_text):
        page.select_option(select_locator, value=option_text)

    def _create_context(self, is_mobile):
        if is_mobile:
            return self.playwright.chromium.launch(headless=False).new_context(
                viewport={"width": 360, "height": 640},
                device_scale_factor=3.0,
                is_mobile=True,
                user_agent="Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"
            )
        else:
            return self.playwright.chromium.launch(headless=False).new_context()

    def mobile_screen_request(self, url):
        mobile_context = None
        try:
            mobile_context = self._create_context(is_mobile=True)
            mobile_page = mobile_context.new_page()
            mobile_page.goto(url)
            # mobile_page.set_viewport_size(width=360, height=640)
            time.sleep(2) 
        except Exception as e:
            print("Mobile View request failed:", e)
            self.exceptions[url] = e
        finally:
            if mobile_context:
                mobile_context.close()

    def find_multi_elements(self, locator):
        if locator.startswith("//") or locator.startswith("(//"):
            # XPath selector
            return self.page.locator(f"xpath={locator}").all()
        elif locator.startswith("#") or locator.startswith("."):
            # CSS selector
            return self.page.locator(f"css={locator}").all()
        elif locator.startswith("text="):
            # Text selector
            return self.page.locator(locator).all()
        else:
            # Default to CSS selector if no specific identifier
            return self.page.locator(f"css={locator}").all()

    def switch_to_frame(self, xpath):
        try:
            frame = self.page.wait_for_selector(f"xpath={xpath}", timeout=3000).content_frame()
            return frame
        except Error.TimeoutError:
            print(f"Frame not found: {xpath}")



    def element_hover(self, xpath):
        try:
            element_xpath = xpath  # Replace with the appropriate XPath for the element

            # Hover over the element
            self.page.hover(f'xpath={element_xpath}')
        except Exception as ex:
            print("Error during element hover:", ex)

    def chat_box_close(self):
        try:
            iframe = self.page.frame_locator("iframe[title='Find more information here']")
            iframe.locator("button[aria-label='Minimize widget']").wait_for(timeout=10000)
            iframe.locator("button[aria-label='Minimize widget']").click()
        except TimeoutError:
            print("Timeout waiting for chat box to be clickable")
        except Exception as e:
            print(f"Error closing chat box: {e}")

    def trust_pilot_click(self, xpath):
        try:
            self.page.hover(xpath)
            self.page.frame(xpath)
            trust_pilot_element = self.page.wait_for_selector("//span[contains(@class, 'starnew')]/img[contains(@src, '/pub/static/frontend/Raptor/Desktop/en_US/images/trustpilot-logo.svg')]")
            trust_pilot_element.click()
            # new_page = self.page.wait_for_event('popup')
            # new_page.bring_to_front()
            # new_page.close()
            # self.page.bring_to_front()

        except TimeoutError as e:
            print("Timeout waiting for element to be clickable:", e)

        except Exception as e:
            print("Element handle error:", e)

    def send_key(self, key):
        try:
            self.page.keyboard.press(key)
        except Error.TimeoutError as ex:
            print(f"An error occurred: {ex}")

    

    def driver_quit(self):
        self.browser.close()
        

    def print_visitor_id(self):
        try:
            self.page.wait_for_timeout(5000)

            visitor_id = self.page.query_selector('//*[@id="rpt_com_visitor_id"]').get_attribute('value')

            print("Visitor ID >>>>>>>>>>>>> ", visitor_id)
            return visitor_id
        except:
            return "not generated"

    def report_genrate(self, visitor_id, con, val1, val2, eve_id):
        try:
            conn = pymysql.connect(host="production-cms.c5tedj3txtxy.eu-west-1.rds.amazonaws.com", user="raptoradmin",
                                   password="Raptorcms2022", database='events', port=3306)
            cursor = conn.cursor()
            if str(visitor_id) == 'not generated':
                cursor.execute("""
                    UPDATE event_file_global 
                    SET status_mark = %s, base_origin_url = %s, prev_url = %s, next_url = %s, value1 = %s, value2 = %s 
                    WHERE Event_ID = %s
                """, ('Event Not Trigger', '', '', '', '', '', 'eve_' + eve_id))
                conn.commit()

            today = date.today()
            formatted_date = today.strftime("raptor_browser_fingerprinting_transaction_%Y_%m_%d")
            table_name = formatted_date

            cursor.execute("SELECT * FROM " + table_name + " WHERE visitor_id = %s", (visitor_id,))
            results = cursor.fetchall()
            row_count = len(results)
            result_counts = {}

            def update_event(cursor, eve_id, status_mark, base_origin_url, prev_url, next_url, value1, value2):
                cursor.execute("""
                    UPDATE event_file_global 
                    SET status_mark = %s, base_origin_url = %s, prev_url = %s, next_url = %s, value1 = %s, value2 = %s 
                    WHERE Event_ID = %s
                """, (status_mark, base_origin_url, prev_url, next_url, value1, value2, 'eve_' + eve_id))

            print(row_count)

            if not results:
                print("no result")
                update_event(cursor, eve_id, 'Event Not Trigger', '', '', '', '', '')
            else:
                for x in results:
                    if x[-2] == eve_id:
                        if con == 'BPN':
                            if val1 == '' and val2 == '':
                                if (x[9] != '' and x[11] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
                            if val1 != '' and val2 == '':
                                if (x[9] != '' and x[11] != '' and x[5] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
                            if val1 != '' and val2 != '':
                                if (x[9] != '' and x[11] != '' and x[5] != '' and x[6] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
                            if val1 == '' and val2 != '':
                                if (x[9] != '' and x[11] != '' and x[6] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
                        elif con == 'BP':
                            if val1 == '' and val2 == '':
                                if (x[9] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
                            if val1 != '' and val2 == '':
                                if (x[9] != '' and x[5] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
                            if val1 != '' and val2 != '':
                                if (x[9] != '' and x[5] != '' and x[6] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
                            if val1 == '' and val2 != '':
                                if (x[9] != '' and x[5] == '' and x[6] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
                        elif con == '':
                            if val1 == '' and val2 == '':
                                if (x[9] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
                                else:
                                    print("Value Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
                            if val1 != '' and val2 == '':
                                if x[5] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
                                else:
                                    print("Value Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
                            if val1 != '' and val2 != '':
                                if x[5] != '' and x[6] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
                                else:
                                    print("Value Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
                            if val1 == '' and val2 != '':
                                if x[6] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
                                else:
                                    print("Value Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
                        else:
                            # Handle other conditions
                            pass



                    elif x[-2] == '90' and row_count == 1:
                        print("status 0")
                        update_event(cursor, eve_id, 'Event not trigger', x[9], x[10], x[11], x[5], x[6])
                    elif row_count == 0:
                        print("Event not fire", eve_id)
                    elif x[-2] == '90':
                        print("PAGE View")

                    else:
                        cursor.execute(
                            "SELECT events_id FROM " + table_name + " WHERE visitor_id = %s AND events_id = %s",
                            (visitor_id, eve_id))
                        result = cursor.fetchone()
                        if result:
                            print("Event ID exists for the visitor ID")
                        else:
                            update_event(cursor, eve_id, 'Event not trigger/status_0', '', '', '', '', '')
                conn.commit()
                cursor.execute(
                    "SELECT events_id,base_origin_url,prev_url,next_url,value1,value2 FROM " + table_name + " WHERE visitor_id = %s AND events_id = %s GROUP BY events_id, event_operation_time HAVING COUNT(*) > 1",
                    (visitor_id, eve_id))
                dup = cursor.fetchall()
                for dupli in dup:
                    dup_id = dupli[0]
                    base_url = dupli[1]
                    prev_url = dupli[2]
                    next_url = dupli[3]
                    value1 = dupli[4]
                    value2 = dupli[5]
                    print('multi fire', dupli[0])
                    update_event(cursor, dup_id, 'Multiple Fire', base_url, prev_url, next_url, value1, value2)
            conn.commit()
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def report_genrate_global(self, visitor_id, con, val1, val2, eve_id, url):
        try:
            conn = pymysql.connect(host="production-cms.c5tedj3txtxy.eu-west-1.rds.amazonaws.com", user="raptoradmin",
                                   password="Raptorcms2022", database='events', port=3306)
            cursor = conn.cursor()
            if str(visitor_id) == 'not generated':
                cursor.execute("""
                    UPDATE event_file_global 
                    SET status_mark = %s, base_origin_url = %s, prev_url = %s, next_url = %s, value1 = %s, value2 = %s 
                    WHERE Event_ID = %s and Pages= %s
                """, ('Event Not Trigger', '', '', '', '', '', 'eve_' + eve_id, url))
                conn.commit()
            today = date.today()
            formatted_date = today.strftime("raptor_browser_fingerprinting_transaction_%Y_%m_%d")
            table_name = formatted_date
            cursor.execute("SELECT * FROM " + table_name + " WHERE visitor_id = %s", (visitor_id,))
            results = cursor.fetchall()
            # print(results)
            row_count = len(results)
            result_counts = {}

            def update_event(cursor, eve_id, status_mark, base_origin_url, prev_url, next_url, value1, value2, url):
                cursor.execute("""
                    UPDATE event_file_global 
                    SET status_mark = %s, base_origin_url = %s, prev_url = %s, next_url = %s, value1 = %s, value2 = %s 
                    WHERE Event_ID = %s and Pages = %s
                """, (status_mark, base_origin_url, prev_url, next_url, value1, value2, 'eve_' + eve_id, url))

            print(row_count)

            if not results:
                print("no result")
                update_event(cursor, eve_id, 'Event not trigger', '', '', '', '', '', url)
            else:
                for x in results:
                    if x[-2] == eve_id and url == x[9]:
                        if con == 'BPN':
                            if val1 == '' and val2 == '':
                                if (x[9] != '' and x[11] != '') or x[10] != '':
                                    print("Working_hereee")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6], url)
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6], url)
                            if val1 != '' and val2 == '':
                                if (x[9] != '' and x[11] != '' and x[5] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6], url)
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6], url)
                            if val1 != '' and val2 != '':
                                if (x[9] != '' and x[11] != '' and x[5] != '' and x[6] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6], url)
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6], url)
                            if val1 == '' and val2 != '':
                                if (x[9] != '' and x[11] != '' and x[6] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6], url)
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6], url)
                        elif con == 'BP':
                            if val1 == '' and val2 == '':
                                if (x[9] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6], url)
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6], url)
                            if val1 != '' and val2 == '':
                                if (x[9] != '' and x[5] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6], url)
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6], url)
                            if val1 != '' and val2 != '':
                                if (x[9] != '' and x[5] != '' and x[6] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6], url)
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6], url)
                            if val1 == '' and val2 != '':
                                if (x[9] != '' and x[5] == '' and x[6] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6], url)
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6], url)
                        elif con == '':
                            if val1 == '' and val2 == '':
                                if (x[9] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6], url)
                                else:
                                    print("Value Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6], url)
                            if val1 != '' and val2 == '':
                                if x[5] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6], url)
                                else:
                                    print("Value Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6], url)
                            if val1 != '' and val2 != '':
                                if x[5] != '' and x[6] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6], url)
                                else:
                                    print("Value Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6], url)
                            if val1 == '' and val2 != '':
                                if x[6] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6], url)
                                else:
                                    print("Value Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6], url)
                        else:
                            # Handle other conditions
                            pass



                    elif x[-2] == '90' and row_count == 1:
                        print("status 0")
                        update_event(cursor, eve_id, 'Event not trigger9000000', x[9], x[10], x[11], x[5], x[6], url)
                    elif row_count == 0:
                        print("Event not fire", eve_id)
                    elif x[-2] == '90':
                        print("PAGE View")

                    else:
                        cursor.execute(
                            "SELECT events_id FROM " + table_name + " WHERE visitor_id = %s AND events_id = %s AND base_origin_url =%s",
                            (visitor_id, eve_id, url))
                        result = cursor.fetchone()
                        if result:
                            print("Event ID exists for the visitor ID")
                        else:
                            update_event(cursor, eve_id, 'Event not trigger/status_0', '', '', '', '', '', url)
                conn.commit()
                cursor.execute(
                    "SELECT events_id,base_origin_url,prev_url,next_url,value1,value2 FROM " + table_name + " WHERE visitor_id = %s AND events_id = %s AND base_origin_url=%s  GROUP BY events_id, event_operation_time,base_origin_url HAVING COUNT(*) > 1",
                    (visitor_id, eve_id, url))
                dup = cursor.fetchall()
                for dupli in dup:
                    dup_id = dupli[0]
                    base_url = dupli[1]
                    prev_url = dupli[2]
                    next_url = dupli[3]
                    value1 = dupli[4]
                    value2 = dupli[5]
                    print('multi fire', dupli[0])
                    update_event(cursor, dup_id, 'Multiple Fire', base_url, prev_url, next_url, value1, value2, url)
            conn.commit()
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()
