import time
import json
# from passcode import password
from datetime import datetime
import csv
from datetime import date
from selenium.webdriver import Chrome, ChromeOptions

class EventAutomation:
   def __init__(self):
        options = ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        
        self.options = options
        self.driver = Chrome(service=Service(), options=self.options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.exceptions = exceptions

    def logs(self):
        return
        logs = self.driver.get_log('performance')
        # res_dict = dict(logs)
        # data = json.loads(logs)
        # print(log)
        perf = {'e': []}
        for i, en in enumerate(logs):
            # print(en)
            if 'event_name' in str(en):
                j = json.loads(en['message'])
                k = j["message"]['params']['request']['postData']
                print(k.split('&'))

    def finds_elements(self, xpath, key=''):
        try:
            if key != '':
                self.driver.find_element(By.XPATH, xpath).send_keys(key)
                self.logs()
                time.sleep(3)
            else:
                try:
                    self.wait.until(EC.presence_of_element_located((By.XPATH, xpath))).click()
                    self.logs()
                except (BaseException, NoSuchElementException, ElementClickInterceptedException):
                    self.element_hover(xpath)
                    self.driver.execute_script(f"window.scrollBy(0, {500});")
                    self.logs()
                    self.wait.until(EC.presence_of_element_located((By.XPATH, xpath))).click()
                    self.logs()
                time.sleep(5)
        except (BaseException, NoSuchElementException, TimeoutException, ElementClickInterceptedException):
            print("Element Not Clicked .........", xpath)
            pass

    def request_func(self, url):
        self.driver.get(url)
        time.sleep(1)

    def mobile_screen_request(self, url):
        try:
            self.driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
            "width": 360,
            "height": 640,
            "deviceScaleFactor": 3.0,
            "mobile": True
            })

            # Set user agent string
            self.driver.execute_cdp_cmd("Network.setUserAgentOverride", {
                "userAgent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"
            })
            self.driver.get(url)
        except (BaseException, Exception) as ex:
            print("Mobile View request failed .............", ex)
            pass

    def find_multi_elements(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)

    def switch_to_frame(self, xpath):
        frame = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        self.driver.switch_to.frame(frame)
        time.sleep(3)

    def element_hover(self, xpath, drag=False):
        try:
            pop_up_element1 = self.driver.find_element(By.XPATH, xpath)
            actions = ActionChains(self.driver)
            actions.move_to_element(pop_up_element1)
            actions.perform()
            if drag:
                actions.drag_and_drop_by_offset(pop_up_element1, -100,
                                                -200)  # Move the element by 100 pixels horizontally and vertically
                # Execute the action chain
                actions.perform()
        except (BaseException, Exception) as ex:
            print(ex)
            pass

    def tagmanager_popup_move(self):
        self.switch_to_frame("//iframe[@class='__TAG_ASSISTANT_BADGE']")
        self.finds_elements('/html/body/debug-badge/frame-auto-resize/div/div/div[2]/i')
        self.element_hover('/html/body/debug-badge/frame-auto-resize/div/div[1]/div[1]/i', drag=True)
        self.driver.switch_to.default_content()

    def robot_click(self, xpath):
        self.switch_to_frame(xpath)
        self.finds_elements('//*[@id="recaptcha-anchor"]/div[1]')
        self.driver.switch_to.default_content()

    def chat_box_close(self):
        try:
            self.switch_to_frame('//*[@id="webWidget"]')
            self.finds_elements("//button[@aria-label='Minimize widget']")
            self.driver.switch_to.default_content()
        except TimeoutException:
            print("chatbox time out error")
            pass
        except ElementClickInterceptedException:
            print('Retry chat box closing')
            self.chat_box_close()

    def trust_pilot_click(self, xpath):
        # self.element_hover(By.XPATH, xpath)
        # trust_pilot_frame = xpath
        # self.switch_to_frame(trust_pilot_frame)
        # trust_pilot_click = '//*[@id="tp-widget-wrapper"]'
        # self.finds_elements(xpath)
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        # self.driver.close()
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        try:
            # Wait for element to be clickable
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            
            # Perform hover action
            ActionChains(self.driver).move_to_element(element).perform()
            
            # Click on the element
            element.click()
            
            # Switch to the new window
            self.driver.switch_to.window(self.driver.window_handles[-1])
            
            # Close the new window
            self.driver.close()
            
            # Switch back to the original window
            self.driver.switch_to.window(self.driver.window_handles[-1])
        except NoSuchElementException as e:
            print("Element not found:", e)
        except TimeoutException as e:
            print("Timeout waiting for element to be clickable:", e)

    def send_key(self, key):
        try:
            actions = ActionChains(self.driver)
            actions.send_keys(key)
        except exceptions as ex:
            print(ex)
        pass



    def save_output(self, filename='output'):
        self.driver.switch_to.window(self.driver.window_handles[1])
        file = open(f'{filename}.txt', 'a+', encoding='utf-8')
        fire_tags = self.driver.find_elements(By.XPATH, '//*[@id="gtm-debug-id-has-tags"]/div[1]/div/div[1]')
        fire_tags_number = self.driver.find_elements(By.XPATH, '//*[@id="gtm-debug-id-has-tags"]/div[1]/div/div[2]')
        for tags, number in zip(fire_tags, fire_tags_number):
            print(tags.text, ">>>>>>>>>", number.text, ">>>>>>>>>>>", datetime.now())
            file.write('\n' + tags.text + "\t" + number.text + "\t" + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        file.close()

    def driver_quit(self):
        self.driver.quit()
        # self.driver.close()

    def print_visitor_id(self):
        try:
            time.sleep(5)
            
            visitor_id = self.driver.find_element(By.XPATH, '//*[@id="rpt_com_visitor_id"]').get_attribute('value')
            
            print("Visitor ID >>>>>>>>>>>>> ", visitor_id)
            return visitor_id
        except:
            return "not generated"


    

    def report_genrate(self,visitor_id, con, val1, val2, eve_id):
        try:
            conn = pymysql.connect(host="production-cms.c5tedj3txtxy.eu-west-1.rds.amazonaws.com", user="raptoradmin", password="Raptorcms2022", database='events', port=3306)
            cursor = conn.cursor()
            if str(visitor_id) == 'not generated':
                cursor.execute("""
                    UPDATE event_file 
                    SET status_mark = %s, base_origin_url = %s, prev_url = %s, next_url = %s, value1 = %s, value2 = %s 
                    WHERE Event_ID = %s
                """, ('Event Not Trigger', '', '', '', '', '', 'eve_' + eve_id))
                conn.commit()

            today = date.today()
            formatted_date = today.strftime("raptor_browser_fingerprinting_transaction_%Y_%m_%d")
            table_name = formatted_date



            cursor.execute("SELECT * FROM "+table_name+" WHERE visitor_id = %s", (visitor_id,))
            results = cursor.fetchall()
            row_count = len(results)
            result_counts = {}
            def update_event(cursor, eve_id, status_mark, base_origin_url, prev_url, next_url, value1, value2):
                cursor.execute("""
                    UPDATE event_file 
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
                                if (x[9] != '' and x[11] != '' and x[5] !='') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
                            if val1 != '' and val2 != '':
                                if (x[9] != '' and x[11] != '' and x[5] !='' and x[6] !='') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
                            if val1 == '' and val2 != '':
                                if (x[9] != '' and x[11] != '' and x[6] !='') or x[10] != '':
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
                                if (x[9] != '' and x[5] != '' and x[6] !='') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
                            if val1 == '' and val2 != '':
                                if (x[9] != '' and x[5] == '' and x[6] !='') or x[10] != '':
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
                                if x[5] != '' and x[6] !='':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6])
                                else:
                                    print("Value Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6])
                            if val1 == '' and val2 != '':
                                if x[6] !='':
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
                        cursor.execute("SELECT events_id FROM "+table_name+" WHERE visitor_id = %s AND events_id = %s", (visitor_id, eve_id))
                        result = cursor.fetchone()
                        if result:
                            print("Event ID exists for the visitor ID")
                        else:
                            update_event(cursor, eve_id, 'Event not trigger/status_0', '','', '', '', '')
                conn.commit()        
                cursor.execute("SELECT events_id,base_origin_url,prev_url,next_url,value1,value2 FROM "+table_name+" WHERE visitor_id = %s AND events_id = %s GROUP BY events_id, event_operation_time HAVING COUNT(*) > 1", (visitor_id, eve_id))
                dup = cursor.fetchall()
                for dupli in dup:
                    dup_id = dupli[0]
                    base_url = dupli[1]
                    prev_url = dupli[2]
                    next_url = dupli[3]
                    value1 = dupli[4]
                    value2 = dupli[5]
                    print('multi fire' ,dupli[0])
                    update_event(cursor, dup_id, 'Multiple Fire', base_url, prev_url, next_url, value1, value2)
            conn.commit()
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()
    
    def report_genrate_global(self,visitor_id, con, val1, val2, eve_id,url):
        try:
            conn = pymysql.connect(host="production-cms.c5tedj3txtxy.eu-west-1.rds.amazonaws.com", user="raptoradmin", password="Raptorcms2022", database='events', port=3306)
            cursor = conn.cursor()
            if str(visitor_id) == 'not generated':
                cursor.execute("""
                    UPDATE event_file_global 
                    SET status_mark = %s, base_origin_url = %s, prev_url = %s, next_url = %s, value1 = %s, value2 = %s 
                    WHERE Event_ID = %s and Pages= %s
                """, ('Event Not Trigger', '', '', '', '', '', 'eve_' + eve_id,url))
                conn.commit()
            today = date.today()
            formatted_date = today.strftime("raptor_browser_fingerprinting_transaction_%Y_%m_%d")
            table_name = formatted_date
            cursor.execute("SELECT * FROM "+table_name+" WHERE visitor_id = %s", (visitor_id,))
            results = cursor.fetchall()
            # print(results)
            row_count = len(results)
            result_counts = {}
            def update_event(cursor, eve_id, status_mark, base_origin_url, prev_url, next_url, value1, value2,url):
                cursor.execute("""
                    UPDATE event_file_global 
                    SET status_mark = %s, base_origin_url = %s, prev_url = %s, next_url = %s, value1 = %s, value2 = %s 
                    WHERE Event_ID = %s and Pages = %s
                """, (status_mark, base_origin_url, prev_url, next_url, value1, value2, 'eve_' + eve_id,url))
                
            print(row_count)
            
            if not results:
                print("no result")
                update_event(cursor, eve_id, 'Event not trigger', '', '', '', '', '',url)
            else:
                for x in results:
                    if x[-2] == eve_id and url == x[9]:
                        if con == 'BPN':
                            if val1 == '' and val2 == '':
                                if (x[9] != '' and x[11] != '') or x[10] != '':
                                    print("Working_hereee")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6],url)
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6],url)
                            if val1 != '' and val2 == '':
                                if (x[9] != '' and x[11] != '' and x[5] !='') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6],url)
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6],url)
                            if val1 != '' and val2 != '':
                                if (x[9] != '' and x[11] != '' and x[5] !='' and x[6] !='') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6],url)
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6],url)
                            if val1 == '' and val2 != '':
                                if (x[9] != '' and x[11] != '' and x[6] !='') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6],url)
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6],url)
                        elif con == 'BP':
                            if val1 == '' and val2 == '':
                                if (x[9] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6],url)
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6],url)
                            if val1 != '' and val2 == '':
                                if (x[9] != '' and x[5] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6],url)
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6],url)
                            if val1 != '' and val2 != '':
                                if (x[9] != '' and x[5] != '' and x[6] !='') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6],url)
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6],url)
                            if val1 == '' and val2 != '':
                                if (x[9] != '' and x[5] == '' and x[6] !='') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6],url)
                                else:
                                    print("Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6],url)
                        elif con == '':
                            if val1 == '' and val2 == '':
                                if (x[9] != '') or x[10] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6],url)
                                else:
                                    print("Value Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6],url)
                            if val1 != '' and val2 == '':
                                if x[5] != '':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6],url)
                                else:
                                    print("Value Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6],url)
                            if val1 != '' and val2 != '':
                                if x[5] != '' and x[6] !='':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6],url)
                                else:
                                    print("Value Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6],url)
                            if val1 == '' and val2 != '':
                                if x[6] !='':
                                    print("Working")
                                    update_event(cursor, eve_id, 'Working', x[9], x[10], x[11], x[5], x[6],url)
                                else:
                                    print("Value Error")
                                    update_event(cursor, eve_id, 'Value Error', x[9], x[10], x[11], x[5], x[6],url)    
                        else:
                            # Handle other conditions
                            pass
                        
                    

                    elif x[-2] == '90' and row_count == 1:
                        print("status 0")
                        update_event(cursor, eve_id, 'Event not trigger9000000', x[9], x[10], x[11], x[5], x[6],url)
                    elif row_count == 0:
                        print("Event not fire", eve_id)
                    elif x[-2] == '90':
                        print("PAGE View")
                    
                    else:
                        cursor.execute("SELECT events_id FROM "+table_name+" WHERE visitor_id = %s AND events_id = %s AND base_origin_url =%s" , (visitor_id, eve_id,url))
                        result = cursor.fetchone()
                        if result:
                            print("Event ID exists for the visitor ID")
                        else:
                            update_event(cursor, eve_id, 'Event not trigger/status_0', '','', '', '', '',url)
                conn.commit()        
                cursor.execute("SELECT events_id,base_origin_url,prev_url,next_url,value1,value2 FROM "+table_name+" WHERE visitor_id = %s AND events_id = %s AND base_origin_url=%s  GROUP BY events_id, event_operation_time,base_origin_url HAVING COUNT(*) > 1", (visitor_id, eve_id,url))
                dup = cursor.fetchall()
                for dupli in dup:
                    dup_id = dupli[0]
                    base_url = dupli[1]
                    prev_url = dupli[2]
                    next_url = dupli[3]
                    value1 = dupli[4]
                    value2 = dupli[5]
                    print('multi fire' ,dupli[0])
                    update_event(cursor, dup_id, 'Multiple Fire', base_url, prev_url, next_url, value1, value2,url)
            conn.commit()
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()
