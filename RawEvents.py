import time
import pyautogui
from selenium.common import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from EventAutomationBaseClass import EventAutomation
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")


class RawEventsTesting(EventAutomation):

    def __init__(self):
        super().__init__()

    def eve_28(self, url):

        self.request_func(url)
        brand_name = '//*[@id="eve_28"]'  #28
        self.finds_elements(brand_name)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '28'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_32(self, url):

        self.request_func(url)
        small_image = '//*[@id="eve_32"]/div/a[2]'  #32  //*[@id="eve_32"]/div/a[2]/img
        self.finds_elements(small_image)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '32'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_33(self, url):
        self.request_func(url)
        time.sleep(2)
        self.finds_elements('//*[@class="share-icon"]')
        print("yesss")
        self.finds_elements('//*[@id="eve_33"]')   #33
        pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '33'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_34(self, url):
        self.request_func(url)
        # time.sleep(2)
        share_icon = '//*[@class="share-icon"]'
        self.finds_elements(share_icon)
        share_whatsapp = '//*[@id="eve_34"]'  #34
        self.finds_elements(share_whatsapp)
        self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '34'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_35(self, url):
        self.request_func(url)
        # time.sleep(2)
        share_icon = '//*[@class="share-icon"]'
        self.finds_elements(share_icon)
        share_button_copy = '//*[@id="eve_35"]'   #35   
        self.finds_elements(share_button_copy)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '35'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_24(self, url):
        self.request_func(url)
        related_pd = '//*[@id="eve_24"]'   #24
        self.finds_elements(related_pd)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '24'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_25(self, url):

        self.request_func(url)
        view_more_btn = '//*[@id="eve_25"]'    #25
        self.finds_elements(view_more_btn)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '25'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_26(self, url):

        self.request_func(url)
        related_pd_cart = '//*[@class="cartBtn related_product_cart"]'   #26 //*[@id="addcartquote_655741"]/div
        self.element_hover(related_pd_cart)
        self.finds_elements(related_pd_cart)
        # close_cart_popup = '//*[@id="close-button"]'
        # self.finds_elements(close_cart_popup)
        # self.chat_box_close()
        self.print_visitor_id()
        con = "BP"
        val1 = '# Product Tiltle'
        val2 = ''
        eve_id = '26'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_32(self, url):
        self.request_func(url)
        small_image = '//*[@id="eve_32"]/div/a[2]'  #32  //*[@id="eve_32"]/div/a[2]/img
        self.finds_elements(small_image)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '32'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_52(self, url):
        self.request_func(url)
        time.sleep(5)
        element = self.driver.find_element(By.XPATH,'//*[@id="eve_52"]/a')
        self.driver.execute_script("arguments[0].click();", element)
        
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '52'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_54(self, url):
        self.request_func(url)
        element = self.driver.find_element(By.XPATH,'//*[@id="eve_52"]/a')
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.back()
        recently_view_pd = '//*[@id="eve_54"]'  #54
        self.finds_elements(recently_view_pd)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '54'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_55(self, url):
        self.request_func(url)
        product_click = '//*[@id="eve_55"]' # 55
        self.finds_elements(product_click)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '55'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_56(self, url):
        self.request_func(url)
        self.element_hover('(//*[@class="includes_item"])[5]')
        left_click = '//*[@id="eve_57"]' # 57
        self.finds_elements(left_click)
        left_click = '//*[@id="eve_56"]' # 56
        self.finds_elements(left_click)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '56'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_57(self, url):
        self.request_func(url)
        self.element_hover('(//*[@class="includes_item"])[5]')
        left_click = '//*[@id="eve_57"]' # 57
        self.finds_elements(left_click)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '57'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_101(self, url):
        self.request_func(url)
        check_availability = '//*[@id="eve_101"]'  #101
        self.finds_elements(check_availability)
        self.chat_box_close()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '101'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_317(self, url):
        self.request_func(url)
        self.chat_box_close()
        other_also_viewed_cart = '//*[@class="rpt_green_btn rfq-btn"]'  #317  //*[@id="eve_317"]
        self.element_hover(other_also_viewed_cart)
        self.finds_elements(other_also_viewed_cart)
        # close_rfq_popup = '//*[@class="form-close eve_form-close allspriteicon close-icon"]'
        # self.finds_elements(close_rfq_popup)
        self.chat_box_close()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '317'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_363(self, url):
        self.request_func(url)
        name = '//*[@id="eve_363"]'
        self.finds_elements(name,'rahul')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = ""
        val1 = '# text'
        val2 = ''
        eve_id = '363'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_364(self, url):
        self.request_func(url)
        email = '//*[@id="eve_364"]'
        self.finds_elements(email,'rahul@raptorsupplies.co.uk')
        
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = ""
        val1 = '# text'
        val2 = ''
        eve_id = '364'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_365(self, url):
        self.request_func(url)
        number = '//*[@id="eve_365"]'
        self.finds_elements(number,'9999999999')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '365'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_366(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_366"]'
        self.finds_elements(comment,'comment')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = ""
        val1 = '# text'
        val2 = ''
        eve_id = '366'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_368(self, url):
        self.request_func(url)
        name = '//*[@id="eve_368"]'
        self.finds_elements(name,'rahul')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = ""
        val1 = '# text'
        val2 = ''
        eve_id = '368'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_369(self, url):
        self.request_func(url)
        email = '//*[@id="eve_369"]'
        self.finds_elements(email,'rahul@raptorsupplies.co.uk')
        
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = ""
        val1 = '# text'
        val2 = ''
        eve_id = '369'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_370(self, url):
        self.request_func(url)
        number = '//*[@id="eve_370"]'
        self.finds_elements(number,'9999999999')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = ""
        val1 = '# text'
        val2 = ''
        eve_id = '370'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_371(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_371"]'
        self.finds_elements(comment,'comment')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = ""
        val1 = '# text'
        val2 = ''
        eve_id = '371'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_252(self, url):
        self.request_func(url)
        time.sleep(1)
        self.finds_elements('//*[@id="eve_252"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '252'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_251(self, url):
        self.request_func(url)
        time.sleep(1)
        self.finds_elements('//*[@id="eve_251"]')
        self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '251'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_250(self, url):
        self.request_func(url)
        time.sleep(1)
        self.finds_elements('//*[@id="eve_250"]')
        self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '250'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_9(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_9']")
        # self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '9'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_13(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_13']")
        # self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '13'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_16(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_16']")
        pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '16'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_18(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_18']")
        pyautogui.press('enter')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '18'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_89(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_89']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '89'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_299(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_299']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '299'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_302(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_302']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '302'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_304(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_304']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '304'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_76(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_76']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '76'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_212(self, url):
        self.mobile_screen_request(url)
        time.sleep(5)
        self.chat_box_close()
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        print('icon click')
        self.finds_elements('//*[@id="eve_212"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '212'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_213(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        self.finds_elements('//*[@id="eve_213"]')
        self.chat_box_close()
        self.finds_elements('//*[@id="countryBgId"]//span')
        print('country close')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '213'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_214(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        self.finds_elements('//*[@id="eve_214"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '214'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_215(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        print('icon click')
        self.finds_elements('//*[@id="eve_215"]')
        print('brand click')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '215'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_216(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        self.finds_elements('//*[@id="eve_212"]')
        print('sign in')
        self.finds_elements('//*[@id="email"]', 'devanshu@nextgenesolutions.com')
        print('username')
        self.finds_elements('//*[@id="pass"]', 'Devanshu@123')
        print('password')
        self.chat_box_close()
        self.finds_elements('//*[@id="send2"]')
        print('login')
        time.sleep(4)
        # self.driver.back()
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        print('icon click')
        self.finds_elements('//*[@id="eve_216"]')  
        # print('my profile')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '216'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_217(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        print('icon click')
        self.finds_elements('//*[@id="eve_217"]')
        print('orders')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '217'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_218(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        print('icon click')
        self.finds_elements('//*[@id="eve_218"]')
        print('coupons')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '218'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_219(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        print('icon click')
        self.chat_box_close()
        self.finds_elements('//*[@id="eve_219"]')
        print('fAQ')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '219'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_220(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        print('icon click')
        self.element_hover('//*[@id="eve_220"]')
        self.finds_elements('//*[@id="eve_220"]')
        print('t and c')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '220'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_221(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        print('icon click')
        self.element_hover('//*[@id="eve_221"]')
        self.finds_elements('//*[@id="eve_221"]')
        print('privacy policy')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '221'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_229(self, url):
        self.mobile_screen_request(url)
        self.driver.refresh()
        self.finds_elements('/html/body', Keys.END)
        time.sleep(2)
        add_to_cart = '//*[@id="eve_229"]'
        self.element_hover(add_to_cart)
        # self.finds_elements(add_to_cart)
        element = self.driver.find_element(By.ID,'eve_229')
        self.driver.execute_script("arguments[0].click();", element)
        print('Add to cart')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '229'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_231(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('/html/body', Keys.END)
        self.finds_elements('//*[@id="eve_229"]')
        print('Add to cart')
        time.sleep(4)
        self.finds_elements('//*[@id="eve_293"]')

        self.finds_elements('//*[@id="eve_231"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '231'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_354(self, url):
        self.request_func(url)
        self.finds_elements('//*[@name="name"]', 'rahul')#354
        print('Name Field')
        self.finds_elements('//*[@id="brand_form"]/div/div[7]/button')#357, 358
        print('Sumbit Click')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '354'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_355(self, url):
        self.request_func(url)
        self.finds_elements('//*[@name="email"]', 'rahul@raptorsupplies.co.uk')#355
        print("Email Field")
        self.finds_elements('//*[@class="discoun_brand_sem_btn-default sendbutton"]')#357, 358
        print('Sumbit Click')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '355'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_356(self, url):
        self.request_func(url)
        self.finds_elements('//*[@name="phone"]', '9999999999')#356
        print('Number Field')
        self.finds_elements('//*[@class="discoun_brand_sem_btn-default sendbutton"]')#357, 358
        print('Sumbit Click')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '356'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_77(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_77"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '77'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_78(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_77"]')
        self.finds_elements('//*[@id="eve_86"]')
        
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '78'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_64(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_64"]')  #//*[@id="eve_64"]
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '64'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_253(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_253"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '253'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_254(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_254"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '254'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_40(self, url):
        self.request_func(url)
        self.finds_elements("(//*[@id='main_rfq_btn'])")
        self.finds_elements('//*[@id="eve_40"]', 'rahul')
        self.finds_elements('//*[@id="shipping-form"]/div/div[3]/button')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '40'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_41(self, url):
        self.request_func(url)
        self.finds_elements("(//*[@id='main_rfq_btn'])")
        self.finds_elements('//*[@id="eve_41"]', 'rahul@raptorsupplies.co.uk')
        self.finds_elements('//*[@id="shipping-form"]/div/div[3]/button')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '41'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_42(self, url):
        self.request_func(url)
        self.finds_elements("(//*[@id='main_rfq_btn'])")
        self.finds_elements('//*[@name="customer_number"]', '8294966962')
        self.finds_elements('//*[@id="shipping-form"]/div/div[3]/button')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '42'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_43(self, url):
        self.request_func(url)
        self.finds_elements("(//*[@id='main_rfq_btn'])")
        self.finds_elements('//*[@id="eve_43"]', 'Automation testing')
        self.finds_elements('//*[@id="shipping-form"]/div/div[3]/button')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '43'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)


    def eve_38(self, url):
        self.request_func(url)
        add_to_cart = '//*[@id="eve_38"]'
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        # self.chat_box_close()
        self.print_visitor_id()
        con = "BP"
        val1 = '# Quantity'
        val2 = ''
        eve_id = '38'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_39(self, url):
        self.request_func(url)
        rfq = "//*[@id='main_rfq_btn']"
        self.element_hover(rfq)
        self.finds_elements(rfq)
        self.print_visitor_id()
        con = "BP"
        val1 = '# Quantity'
        val2 = ''
        eve_id = '39'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_51(self, url):
        self.request_func(url)
        content_menu = '//*[@id="eve_51"]/li[2]/a'
        self.finds_elements(content_menu)
        self.print_visitor_id()
        
        con = "BP"
        val1 = '# field'
        val2 = ''
        eve_id = '51'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_53(self, url):
        self.request_func(url)
        # add_to_cart = '//*[@id="eve_52"]/div[4]/div'  #//*[@id="eve_52"]/div[4]/div
        # self.element_hover(add_to_cart)
        # self.finds_elements(add_to_cart)
        element = self.driver.find_element(By.XPATH,'//*[@id="eve_52"]/div[4]/div')
        self.driver.execute_script("arguments[0].click();", element)
        self.print_visitor_id()
        
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '53'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_319(self, url):
        self.request_func(url)
        comment = '//*[@id="row1_2"]'
        self.finds_elements(comment)
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#title'
        val2 = '#View'
        eve_id = '319'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_222(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        print('icon click')
        self.finds_elements('//*[@id="eve_215"]')
        print('brand click')
        self.finds_elements('//*[@id="eve_222"]')
        print("brand menu")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Brand Name'
        val2 = ''
        eve_id = '222'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_223(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        self.finds_elements('//*[@id="eve_214"]')
        self.finds_elements('//*[@id="eve_223"]')
        
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Category Name'
        val2 = ''
        eve_id = '223'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_224(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '224'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_104(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_104"]/h3/a')
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Name'
        val2 = 'url'
        eve_id = '104'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_105(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_105"]/ul/li[1]/a')
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Name'
        val2 = 'url'
        eve_id = '105'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_106(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_106"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Name'
        val2 = 'url'
        eve_id = '106'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_107(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_107"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Name'
        val2 = 'url'
        eve_id = '107'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    
    def eve_59(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_59"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Name'
        val2 = 'url'
        eve_id = '59'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_61(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="all-product"]/div[1]/div[1]/div/p/a')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '61'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_62(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_62"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '62'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_79(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_77"]','a')
        self.finds_elements('//*[@id="wherewedeliverul"]/li[1]/div/a')
        self.driver.back()
        self.print_visitor_id()
        con = "BP"
        val1 = 'URL | Item Name'
        val2 = ''
        eve_id = '79'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_86(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_86"]')
        # self.finds_elements('//*[@id="wherewedeliverul"]/li[1]/div/a')
        # self.driver.back()
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '86'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_87(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_86"]')
        self.finds_elements('//*[@class="middle_east_click"]')
        # self.finds_elements('//*[@id="wherewedeliverul"]/li[1]/div/a')
        # self.driver.back()
        self.print_visitor_id()
        con = "BP"
        val1 = '#item'
        val2 = ''
        eve_id = '87'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_88(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_86"]')
        self.finds_elements('//*[@class="middle_east_click"]')
        self.finds_elements('//*[@id="africa-middle-east"]/ul/li[1]/div/div/div[1]/div[2]/p/a')
        self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#item'
        val2 = '#language'
        eve_id = '88'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    
    

    def eve_94(self,url):
        self.request_func(url)
        whatsapp = "//*[@id='eve_94']"
        self.finds_elements(whatsapp)
        self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '94'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_96(self,url):
        self.request_func(url)
        explore_pd = '//*[@id="eve_96"]/div/ul[1]/li[1]/a'
        self.finds_elements(explore_pd)
        self.print_visitor_id()
        con = "BPN"
        val1 = 'NAME'
        val2 = 'URL'
        eve_id = '96'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_335(self,url):
        self.request_func(url)
        ind_form  = "//*[@id='individualForm']" #//*[@id="individualForm"]
        self.finds_elements(ind_form)
        self.print_visitor_id()
        con = "BP"
        val1 = '#NAME'
        val2 = ''
        eve_id = '335'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_336(self,url):
        self.request_func(url)
        name  = "//*[@id='eve_336']" #//*[@id="individualForm"]
        self.finds_elements(name,'rahul')
        self.finds_elements("//*[@id='xyz']")
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '336'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_337(self,url):
        self.request_func(url)
        name  = "//*[@id='eve_337']" #//*[@id="individualForm"]
        self.finds_elements(name,'singh')
        self.finds_elements("//*[@id='xyz']")
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '337'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_338(self,url):
        self.request_func(url)
        company_f  = "//*[@id='companyForm']" #//*[@id="individualForm"]
        self.finds_elements(company_f)
        company  = "//*[@name='companyName']" #//*[@id="individualForm"]
        self.finds_elements(company,'rahul@raptorsupplies.co.uk')
        self.finds_elements("//*[@id='xyz']")
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '338'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_339(self,url):
        self.request_func(url)
        mail  = '//*[@id="eve_339"]'
        self.finds_elements(mail,'rahul@raptorsupplies.co.uk')
        self.finds_elements("//*[@id='xyz']")
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '339'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_335_company(self, url):
        self.request_func(url)
        self.chat_box_close()
        self.finds_elements('//*[@id="companyForm"]')
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '335'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_336_company(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="companyForm"]')
        comment = '//*[@id="eve_336"]'
        self.finds_elements(comment,'Archana')
        comment = '//*[@id="eve_337"]'
        self.finds_elements(comment,'Gautam')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '336'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_337_company(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="companyForm"]')
        comment = '//*[@id="eve_337"]'
        self.finds_elements(comment,'Gautam')
        comment = '//*[@id="eve_338"]'
        self.finds_elements(comment,'Raptor')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '337'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_338_company(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="companyForm"]')
        comment = '//*[@id="eve_338"]'
        self.finds_elements(comment,'Raptor')
        comment = '//*[@id="eve_339"]'
        self.finds_elements(comment,'raptor@gmail.com')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '338'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_339_company(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="companyForm"]')
        comment = '//*[@id="eve_339"]'
        self.finds_elements(comment,'raptor@gmail.com')
        password="(//*[@id='password'])"
        self.finds_elements(password,'445tg4')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '339'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    
    def eve_282(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="eve_282"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@id="eve_389"]', 'Archana')
        self.print_visitor_id()
        con = "BP"
        val1 = '#url'
        val2 = ''
        eve_id = '282'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)


    def eve_284(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="mycheckbox_844705_850574"]'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="compareClear"]/a')
        self.finds_elements(comment)
        self.print_visitor_id()
        con = "BP"
        val1 = 'URL1 | URL2 | URL3'
        val2 = ''
        eve_id = '284'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_15(self, url):
        self.request_func(url)
        add_to_cart = "//*[@id='eve_38']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        time.sleep(2)
        close_cart_popup = '//*[@id="eve_295"]'
        self.finds_elements(close_cart_popup)
        shop_cart = '//*[@class="cart_icon"]'
        self.finds_elements(shop_cart)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#pd count'
        val2 = ''
        eve_id = '15'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_300(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_299']")
        self.finds_elements("//*[@id='eve_300']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#cat name'
        val2 = ''
        eve_id = '300'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_303(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_302']")
        self.finds_elements("//*[@id='eve_303']/div/a")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#brand name'
        val2 = ''
        eve_id = '303'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_306(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@id='eve_306']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#lang name'
        val2 = 'url'
        eve_id = '306'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    # def eve_116(self, url):
    #     self.request_func(url)
    #     time.sleep(2)
    #     self.finds_elements('//*[@id="eve_116"]')
    #     self.print_visitor_id()
    #     con = "BPN"
    #     val1 = ''
    #     val2 = 'url'
    #     eve_id = '116'
    #     self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_230(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('/html/body', Keys.END)
        self.finds_elements('//*[@id="float_rfq_btn"]')
        print('rfq')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '230'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_122(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="eve_122"]/div[1]/div/h4/a'
        self.finds_elements(comment)
        self.driver.back()
        # self.finds_elements('//*[@id="eve_284"]')
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '122'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_269(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_13"]')
        print('sign in')
        self.finds_elements('//*[@id="email"]', 'devanshu@nextgenesolutions.com')
        print('username')
        self.finds_elements('//*[@id="pass"]', 'Devanshu@123')
        print('password')
        self.chat_box_close()
        self.finds_elements('//*[@id="send2"]')
        print('login')
        time.sleep(4)
        self.finds_elements('//*[@id="eve_13"]')
        self.finds_elements('//*[@id="account-nav"]/ul/li[2]')
        self.finds_elements('//*[@id="table_000000402"]/div[6]/span/span/span')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '269'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_270(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_13"]')
        print('sign in')
        self.finds_elements('//*[@id="email"]', 'devanshu@nextgenesolutions.com')
        print('username')
        self.finds_elements('//*[@id="pass"]', 'Devanshu@123')
        print('password')
        self.chat_box_close()
        self.finds_elements('//*[@id="send2"]')
        print('login')
        time.sleep(4)
        self.finds_elements('//*[@id="eve_13"]')
        self.finds_elements('//*[@id="account-nav"]/ul/li[2]')
        self.finds_elements('//*[@class="viewbtn"]')
        self.print_visitor_id()
        con = ""
        val1 = '#order no'
        val2 = ''
        eve_id = '270'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_271(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_13"]')
        print('sign in')
        self.finds_elements('//*[@id="email"]', 'devanshu@nextgenesolutions.com')
        print('username')
        self.finds_elements('//*[@id="pass"]', 'Devanshu@123')
        print('password')
        self.chat_box_close()
        self.finds_elements('//*[@id="send2"]')
        print('login')
        time.sleep(4)
        self.finds_elements('//*[@id="eve_13"]')
        self.finds_elements('//*[@id="account-nav"]/ul/li[2]')
        # self.finds_elements('//*[@class="viewbtn"]')
        self.print_visitor_id()
        con = ""
        val1 = '#order no'
        val2 = ''
        eve_id = '271'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_267(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_13"]')
        print('sign in')
        self.finds_elements('//*[@id="email"]', 'devanshu@nextgenesolutions.com')
        print('username')
        self.finds_elements('//*[@id="pass"]', 'Devanshu@123')
        print('password')
        # self.chat_box_close()
        self.finds_elements('//*[@id="send2"]')
        print('login')
        time.sleep(5)
        self.finds_elements('//*[@id="eve_13"]')
        self.finds_elements('//*[@id="account-nav"]/ul/li[2]/a')
        # self.finds_elements('//*[@id="account-nav"]/ul/li[2]/a')
        time.sleep(2)
        self.finds_elements('//*[@id="maincontent"]/div[2]/div[1]/section/div[2]/div/div/div/div[1]/ul/li[1]/a')
        # self.finds_elements('//*[@class="viewbtn"]')
        self.print_visitor_id()
        con = "BP"
        val1 = 'Menu_Name'
        val2 = ''
        eve_id = '267'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_269(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_13"]')
        print('sign in')
        self.finds_elements('//*[@id="email"]', 'devanshu@nextgenesolutions.com')
        print('username')
        self.finds_elements('//*[@id="pass"]', 'Devanshu@123')
        print('password')
        self.chat_box_close()
        self.finds_elements('//*[@id="send2"]')
        print('login')
        time.sleep(4)
        self.finds_elements('//*[@id="eve_13"]')
        self.finds_elements('//*[@id="account-nav"]/ul/li[2]') 
        self.finds_elements('//*[@id="table_000004463"]/div[6]/span/span/span')
        # self.finds_elements('//*[@class="viewbtn"]')
        self.print_visitor_id()
        con = ""
        val1 = '#order no'
        val2 = ''
        eve_id = '269'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_80(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="junking_color"]/li[2]/a')
        print('filter')
        # self.finds_elements('//*[@class="viewbtn"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '80'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_225(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        time.sleep(2)
        # self.finds_elements('//*[@id="at_23339"]/span[2]') 
        self.driver.execute_script('document.querySelector("#at_23339").click()')
        self.finds_elements('//*[@class="fileter-inner"]/label/span')
        self.print_visitor_id()
        con = ""
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '225'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_226(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        time.sleep(2)
        self.finds_elements('//*[@id="filtersection"]') 
        # self.driver.execute_script('document.querySelector("#at_23339").click()')
        self.finds_elements('//*[@id="a_25668"]','1/2"')
        self.print_visitor_id()
        con = ""
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '226'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_44(self, url):
        self.request_func(url)
        self.finds_elements("(//*[@id='main_rfq_btn'])")
        self.finds_elements('//*[@id="eve_44"]', 'uk')
        # self.finds_elements('//*[@id="shipping-form"]/div/div[3]/button')
        self.print_visitor_id()
        con = "BP"
        val1 = '# country name'
        val2 = '# new country name'
        eve_id = '44'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_21(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_21"]/ul/li[3]/a')
        
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '21'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_249(self, url):
        self.request_func(url)
        self.finds_elements("(//*[@id='eve_249'])")
        
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = '# url'
        eve_id = '249'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_344(self, url):
        self.request_func(url)
        time.sleep(4)
        # self.finds_elements("//*[@id='eve_344']")
        self.driver.refresh()
        time.sleep(2)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '344'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    
    def eve_5(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']",'qh7')
        pyautogui.press('enter')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '5'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_6(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']",'1asdgasg')
        pyautogui.press('enter')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '6'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_272(self, url):
        self.request_func(url)
        self.finds_elements("//*[@class='brandproductbox brandproductbox2 search_cards_innerWrap box_shadow_hover']/a")
        # pyautogui.press('enter')
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Result Number'
        val2 = ''
        eve_id = '272'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_273(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='sortName']")
        self.finds_elements('//*[@class="parent"]//ul//li')
        # self.chat_box_close()
        # self.finds_elements('//*[@class="submenu"]/li[3]')
        # pyautogui.press('enter')
        self.print_visitor_id()
        con = ""
        val1 = 'Name'
        val2 = ''
        eve_id = '273'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_12(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements('//*[@class="country-change"]')
        self.finds_elements('//*[@id="top_country_list"]','United Kingdom')
        time.sleep(2)
        self.finds_elements('//*[@id="eve_12"]')
        # self.chat_box_close()
        # self.finds_elements('//*[@class="submenu"]/li[3]')
        # pyautogui.press('enter')
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Name'
        val2 = 'Name'
        eve_id = '12'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_98(self, url):
        self.request_func(url)
        email = '//*[@id="eve_98"]'
        self.finds_elements(email)
        pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '98'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_99(self, url):
        self.request_func(url)
        phone = '//*[@id="eve_99"]'
        self.finds_elements(phone)
        pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '99'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_100(self, url):
        self.request_func(url)
        wpt = '//*[@id="eve_100"]'
        self.finds_elements(wpt)
        self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '100'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_63(self, url):
        self.request_func(url)
        self.finds_elements('//*[@class="rfq-btn"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '63'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_386(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_386"]/ul/li[2]/a/p/strong'
        self.finds_elements(comment)
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '386'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_7(self, url):
        self.request_func(url)
        comment = '//*[@id="search"]'
        self.finds_elements(comment,'morse')
        # pyautogui.press('enter')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '7'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_8(self, url):
        self.request_func(url)
        comment = '//*[@id="search"]'
        self.finds_elements(comment,'morse')
        pyautogui.press('enter')
        self.driver.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '8'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_404(self, url):
        self.request_func(url)
        rfq = '//*[@class="rfq-btn"]'
        self.finds_elements(rfq)
        
        self.print_visitor_id()
        con = ""
        val1 = 'VAl'
        val2 = 'mpn'
        eve_id = '404'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_120(self, url):
        self.request_func(url)
        cat = '//*[@id="eve_120"]/div[1]/div/div[1]/div/ul/li[1]/a'
        self.finds_elements(cat)
        
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Name'
        val2 = 'Url'
        eve_id = '120'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_198(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        click_On_Checkout="//*[@id='eve_294']"
        self.finds_elements( click_On_Checkout)
        #Postal code
        postal_Code="(//*[@name='postcode'])"
        self.finds_elements(postal_Code,123456)
        #Contact number
        phone_number="(//*[@name='telephone'])"
        self.finds_elements(phone_number,1234567890)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '198'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_388(self, url):
        self.request_func(url)
        comment = '//*[@id="maindis"]/div/table/tbody/tr[1]'
        self.finds_elements(comment)
        # self.driver.back()
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '388'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_393(self, url):
        self.request_func(url)
        comment = '//*[@id="maindis"]/div/table/tbody/tr[1]/td[5]/button'
        self.finds_elements(comment)
        # self.driver.back()
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '393'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_294(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart = "//*[@id='eve_38']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        self.driver.back()
        self.print_visitor_id()
        con = "BP"
        val1 = 'val1'
        val2 = 'val2'
        eve_id = '294'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_402(self, url):
        self.request_func(url)
        rfq = '//*[@id="main_rfq_btn"]'
        self.element_hover(rfq)
        self.finds_elements(rfq)
        self.finds_elements('//*[@id="eve_43"]', 'Automation testing')
        self.finds_elements('//*[@id="shipping-form"]/div/div[3]/button')
        element = self.driver.find_element(By.XPATH,'//*[@id="eve_402"]')
        self.driver.execute_script("arguments[0].click();", element)
        # self.finds_elements('//*[@id="eve_402"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '402'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_377(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_377"]'
        self.finds_elements(comment,'Archana')
        self.finds_elements('//*[@id="382"]')
        self.print_visitor_id()
        con = ""
        val1 = '# text'
        val2 = ''
        eve_id = '377'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_378(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_378"]'
        self.finds_elements(comment,'archana@raptor.com')
        self.finds_elements('//*[@id="382"]')
        self.print_visitor_id()
        con = ""
        val1 = '# text'
        val2 = ''
        eve_id = '378'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_378(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_378"]'
        self.finds_elements(comment,'archana@raptor.com')
        self.finds_elements('//*[@id="382"]')
        self.print_visitor_id()
        con = ""
        val1 = '# text'
        val2 = ''
        eve_id = '378'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_379(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_379"]'
        self.finds_elements(comment,'999999999')
        self.finds_elements('//*[@id="382"]')
        self.print_visitor_id()
        con = ""
        val1 = '# text'
        val2 = ''
        eve_id = '379'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_380(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_380"]'
        self.finds_elements(comment,'India')
        self.finds_elements('//*[@id="382"]')
        self.print_visitor_id()
        con = ""
        val1 = '# text'
        val2 = ''
        eve_id = '380'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_381(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_381"]'
        self.finds_elements(comment,'testing')
        self.finds_elements('//*[@id="382"]')
        self.print_visitor_id()
        con = ""
        val1 = '# text'
        val2 = ''
        eve_id = '381'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_360(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']",'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/div[2]')
        # self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'val1'
        val2 = 'val2'
        eve_id = '360'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_361(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']",'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        # self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_362(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']",'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        # self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_274(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_274"]')
        # self.driver.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '274'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_275(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_275"]')
        # self.driver.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '275'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_276(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_276"]')
        # self.driver.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '276'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_124(self,url):
        self.request_func(url)
        
        #RFQ Name
        name_in_Form="(//*[@id='eve_124'])"
        self.finds_elements(name_in_Form,'xyz')
        click_On_Get_A_Quote="(//*[text()='Get Quote Now'])"
        self.finds_elements(click_On_Get_A_Quote)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Text'
        val2 = ''
        eve_id = '124'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_125(self,url):
        self.request_func(url)
        
        #RFQ Email
        email_in_Form="(//*[@id='eve_125'])"
        self.finds_elements(email_in_Form,'shubham@raptorsupplies.co.uk')
        #Click on Get a Quote
        click_On_Get_A_Quote="(//*[text()='Get Quote Now'])"
        self.finds_elements(click_On_Get_A_Quote) 
        self.print_visitor_id()
        con = "BP"
        val1 = '#Text'
        val2 = ''
        eve_id = '125'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_126(self,url):
        self.request_func(url)
        
        #RFQ Contact Number
        phoneNo_in_Form="(//*[@id='eve_126'])"
        self.finds_elements(phoneNo_in_Form,1234567890)
        #Click on Get a Quote
        click_On_Get_A_Quote="(//*[text()='Get Quote Now'])"
        self.finds_elements(click_On_Get_A_Quote)  
        self.print_visitor_id()
        con = "BP"
        val1 = '#Text'
        val2 = ''
        eve_id = '126'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_127(self,url):
        self.request_func(url)
        
        #RFQ country dropdown
        countryDropdown_in_Form="(//*[@id='eve_127'])"
        self.finds_elements(countryDropdown_in_Form,'Brazil')
        #Click on Get a Quote
        click_On_Get_A_Quote="(//*[text()='Get Quote Now'])"
        self.finds_elements(click_On_Get_A_Quote) 
        self.print_visitor_id()
        con = "BP"
        val1 = '#Text'
        val2 = ''
        eve_id = '127'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_128(self,url):
        self.request_func(url)
        self.chat_box_close()
        #RFQ What items do  you need
        Items="(//*[@id='eve_128'])"
        self.finds_elements(Items,'Electronics')
        #Click on Get a Quote
        click_On_Get_A_Quote="(//*[text()='Get Quote Now'])"
        self.finds_elements(click_On_Get_A_Quote) 
        self.print_visitor_id()
        con = "BP"
        val1 = '#Text'
        val2 = ''
        eve_id = '128'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_129(self,url):
        self.request_func(url)
        self.chat_box_close()
        #submit_your_failure
        captcha="(//*[@class='recaptcha-checkbox-border'])"
        self.finds_elements(captcha)
        #Click on Get a Quote
        click_On_Get_A_Quote="(//*[text()='Get Quote Now'])"
        self.finds_elements(click_On_Get_A_Quote) 
        self.print_visitor_id()
        con = "BP"
        val1 = '#Text'
        val2 = ''
        eve_id = '129'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_130(self,url):
        self.request_func(url)
        self.chat_box_close()
        #Name
        name_in_Form="(//*[@id='eve_124'])"
        self.finds_elements(name_in_Form,'xyz')
        #RFQ Email
        email_in_Form="(//*[@id='eve_125'])"
        self.finds_elements(email_in_Form,'shubham@raptorsupplies.co.uk')
        #RFQ Contact Number
        phoneNo_in_Form="(//*[@id='eve_126'])"
        self.finds_elements(phoneNo_in_Form,1234567890)
        #RFQ country dropdown
        countryDropdown_in_Form="(//*[@id='eve_127'])"
        self.finds_elements(countryDropdown_in_Form,'Brazil')
        #RFQ What items do  you need
        Items="(//*[@id='eve_128'])"
        self.finds_elements(Items,'Electronics')
        #Click on Get a Quote
        click_On_Get_A_Quote="(//*[text()='Get Quote Now'])"
        self.finds_elements(click_On_Get_A_Quote) 
        self.print_visitor_id()
        con = "BP"
        val1 = 'Email ID | Checked Box: (True/False)'
        val2 = 'Phone'
        eve_id = '130'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_383(self,url):
        self.request_func(url)
        self.chat_box_close()
        #Name
        name_in_Form="(//*[@id='eve_124'])"
        self.finds_elements(name_in_Form,'Raptor')
        #RFQ Email
        email_in_Form="(//*[@id='eve_125'])"
        self.finds_elements(email_in_Form,'shubham@raptorsupplies.co.uk')
        #RFQ Contact Number
        phoneNo_in_Form="(//*[@id='eve_126'])"
        self.finds_elements(phoneNo_in_Form,1234567890)
        #RFQ country dropdown
        countryDropdown_in_Form="(//*[@id='eve_127'])"
        self.finds_elements(countryDropdown_in_Form,'Brazil')
        #RFQ What items do  you need
        Items="(//*[@id='eve_128'])"
        self.finds_elements(Items,'Electronics')
        #Click on checkbox
        click_On_Checkbox="(//*[@class='checkmark'])"
        self.finds_elements(click_On_Checkbox)
        #Click on Get a Quote
        click_On_Get_A_Quote="(//*[text()='Get Quote Now'])"
        self.finds_elements(click_On_Get_A_Quote) 
        self.print_visitor_id()
        con = "BP"
        val1 = 'Email ID'
        val2 = ''
        eve_id = '383'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_384(self,url):
        self.request_func(url)
        self.chat_box_close()
        #Name
        name_in_Form="(//*[@id='eve_124'])"
        self.finds_elements(name_in_Form,'Raptor')
        #RFQ Email
        email_in_Form="(//*[@id='eve_125'])"
        self.finds_elements(email_in_Form,'shubham@raptorsupplies.co.uk')
        #RFQ Contact Number
        phoneNo_in_Form="(//*[@id='eve_126'])"
        self.finds_elements(phoneNo_in_Form,1234567890)
        #RFQ country dropdown
        countryDropdown_in_Form="(//*[@id='eve_127'])"
        self.finds_elements(countryDropdown_in_Form,'Brazil')
        #RFQ What items do  you need
        Items="(//*[@id='eve_128'])"
        self.finds_elements(Items,'Electronics')
        #Click on checkbox
        click_On_Checkbox="(//*[@class='checkmark'])"
        self.finds_elements(click_On_Checkbox)
        #uncheck the checkbox subscription
        uncheck__Checkbox="(//*[@class='checkmark'])"
        self.finds_elements( uncheck__Checkbox)
        #Click on Get a Quote
        click_On_Get_A_Quote="(//*[text()='Get Quote Now'])"
        self.finds_elements(click_On_Get_A_Quote) 
        self.print_visitor_id()
        con = "BP"
        val1 = 'Email ID'
        val2 = ''
        eve_id = '384'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

#Contact Us
    def eve_236(self, url):
        self.request_func(url)
        time.sleep(1)
        self.finds_elements('//*[@id="eve_236"]')

        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '236'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_237(self, url):
        self.request_func(url)
        time.sleep(1)
        self.finds_elements('//*[@id="eve_237"]')

        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '237'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

      

    def eve_238(self, url):
        self.request_func(url)
        time.sleep(1)
        self.finds_elements('//*[@id="eve_238"]')

        self.print_visitor_id()
        con = "BP"
        val1 = '#value'
        val2 = ''
        eve_id = '238'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_239(self, url):
        self.request_func(url)
        time.sleep(1)
        self.finds_elements('//*[@id="eve_239"]')

        self.print_visitor_id()
        con = "BP"
        val1 = '#value'
        val2 = ''
        eve_id = '239'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)    


    def eve_240(self, url):
        self.request_func(url)
        time.sleep(1)
        self.finds_elements('//*[@id="eve_240"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#value'
        val2 = ''
        eve_id = '240'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)    

    def eve_241(self, url):
        self.request_func(url)
        time.sleep(1)
        self.finds_elements('//*[@id="eve_241"]')
        self.print_visitor_id()
        con = "BP"
        val1 ='#value'
        val2 = ''
        eve_id = '241'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)  

    def eve_242(self, url):
        self.request_func(url)
        time.sleep(1)
        self.finds_elements('//*[@id="eve_242"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#value'
        val2 = ''
        eve_id = '242'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)  

    def eve_243(self, url):
        self.request_func(url)
        time.sleep(1)
        self.finds_elements('//*[@id="eve_243"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#value'
        val2 = ''
        eve_id = '243'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id) 

    def eve_244(self, url):
        self.request_func(url)
        time.sleep(1)
        self.finds_elements('//*[@id="eve_236"]')
        self.finds_elements('//*[@id="tab4C"]/ul/li[1]')

        self.print_visitor_id()
        con = "BP"
        val1 = '#Name-Header'
        val2 = ''
        eve_id = '244'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_70(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="eve_70"]/ul/li[2]/a'
        self.finds_elements(comment)
        # self.finds_elements('//*[@id="eve_284"]')
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BP"
        val1 = '#filedname'
        val2 = ''
        eve_id = '70'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_285(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="mycheckbox_844705_850574"]'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="mycheckbox_5165768_5165947"]')
        self.finds_elements('//*[@id="mycheckbox_5165773_5165947"]')
        self.finds_elements('//*[@id="open-modal"]')
        self.print_visitor_id()
        con = "BP"
        val1 = 'URL1|URL2|URL3'
        val2 = ''
        eve_id = '285'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_111(self, url):
        self.request_func(url)
        comment = '//*[@id="gridViewSwitch"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#previouse view'
        val2 = '#nextview'
        eve_id = '111'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_72(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_72"]'
        self.finds_elements(comment)
        self.driver.back()
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = '# Mother title'
        val2 = '#View'
        eve_id = '72'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_110(self, url):
        self.request_func(url)
        comment = '//*[@id="atc_3"]/span'
        self.finds_elements(comment)
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#Product Title/Model Number'
        val2 = 'Viewname'
        eve_id = '110'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    
    def eve_103(self, url):
        self.request_func(url)
        comment = '//*[@class="add_cart caterfq"]'
        self.finds_elements(comment)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Product Title | Model Number'
        val2 = 'View name'
        eve_id = '103'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_109(self, url):
        self.request_func(url)
        comment = '//*[@id="row0_1"]'
        self.finds_elements(comment)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Product Title'
        val2 = ''
        eve_id = '109'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_69(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_69"]'
        self.finds_elements(comment)
        self.driver.back()
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = '3title'
        val2 = 'image'
        eve_id = '69'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_71(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_71"]/label/div[1]/img'
        self.finds_elements(comment)
        self.driver.back()
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = '#category'
        val2 = 'Title'
        eve_id = '71'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_73(self, url):
        self.request_func(url)
        comment = '//*[@id="row2"]/td[2]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#Mother title'
        val2 = '#View'
        eve_id = '73'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id) 


    def eve_113(self, url):
        self.request_func(url)
       
        self.finds_elements('//*[@id="parent_"]/table/tbody/tr[1]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = '#text'
        eve_id = '113'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
        

    def eve_114(self, url):
        self.request_func(url)
        self.finds_elements('//*[@class="addto_cart"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#quantity | Title'
        val2 = 'View name'
        eve_id = '114'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_115(self, url):
        self.request_func(url)
        self.finds_elements('//*[@class="rfq-btn"]')

        self.print_visitor_id()
        con = "BP"
        val1 = '#title'
        val2 = '#viewname'
        eve_id = '115'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_347(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="gridViewSwitch"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#privous view'
        val2 = 'Next veiw'
        eve_id = '347'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_287(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_287"]', 'comment')
        self.finds_elements('//*[@id="ksb_but"]')

        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '287'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_286(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_286"]', 'archanagautam@gmail.com')
        self.finds_elements('//*[@id="ksb_but"]')
        
        self.print_visitor_id()
        con = "BP"
        val1 = '#email'
        val2 = ''
        eve_id = '286'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)    

    
    
    

    def eve_245(self, url):
        self.request_func(url)
        time.sleep(1)
        self.finds_elements('//*[@id="eve_245"]')
        self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '245'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_246(self, url):
        self.request_func(url)
        time.sleep(1)
        self.finds_elements('//*[@id="eve_246"]')
        self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '246'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_247(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_247"]')
        self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '247'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_248(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_248"]')
        self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '248'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)


    def eve_148(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_148"]'
        self.finds_elements(comment,'Archana')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '148'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_149(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_149"]'
        self.finds_elements(comment,'archana@raptor.com')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '149'

        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)    
 

    def eve_150(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_150"]'
        self.finds_elements(comment,'999999999')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '150'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)   

    def eve_151(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_151"]'
        self.finds_elements(comment,'testing')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '151'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)  


    def eve_389(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="maindis"]/div/table/tbody/tr[2]/td[5]/button'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="eve_389"]', 'Archana')
        self.finds_elements('//*[@id="eve_397"]/div/div[2]/div[5]/button')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '389'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)


    def eve_121(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="eve_121"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@id="eve_284"]')
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        
        val2 = ''
        eve_id = '121'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id) 

    def eve_117(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="eve_117"]'
        self.finds_elements(comment)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#name'
        
        val2 = '#URL'
        eve_id = '117'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)  

    def eve_116(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="promotionalslid"]/div[2]/button[2]'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="promotionalslid"]/div[1]/div/div[4]/div/div/div')
        # self.finds_elements('//*[@id="eve_284"]')
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        
        val2 = '#URL'
        eve_id = '116'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)   

    def eve_119(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="eve_11"]'
        self.finds_elements(comment)
        self.print_visitor_id()
        con ="BPN"
        val1 = ''
        val2 = ''
        eve_id = '119'
        
    
    def eve_118(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="eve_118"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@id="eve_284"]')
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#name'
        val2 = '#URL'
        eve_id = '118'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)  

    


    def eve_122(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="eve_122"]/div[1]/div/h4/a'
        self.finds_elements(comment)
        self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#blog_title'
        val2 = ''
        eve_id = '122'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    

    def eve_66(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="eve_66"]/button/i'
        self.finds_elements(comment, 'vestil')
        pyautogui.press('enter')
        # self.finds_elements('//*[@id="eve_284"]')
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Filter name'
        
        val2 = 'position'
        eve_id = '66'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_67(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="eve_67"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@id="eve_284"]')
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Filter name'
        val2 = '#filtervale'
        eve_id = '67'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_68(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="eve_68"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@id="eve_284"]')f
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Filter name'
        val2 = 'filter value'
        eve_id = '68'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_69(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_69"]'
        self.finds_elements(comment)
        self.driver.back()
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = '#title'
        val2 = 'image'
        eve_id = '69'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    

    def eve_134(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_134"]'
        self.finds_elements(comment,'raptor')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '134'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_133(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_133"]'
        self.finds_elements(comment,'999999999')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '133'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_132(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_132"]'
        self.finds_elements(comment,'raptor@supples.com')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '132'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)   

    def eve_163(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_163"]'
        self.finds_elements(comment,'RAptor')
        self.finds_elements('//*[@id="next-btn2"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '163'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_164(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_164"]'
        self.finds_elements(comment,'12324')
        # pyautogui.press('enter')
        # self.driver.back()
        self.finds_elements('//*[@id="next-btn2"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '164'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_166(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_166"]'
        self.finds_elements(comment,'234')
        self.finds_elements('//*[@id="next-btn2"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '166'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_168(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_168"]'
        self.finds_elements(comment,'a1k/2d')
        self.finds_elements('//*[@id="next-btn2"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '168'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_169(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_169"]'
        self.finds_elements(comment,'delhi')
        self.finds_elements('//*[@id="next-btn2"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '169'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
        

    def eve_170(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_170"]'
        self.finds_elements(comment,'110076')
        self.finds_elements('//*[@id="next-btn2"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '170'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    #Shopping_Cart

    def eve_350(self,url):
        self.request_func(url)
        add_to_cart ="//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close() 
        click_On_View_Cart="(//*[@id='eve_293'])"
        self.finds_elements( click_On_View_Cart)
        print_button="(//*[@id='eve_350'])"
        self.finds_elements( print_button)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '350'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_179(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart="(//*[@id='eve_293'])"
        self.finds_elements( click_On_View_Cart)
        # close_popup="(//*[@id='Path_5'])"
        # self.finds_elements(close_popup)
        click_On_Product='//*[@class="product_details_inner"]/a'
        self.finds_elements(click_On_Product)
        self.print_visitor_id()
        con = "BP"
        val1 = 'SKU'
        val2 = 'Title'
        eve_id = '179'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_180(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart="(//*[@id='eve_293'])"
        self.finds_elements( click_On_View_Cart)
        #Add_Quantity
        add_Quantity="(//*[@id='eve_180'])"
        self.finds_elements(add_Quantity)
        self.print_visitor_id()
        con = "BP"
        val1 = '# Quantity Before'
        val2 = '# Quantity After'
        eve_id = '180'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_181(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart="(//*[@id='eve_293'])"
        self.finds_elements( click_On_View_Cart)
        #Add_Quantity
        add_Quantity="(//*[@id='eve_180'])"
        self.finds_elements(add_Quantity)
        #Reduce Quantity
        reduce_Quantity="(//*[@id='eve_181'])"
        self.finds_elements(reduce_Quantity)
        self.print_visitor_id()
        con = "BP"
        val1 = '# Quantity Before'
        val2 = '# Quantity After'
        eve_id = '181'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

   
    def eve_182(self,url):
        self.request_func(url)
        add_to_cart ="//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart="(//*[@id='eve_293'])"
        self.finds_elements( click_On_View_Cart)
        #Trash Bin
        click_On_Trash_bin="(//*[@id='eve_182'])"
        self.finds_elements(click_On_Trash_bin)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Title'
        val2 = '# '
        eve_id = '182'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_184(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart="(//*[@id='eve_293'])"
        self.finds_elements( click_On_View_Cart)
        #Country Dropdown
        click_On_Country_Dropdown="(//*[@alt='country-flag'])"
        self.finds_elements(click_On_Country_Dropdown)
        change_country="(//*[text()='Change Country'])"
        self.finds_elements(change_country)
        country_dropdown="(//*[@id='top_country_list'])"
        self.finds_elements(country_dropdown,"India")
        self.print_visitor_id()
        con = "BP"
        val1 = 'Current Country'
        val2 = 'Selected Country'
        eve_id = '184'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_185(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart="(//*[@id='eve_293'])"
        self.finds_elements( click_On_View_Cart)
        #Shipping Country Details
        country_Shipping="(//*[@name='country_id'])"
        self.finds_elements(country_Shipping,'Bangladesh')
        #Mode of Shipping
        try:
            self.driver.find_element(By.XPATH, '//*[@class="table-checkout-shipping-method shipping_info_label_wrp"]').find_element(By.TAG_NAME, 'td').click()
        except Exception as e:
            print(e)
        
        #ExWorks_Pickup="(//*[@id='s_method_freeshipping_freeshipping'])"
        #self.finds_elements(ExWorks_Pickup)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Mode of Shipment'
        val2 = 'Freight Charge'
        eve_id = '185'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)


    def eve_186(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart="(//*[@id='eve_293'])"
        self.finds_elements( click_On_View_Cart)
        #Shipping Country Details
        country_Shipping="(//*[@name='country_id'])"
        self.finds_elements(country_Shipping,'Bangladesh')
        #Mode of Shipping
        #select_Express="(//*[@id='s_method_matrixrate_matrixrate_19244'])"
        #self.finds_elements(select_Express)
        #Discount Code
        apply_Discount_Code="(//*[@id='coupon_code'])"
        self.finds_elements(apply_Discount_Code,'FAB5')
        click_On_Apply="(//*[@id='eve_186'])"
        self.finds_elements( click_On_Apply)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Discount code | <Discount Status(Applied/"Please enter valid Coupan>'
        val2 = 'Subtotal with Currecny'
        eve_id = '186'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)


    def eve_187(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart="(//*[@id='eve_293'])"
        self.finds_elements( click_On_View_Cart)
        #Shipping Country Details
        #self.finds_elements(apply_Discount_Code,'FAB5')
        #click_On_Apply="(//*[@id='eve_186'])"
        #self.finds_elements( click_On_Apply)
        #Checkout_Button
        click_On_Checkout_Button="(//*[@id='eve_187'])"
        self.finds_elements(click_On_Checkout_Button)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = 'Subtotal with Currecny'
        eve_id = '187'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_190(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart="(//*[@id='eve_293'])"
        self.finds_elements( click_On_View_Cart)
        click_on_TC='(//*[@id="eve_190"])'
        self.finds_elements(click_on_TC)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Text (Email id)'
        val2 = ''
        eve_id = '190'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_188(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart="//*[@id='eve_293']"
        self.finds_elements( click_On_View_Cart)
        enter_email='//*[@id="eve_188"]'
        self.finds_elements(enter_email,"shubham@raptorsupplies.co.uk")
        self.finds_elements('//*[@id="eve_349"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Text (Email id)'
        val2 = ''
        eve_id = '188'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    
    def eve_352(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close() 
        click_On_View_Cart="(//*[@id='eve_293'])"
        self.finds_elements( click_On_View_Cart)
        delete_popup="(//*[@id='eve_182'])"
        self.finds_elements(delete_popup)
        remove="(//*[@id='eve_352'])"
        self.finds_elements(remove)

        self.print_visitor_id()
        con = "BP"
        val1 = 'SKU | Quantity | item Value'
        val2 = 'Type of Click ("Cancel"/"Remove"/"Cross")'
        eve_id = '352'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_97(self,url):
        self.request_func(url)
        add_to_cart ="//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close() 
        click_On_View_Cart="(//*[@id='eve_293'])"
        self.finds_elements( click_On_View_Cart)
        trust_Pilot="(//*[@id='eve_97'])"
        self.finds_elements(trust_Pilot)
        
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '97'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    
    def eve_399(self,url):
        self.request_func(url)
        add_to_cart ="//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close() 
        click_On_View_Cart="(//*[@id='eve_293'])"
        self.finds_elements( click_On_View_Cart)
        save_pdf="(//*[@id='eve_350'])"
        self.finds_elements( save_pdf)
        pdf="(//*[@class='print-cart save-as-pdf'])"
        self.finds_elements(pdf)
        
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '399'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    
    def eve_400(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close() 
        click_On_View_Cart="(//*[@id='eve_293'])"
        self.finds_elements( click_On_View_Cart)
        #Discount Code
        apply_Discount_Code="(//*[@id='coupon_code'])"
        self.finds_elements(apply_Discount_Code,'FAB5')
        click_On_Apply="(//*[@id='eve_186'])"
        self.finds_elements( click_On_Apply)
        cross='(//*[@id="Group_5"])'
        self.finds_elements(cross)
        remove_discount="(//*[@id='eve_400'])"
        self.finds_elements(remove_discount)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Coupon Code'
        val2 = ''
        eve_id = '400'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    #CheckOUT Page
    def eve_192(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[text()='Checkout'])"
        self.finds_elements( click_On_Checkout)
        #Shipping Information

        email_Address="//*[@id='customer-email']"
        self.finds_elements(email_Address,'shubham@raptorsupplies.co.uk')
        first_Name="(//*[@name='firstname'])"
        self.finds_elements(first_Name,'Abc')
        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '192'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
 
    def eve_193(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #checkout
        click_On_Checkout="(//*[text()='Checkout'])"
        self.finds_elements(click_On_Checkout)
        #Company Name
        company_Name="(//*[@name='company'])"
        self.finds_elements(company_Name,'Raptor')
        #Address
        address="(//*[@name='street[0]'])"
        self.finds_elements(address,'UK')
        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '193'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_194(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[text()='Checkout'])"
        self.finds_elements( click_On_Checkout)
        #Address
        address="(//*[@name='street[0]'])"
        self.finds_elements(address,'UK')
        #city Name
        city_Name="(//*[@name='city'])"
        self.finds_elements(city_Name,'abc')
        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '194'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_195(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[text()='Checkout'])"
        self.finds_elements( click_On_Checkout)
        #City_Name
        city_Name="(//*[@name='city'])"
        self.finds_elements(city_Name,'abc')
        #Country dropdown
        country_Dropdown="(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown,'Egypt')
        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '195'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_196(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart ="//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        #Country Dropdown
        country_Dropdown="(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown,'Oman')
        #State
        state_Or_Province="(//*[@name='region_id'])"
        self.finds_elements(state_Or_Province,'Goa')
        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '196'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_197(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        #Country Dropdown
        country_Dropdown="(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown,'India')
        #State dropdown
        state_Or_Province="(//*[@name='region_id'])"
        self.finds_elements(state_Or_Province,'Assam')
        #Postal code
        postal_Code="(//*[@name='postcode'])"
        self.finds_elements(postal_Code,123456)

        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '197'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_198(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        #Postal code
        postal_Code="(//*[@name='postcode'])"
        self.finds_elements(postal_Code,123456)
        #Contact number
        phone_number="(//*[@name='telephone'])"
        self.finds_elements(phone_number,1234567890)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '198'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_199(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        #Contact number
        phone_number="(//*[@name='telephone'])"
        self.finds_elements(phone_number,1234567890)
        #Click on continue or submit
        click_On_continue="//*[@name='postcode']"
        self.finds_elements(click_On_continue)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '199'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_200(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        #Email Id
        email_Address="(//*[@id='customer-email'])"
        self.finds_elements(email_Address,'shubham@raptorsupplies.co.uk')
        #First Name
        first_Name="(//*[@name='firstname'])"
        self.finds_elements(first_Name,'Abc')
        #Last Name
        last_Name="(//*[@name='lastname'])"
        self.finds_elements(last_Name,'Kumar')
        #Company Name
        company_Name="(//*[@name='company'])"
        self.finds_elements(company_Name,'Raptor')
        #Address
        address="(//*[@name='street[0]'])"
        self.finds_elements(address,'UK')
        #City_Name
        city_Name="(//*[@name='city'])"
        self.finds_elements(city_Name,'abc')
        #Country dropdown
        country_Dropdown="(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown,'Egypt')
        #State dropdown
        state_Or_Province="(//*[@name='region_id'])"
        self.finds_elements(state_Or_Province,'Goa')
        #Postal code
        postal_Code="(//*[@name='postcode'])"
        self.finds_elements(postal_Code,123456)
        #Contact number
        phone_number="(//*[@name='telephone'])"
        self.finds_elements(phone_number,1234567890)
        #Click on continue or submit
        click_On_continue="(//*[@id='eve_200'])"
        self.finds_elements(click_On_continue)
       
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Email'
        val2 = ''
        eve_id = '200'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_201(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        #Email Id
        email_Address="(//*[@id='customer-email'])"
        self.finds_elements(email_Address,'shubham@raptorsupplies.co.uk')
        #First Name
        first_Name="(//*[@name='firstname'])"
        self.finds_elements(first_Name,'Abc')
        #Last Name
        last_Name="(//*[@name='lastname'])"
        self.finds_elements(last_Name,'Kumar')
        #Company Name
        company_Name="(//*[@name='company'])"
        self.finds_elements(company_Name,'Raptor')
        #Address
        address="(//*[@name='street[0]'])"
        self.finds_elements(address,'UK')
        #City_Name
        city_Name="(//*[@name='city'])"
        self.finds_elements(city_Name,'abc')
        #Country dropdown
        country_Dropdown="(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown,'India')
        #State dropdown
        state_Or_Province="(//*[@name='region_id'])"
        self.finds_elements(state_Or_Province,'Goa')
        #Postal code
        postal_Code="(//*[@name='postcode'])"
        self.finds_elements(postal_Code,123456)
        #Contact number
        phone_number="(//*[@name='telephone'])"
        self.finds_elements(phone_number,1234567890)
        #Click on continue or submit
        click_On_continue="(//*[@id='eve_200'])"
        self.finds_elements(click_On_continue)
        #Express 5 to 7 Days
        self.driver.find_element(By.XPATH, '//*[@class="table-checkout-shipping-method shipping_info_label_wrp"]').find_element(By.TAG_NAME, 'td').click()
        # self.finds_elements(express_Clicking)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Freight Amount'
        val2 = 'shiping method'
        eve_id = '201'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)


    def eve_203(self,url):
        self.request_func(url)
         #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        email_Address="(//*[@id='customer-email'])"
        self.finds_elements(email_Address,'shubham@raptorsupplies.co.uk')
        first_Name="(//*[@name='firstname'])"
        self.finds_elements(first_Name,'Abc')
        #Last Name
        last_Name="(//*[@name='lastname'])"
        self.finds_elements(last_Name,'Kumar')
        #Company Name
        company_Name="(//*[@name='company'])"
        self.finds_elements(company_Name,'Raptor')
        #Address
        address="(//*[@name='street[0]'])"
        self.finds_elements(address,'UK')
        #City_Name
        city_Name="(//*[@name='city'])"
        self.finds_elements(city_Name,'abc')
        #Country dropdown
        country_Dropdown="(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown,'Egypt')
        #State dropdown
        # state_Or_Province="(//*[@name='region_id'])"
        # self.finds_elements(state_Or_Province,'Goa')
        #Postal code
        postal_Code="(//*[@name='postcode'])"
        self.finds_elements(postal_Code,123456)
        #Contact number
        phone_number="(//*[@name='telephone'])"
        self.finds_elements(phone_number,1234567890)
        #Click on continue or submit
        click_On_continue="(//*[@id='eve_200'])"
        self.finds_elements( click_On_continue)
        #Ex-Works Pickup
        self.driver.find_element(By.XPATH, '//*[@id="checkout-shipping-method-load"]/table/tbody/tr[2]').click()
        time.sleep(2)
        select_Shippping_Courier="//*[@id='eve_203']"
        self.finds_elements(select_Shippping_Courier)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Courier Name'
        val2 = ''
        eve_id = '203'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_204(self,url):
        self.request_func(url)
         #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        email_Address="(//*[@id='customer-email'])"
        self.finds_elements(email_Address,'shubham@raptorsupplies.co.uk')
        first_Name="(//*[@name='firstname'])"
        self.finds_elements(first_Name,'Abc')
        #Last Name
        last_Name="(//*[@name='lastname'])"
        self.finds_elements(last_Name,'Kumar')
        #Company Name
        company_Name="(//*[@name='company'])"
        self.finds_elements(company_Name,'Raptor')
        #Address
        address="(//*[@name='street[0]'])"
        self.finds_elements(address,'UK')
        #City_Name
        city_Name="(//*[@name='city'])"
        self.finds_elements(city_Name,'abc')
        #Country dropdown
        country_Dropdown="(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown,'Egypt')
        #State dropdown
        # state_Or_Province="(//*[@name='region_id'])"
        # self.finds_elements(state_Or_Province,'Goa')
        #Postal code
        postal_Code="(//*[@name='postcode'])"
        self.finds_elements(postal_Code,123456)
        #Contact number
        phone_number="(//*[@name='telephone'])"
        self.finds_elements(phone_number,1234567890)
        #Click on continue or submit
        click_On_continue="(//*[@id='eve_200'])"
        self.finds_elements( click_On_continue)
        #Ex-Works Pickup
        self.driver.find_element(By.XPATH, '//*[@id="checkout-shipping-method-load"]/table/tbody/tr[2]').click()
        
        #select shipping courier methods
        select_Shippping_Courier="(//*[@id='eve_203'])"
        self.finds_elements(select_Shippping_Courier)
       #Pass ExWork-Account Number
        account_Number="(//*[@id='eve_204'])"
        self.finds_elements(account_Number,24654743254)

        self.print_visitor_id()
        con = "BP"
        val1 = '#Text'
        val2 = ''
        eve_id = '204'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)



    def eve_205(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart ="//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        #Shipping Information
        #Email Id
        email_Address="(//*[@id='customer-email'])"
        self.finds_elements(email_Address,'shubham@raptorsupplies.co.uk')
        #First Name
        first_Name="(//*[@name='firstname'])"
        self.finds_elements(first_Name,'Abc')
        #Last Name
        last_Name="(//*[@name='lastname'])"
        self.finds_elements(last_Name,'Kumar')
        #Company Name
        company_Name="(//*[@name='company'])"
        self.finds_elements(company_Name,'Raptor')
        #Address
        address="(//*[@name='street[0]'])"
        self.finds_elements(address,'UK')
        #City_Name
        city_Name="(//*[@name='city'])"
        self.finds_elements(city_Name,'abc')
        #Country dropdown
        country_Dropdown="(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown,'Egypt')
        #State dropdown
        #state_Or_Province="(//*[@name='region_id'])"
        #self.finds_elements(state_Or_Province,'Goa')
        #Postal code
        postal_Code="(//*[@name='postcode'])"
        self.finds_elements(postal_Code,123456)
        #Contact number
        phone_number="(//*[@name='telephone'])"
        self.finds_elements(phone_number,1234567890)
        #Click on continue or submit
        click_On_continue="(//*[@id='eve_200'])"
        self.finds_elements(click_On_continue)
        #Express 5 to 7 days
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@class="table-checkout-shipping-method shipping_info_label_wrp"]').find_element(By.TAG_NAME, 'td').click()
        
        #Process_Payment
        click_On_Payment="(//*[@id='proceed_payment'])"
        self.finds_elements(click_On_Payment) 
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '205'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)


    def eve_206(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        #Shipping Information
       #Email Id
        email_Address="(//*[@id='customer-email'])"
        self.finds_elements(email_Address,'shubham@raptorsupplies.co.uk')
        #First Name
        first_Name="(//*[@name='firstname'])"
        self.finds_elements(first_Name,'Automation')
        #Last Name
        last_Name="(//*[@name='lastname'])"
        self.finds_elements(last_Name,'Testing')
        #Company Name
        company_Name="(//*[@name='company'])"
        self.finds_elements(company_Name,'Raptor')
        #Address
        address="(//*[@name='street[0]'])"
        self.finds_elements(address,'UK')
        #City_Name
        city_Name="(//*[@name='city'])"
        self.finds_elements(city_Name,'abc')
        #Country dropdown
        country_Dropdown="(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown,'Egypt')
        #State dropdown
        #state_Or_Province="(//*[@name='region_id'])"
        #self.finds_elements(state_Or_Province,'Goa')
        #Postal code
        postal_Code="(//*[@name='postcode'])"
        self.finds_elements(postal_Code,123456)
        #Contact number
        phone_number="(//*[@name='telephone'])"
        self.finds_elements(phone_number,1234567890)
        #Click on continue or submit
        click_On_continue="(//*[@id='eve_200'])"
        self.finds_elements(click_On_continue)
        #Express 5 to 7 days
        self.driver.find_element(By.XPATH, '//*[@class="table-checkout-shipping-method shipping_info_label_wrp"]').find_element(By.TAG_NAME, 'td').click()
        
        #Process_Payment
        click_On_Payment="(//*[@id='proceed_payment'])"
        self.finds_elements(click_On_Payment) 
        #select payment mode
        creditCard_Mode="(//*[text()='Credit Card'])"
        self.finds_elements(creditCard_Mode)
        #Click on checkbox of credit card
        credit_Card_Checkbox="(//*[@id='stripe_check'])"
        self.finds_elements(credit_Card_Checkbox)
        #Click on Place order
        place_Order="(//*[@id='stripe_real'])"
        self.finds_elements(place_Order)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Name of Payment mode'
        val2 = ''
        eve_id = '206'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_207(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        #Shipping Information
       #Email Id
        email_Address="(//*[@id='customer-email'])"
        self.finds_elements(email_Address,'shubham@raptorsupplies.co.uk')
        #First Name
        first_Name="(//*[@name='firstname'])"
        self.finds_elements(first_Name,'Abc')
        #Last Name
        last_Name="(//*[@name='lastname'])"
        self.finds_elements(last_Name,'Kumar')
        #Company Name
        company_Name="(//*[@name='company'])"
        self.finds_elements(company_Name,'Raptor')
        #Address
        address="(//*[@name='street[0]'])"
        self.finds_elements(address,'UK')
        #City_Name
        city_Name="(//*[@name='city'])"
        self.finds_elements(city_Name,'abc')
        #Country dropdown
        country_Dropdown="(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown,'Egypt')
        #State dropdown
        #state_Or_Province="(//*[@name='region_id'])"
        #self.finds_elements(state_Or_Province,'Goa')
        #Postal code
        postal_Code="(//*[@name='postcode'])"
        self.finds_elements(postal_Code,123456)
        #Contact number
        phone_number="(//*[@name='telephone'])"
        self.finds_elements(phone_number,1234567890)
        #Click on continue or submit
        click_On_continue="(//*[@id='eve_200'])"
        self.finds_elements(click_On_continue)
        #Express 5 to 7 days
        self.driver.find_element(By.XPATH, '//*[@class="table-checkout-shipping-method shipping_info_label_wrp"]').find_element(By.TAG_NAME, 'td').click()
        
        #Process_Payment
        click_On_Payment="(//*[@id='proceed_payment'])"
        self.finds_elements(click_On_Payment) 
        #select payment mode
        net_payment="(//*[@id='tooltip_banktransfer'])"
        self.finds_elements(net_payment)
        purschase_no="(//*[@id='eve_209'])"
        self.finds_elements(purschase_no,6547685)
        #Click on checkbox of credit card
        net_payment_Checkbox="(//*[@id='net_check'])"
        self.finds_elements(net_payment_Checkbox)
        #Click on Place order
        #place_Order="(//*[@id='net_real'])"
        #self.finds_elements(place_Order)

        self.print_visitor_id()
        con = "BPN"
        val1 = 'Subtotal with Currency'
        val2 = ''
        eve_id = '207'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)        

    

    def eve_209(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        #Shipping Information
       #Email Id
        email_Address="(//*[@id='customer-email'])"
        self.finds_elements(email_Address,'shubham@raptorsupplies.co.uk')
        #First Name
        first_Name="(//*[@name='firstname'])"
        self.finds_elements(first_Name,'Abc')
        #Last Name
        last_Name="(//*[@name='lastname'])"
        self.finds_elements(last_Name,'Kumar')
        #Company Name
        company_Name="(//*[@name='company'])"
        self.finds_elements(company_Name,'Raptor')
        #Address
        address="(//*[@name='street[0]'])"
        self.finds_elements(address,'UK')
        #City_Name
        city_Name="(//*[@name='city'])"
        self.finds_elements(city_Name,'abc')
        #Country dropdown
        country_Dropdown="(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown,'Egypt')
        #State dropdown
        #state_Or_Province="(//*[@name='region_id'])"
        #self.finds_elements(state_Or_Province,'Goa')
        #Postal code
        postal_Code="(//*[@name='postcode'])"
        self.finds_elements(postal_Code,123456)
        #Contact number
        phone_number="(//*[@name='telephone'])"
        self.finds_elements(phone_number,1234567890)
        #Click on continue or submit
        click_On_continue="(//*[@id='eve_200'])"
        self.finds_elements(click_On_continue)
        #Express 5 to 7 days
        self.driver.find_element(By.XPATH, '//*[@class="table-checkout-shipping-method shipping_info_label_wrp"]').find_element(By.TAG_NAME, 'td').click()
        
        #Process_Payment
        click_On_Payment="(//*[@id='proceed_payment'])"
        self.finds_elements(click_On_Payment) 
        #select payment mode Net 30
        select_Net="(//*[text()='NET30 Payment'])"
        self.finds_elements(select_Net)
        #enter purchase order id
        purchase_Order="(//*[@id='eve_209'])"
        self.finds_elements(purchase_Order,575885)
        #Click on net30 payment checkbox
        net_Payment_Checkbox="(//*[@id='net_check'])"
        self.finds_elements(net_Payment_Checkbox)
        #Place order 
        place_Order="(//*[@id='net_real'])"
        self.finds_elements(place_Order)
        #Message display
        confirmation_msg="(//*[text()='Thank you for '])"
        self.finds_elements(confirmation_msg)

        self.print_visitor_id()
        con = "BP"
        val1 = '#TEXT'
        val2 = ''
        eve_id = '209'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id) 

    def eve_210(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        #Shipping Information
       #Email Id
        email_Address="(//*[@id='customer-email'])"
        self.finds_elements(email_Address,'shubham@raptorsupplies.co.uk')
        #First Name
        first_Name="(//*[@name='firstname'])"
        self.finds_elements(first_Name,'Abc')
        #Last Name
        last_Name="(//*[@name='lastname'])"
        self.finds_elements(last_Name,'Kumar')
        #Company Name
        company_Name="(//*[@name='company'])"
        self.finds_elements(company_Name,'Raptor')
        #Address
        address="(//*[@name='street[0]'])"
        self.finds_elements(address,'UK')
        #City_Name
        city_Name="(//*[@name='city'])"
        self.finds_elements(city_Name,'abc')
        #Country dropdown
        country_Dropdown="(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown,'Egypt')
        #State dropdown
        #state_Or_Province="(//*[@name='region_id'])"
        #self.finds_elements(state_Or_Province,'Goa')
        #Postal code
        postal_Code="(//*[@name='postcode'])"
        self.finds_elements(postal_Code,123456)
        #Contact number
        phone_number="(//*[@name='telephone'])"
        self.finds_elements(phone_number,1234567890)
        #Click on continue or submit
        click_On_continue="(//*[@id='eve_200'])"
        self.finds_elements(click_On_continue)
        #Express 5 to 7 days
        self.driver.find_element(By.XPATH, '//*[@class="table-checkout-shipping-method shipping_info_label_wrp"]').find_element(By.TAG_NAME, 'td').click()
        
        #Process_Payment
        click_On_Payment="(//*[@id='proceed_payment'])"
        self.finds_elements(click_On_Payment) 
        #select payment mode Profora Invoice
        select_Proforma="(//*[text()='Proforma Invoice'])"
        self.finds_elements(select_Proforma)
        #enter purchase order id
        purchase_Order="(//*[@id='eve_210'])"
        self.finds_elements(purchase_Order,4587698)
        #Click on proforma payment checkbox
        profroma_Invoice_Checkbox="(//*[@id='performa_check'])"
        self.finds_elements(profroma_Invoice_Checkbox)
        #Place order 
        place_Order="(//*[@id='performa_real'])"
        self.finds_elements(place_Order)

        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '210'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id) 

    def eve_211(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart ="//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        #Shipping Information
       #Email Id
        email_Address="(//*[@id='customer-email'])"
        self.finds_elements(email_Address,'shubham@raptorsupplies.co.uk')
        #First Name
        first_Name="(//*[@name='firstname'])"
        self.finds_elements(first_Name,'Abc')
        #Last Name
        last_Name="(//*[@name='lastname'])"
        self.finds_elements(last_Name,'Kumar')
        #Company Name
        company_Name="(//*[@name='company'])"
        self.finds_elements(company_Name,'Raptor')
        #Address
        address="(//*[@name='street[0]'])"
        self.finds_elements(address,'UK')
        #City_Name
        city_Name="(//*[@name='city'])"
        self.finds_elements(city_Name,'abc')
        #Country dropdown
        country_Dropdown="(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown,'Egypt')
        #State dropdown
        #state_Or_Province="(//*[@name='region_id'])"
        #self.finds_elements(state_Or_Province,'Goa')
        #Postal code
        postal_Code="(//*[@name='postcode'])"
        self.finds_elements(postal_Code,123456)
        #Contact number
        phone_number="(//*[@name='telephone'])"
        self.finds_elements(phone_number,1234567890)
        #Click on continue or submit
        click_On_continue="(//*[@id='eve_200'])"
        self.finds_elements(click_On_continue)
        #Express 5 to 7 days
        self.driver.find_element(By.XPATH, '//*[@class="table-checkout-shipping-method shipping_info_label_wrp"]').find_element(By.TAG_NAME, 'td').click()
        #Process_Payment
        click_On_Payment="(//*[@id='proceed_payment'])"
        self.finds_elements(click_On_Payment) 
        #select payment mode Profora Invoice
        select_Proforma="(//*[text()='Proforma Invoice'])"
        self.finds_elements(select_Proforma)
        #enter purchase order id
        purchase_Order="(//*[@id='eve_210'])"
        self.finds_elements(purchase_Order,265454)
        #Click on net30 payment checkbox
        profroma_Invoice_Checkbox="(//*[@id='performa_check'])"
        self.finds_elements(profroma_Invoice_Checkbox)
        #Place order 
        place_Order="(//*[@id='performa_real'])"
        self.finds_elements(place_Order)
        
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Email'
        val2 = ''
        eve_id = '211'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_334(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        #Shipping Information
       #Email Id
        email_Address="(//*[@id='customer-email'])"
        self.finds_elements(email_Address,'shubham@raptorsupplies.co.uk')
        #First Name
        first_Name="(//*[@name='firstname'])"
        self.finds_elements(first_Name,'Abc')
        #Last Name
        last_Name="(//*[@name='lastname'])"
        self.finds_elements(last_Name,'Kumar')
        #Company Name
        company_Name="(//*[@name='company'])"
        self.finds_elements(company_Name,'Raptor')
        #Address
        address="(//*[@name='street[0]'])"
        self.finds_elements(address,'UK')
        #City_Name
        city_Name="(//*[@name='city'])"
        self.finds_elements(city_Name,'abc')
        #Country dropdown
        country_Dropdown="(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown,'Egypt')
        #State dropdown
        #state_Or_Province="(//*[@name='region_id'])"
        #self.finds_elements(state_Or_Province,'Goa')
        #Postal code
        postal_Code="(//*[@name='postcode'])"
        self.finds_elements(postal_Code,123456)
        #Contact number
        phone_number="(//*[@name='telephone'])"
        self.finds_elements(phone_number,1234567890)
        #Click on continue or submit
        click_On_continue="(//*[@id='eve_200'])"
        self.finds_elements(click_On_continue)
        #Click on edit option for shipping details
        edit_Option="(//*[@class='edit_shipping_info'])"
        self.finds_elements(edit_Option)
        #Edit city name
        edit_City="(//*[@name='city'])"
        self.finds_elements(edit_City)
        click_On_continue="(//*[@id='eve_200'])"
        self.finds_elements(click_On_continue)
        expres_mode="(//*[text()='Express (5 - 7 days)'])"
        self.finds_elements(expres_mode)
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Section Name'
        val2 = ''
        eve_id = '334'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_396(self,url):
        self.request_func(url)
        #Add To Cart
        add_to_cart ="//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        #Live Chat
        self.chat_box_close()
        #CheckOut Option
        click_On_Checkout="(//*[@id='eve_294'])"
        self.finds_elements( click_On_Checkout)
        #Shipping Information
       #Email Id
        email_Address="(//*[@id='customer-email'])"
        self.finds_elements(email_Address,'shubham@raptorsupplies.co.uk')
        #First Name
        first_Name="(//*[@name='firstname'])"
        self.finds_elements(first_Name,'Abc')
        #Last Name
        last_Name="(//*[@name='lastname'])"
        self.finds_elements(last_Name,'Kumar')
        #Company Name
        company_Name="(//*[@name='company'])"
        self.finds_elements(company_Name,'Raptor')
        #Address
        address="(//*[@name='street[0]'])"
        self.finds_elements(address,'UK')
        #City_Name
        city_Name="(//*[@name='city'])"
        self.finds_elements(city_Name,'abc')
        #Country dropdown
        country_Dropdown="(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown,'Egypt')
        #State dropdown
        #state_Or_Province="(//*[@name='region_id'])"
        #self.finds_elements(state_Or_Province,'Goa')
        #Postal code
        postal_Code="(//*[@name='postcode'])"
        self.finds_elements(postal_Code,123456)
        #Contact number
        phone_number="(//*[@name='telephone'])"
        self.finds_elements(phone_number,1234567890)
        #uncheck on Billing information
        uncheck_Billing_Info="(//*[@id='eve_396'])"
        self.finds_elements(uncheck_Billing_Info)
        
        self.print_visitor_id()
        con = "BP"
        val1 = 'Select/ Unselect'
        val2 = ''
        eve_id = '396'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id) 

    #ATC POPUP

    def eve_295(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        cross_popup=self.driver.find_element(By.XPATH,"//*[@id='eve_295']")
        self.driver.execute_script("arguments[0].click();", cross_popup)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '295'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_290(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        time.sleep(2)
        add_Quantity=self.driver.find_element(By.XPATH,"//*[@id='eve_290']")
        self.driver.execute_script("arguments[0].click();", add_Quantity)
        
        # self.finds_elements(add_Quantity)
        self.print_visitor_id()
        con = "BP"
        val1 = '# Quantity Before'
        val2 = '# Quantity After'
        eve_id = '290'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_291(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        add_Quantity=self.driver.find_element(By.XPATH,"//*[@id='eve_290']")
        self.driver.execute_script("arguments[0].click();", add_Quantity)
        reduce_Quantity=self.driver.find_element(By.XPATH,"(//*[@id='eve_291'])")
        self.driver.execute_script("arguments[0].click();", reduce_Quantity)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Title'
        val2 = ''
        eve_id = '291'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_292(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Trash_bin=self.driver.find_element(By.XPATH,"//*[@id='eve_292']")
        self.driver.execute_script("arguments[0].click();", click_On_Trash_bin)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Title'
        val2 = ''
        eve_id = '292'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_293(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart=self.driver.find_element(By.XPATH,"//*[@id='eve_293']/a")
        self.driver.execute_script("arguments[0].click();", click_On_View_Cart)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Title'
        val2 = 'Subtotal with Currency'
        eve_id = '293'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_294(self,url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout=self.driver.find_element(By.XPATH,"//*[@id='eve_294']/a")
        self.driver.execute_script("arguments[0].click();", click_On_Checkout)
        self.driver.back()
        time.sleep(5)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Title'
        val2 = 'Subtotal with Currency'
        eve_id = '294'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_390(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="maindis"]/div/table/tbody/tr[2]/td[5]/button'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="eve_390"]', 'archanagautam@gmail.com')
        pyautogui.press('enter')
        # self.finds_elements('//*[@id="closeBtn"]/div/div[2]/div[5]/button')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '390'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    

    def eve_397(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="maindis"]/div/table/tbody/tr[2]/td[5]/button'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="eve_390"]','rahul@raptorsupplies.co.uk')
        self.finds_elements('//*[@id="closeBtn"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#email'
        val2 = ''
        eve_id = '397'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    
    def eve_403(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="maindis"]/div/table/tbody/tr[2]/td[5]/button'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="quantity"]/button[2]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#Initial Value'
        val2 = '#Final Value'
        eve_id = '403'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)


    def eve_65(self, url):
        self.request_func(url)
        comment = '//*[@id="Item"]/label[1]/span'
        self.finds_elements(comment)
        # self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Filter name'
        val2 = '#value1 | #value2 | #value3'
        eve_id = '65'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_161(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_161"]/option[2]'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="next-btn2"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '161'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_162(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_162"]'
        self.finds_elements(comment,'1223')
        pyautogui.press('enter')
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '162'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_158(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_163"]', 'company name')
        print("company name")
        self.finds_elements('//*[@id="eve_164"]', '1234567')
        print("registration number")
        self.finds_elements('//*[@id="eve_166"]', '12')
        print("VAT")
        self.finds_elements('//*[@id="eve_161"]/option[2]')
        print("Currency")
        self.finds_elements('//*[@id="eve_162"]', '1234567')
        print("required credit card")
        self.finds_elements('//*[@id="eve_168"]', 'Akshat Vila')
        print("address")
        self.finds_elements('//*[@id="eve_169"]', 'delhi')
        print("city")
        self.finds_elements('//*[@id="eve_170"]', '110044')
        print("postal code")
        self.finds_elements(' //*[@id="eve_171"]/option[7]')
        print("country")
        self.finds_elements('//*[@id="next-btn2"]')
        self.finds_elements('//*[@id="eve_158"]', 'Arch')
        print("Full name")
        self.finds_elements('//*[@id="submit"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '158'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)



    

    def eve_159(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_162"]'
        self.finds_elements(comment)
        pyautogui.press('enter')
        self.finds_elements('//*[@id="eve_159"]', 'archanagautam1951@gmail.com')
        self.finds_elements('//*[@id="submit"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '159'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_160(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_162"]'
        self.finds_elements(comment)
        pyautogui.press('enter')
        self.finds_elements('//*[@id="eve_160"]', '9999999999')
        self.finds_elements('//*[@id="submit"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '160'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_171(self, url):
        self.request_func(url)
        comment = ' //*[@id="eve_171"]/option[7]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@id="next-btn2"]')
        self.print_visitor_id()
        con = "BP"  
        val1 = '# text'
        val2 = ''
        eve_id = '171'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)  

    def eve_90(self, url):
        self.request_func(url)
        time.sleep(4)
        # self.finds_elements('//*[@id="next-btn2"]')
        self.print_visitor_id()
        con = "BP"  
        val1 = ''
        val2 = ''
        eve_id = '90'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_283(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="mycheckbox_844705_850574"]'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="mycheckbox_844705_850574"]')
        self.print_visitor_id()
        con = "BP"
        val1 = 'URL'
        val2 = ''
        eve_id = '283'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_228(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.chat_box_close()
        self.finds_elements('//*[@id="at_brand"]')
        time.sleep(3)
        self.finds_elements('//*[@id="brandFilter"]/div/label[1]')
        self.finds_elements('//*[@id="close"]/span')
        self.finds_elements('//*[@id="xyz"]')

        self.print_visitor_id()
        con = "BPN"
        val1 = '# Filter_name'
        val2 = '# filter1 value1 | value 2..'
        eve_id = '228'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_227(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.chat_box_close()
        self.finds_elements('//*[@id="at_brand"]')
        time.sleep(3)
        self.finds_elements('//*[@id="brandFilter"]/div/label[1]')
        self.finds_elements('//*[@id="close"]/span')
        # self.finds_elements('//*[@id="eve_224"]')
        self.finds_elements('//*[@id="abc"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = '# Filter_name'
        val2 = '# filter1 value1 | value 2..'
        eve_id = '227'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_266(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_13"]')
        print('sign in')
        self.finds_elements('//*[@id="email"]', 'devanshu@nextgenesolutions.com')
        print('username')
        self.finds_elements('//*[@id="pass"]', 'Devanshu@123')
        print('password')
        self.chat_box_close()
        self.finds_elements('//*[@id="send2"]')
        print('login')
        time.sleep(4)

        self.element_hover('//*[@id="eve_13"]')
        self.finds_elements('//*[@class="header_orders"]')
        time.sleep(2)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Name'
        val2 = ''
        eve_id = '266'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
def run_program():

    program_dict = {
        
        # Product 0
        'eve_24' : 'eve_24("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_25' : 'eve_25("https://www.raptorsupplies.com/pd/dayton/6k844")',
        'eve_26' : 'eve_26("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_52' : 'eve_52("https://www.raptorsupplies.com/pd/morse-drum/86")',
        'eve_53' : 'eve_53("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_54' : 'eve_54("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_55' : 'eve_55("https://www.raptorsupplies.com/pd/aurand/s2k7")',
        'eve_56' : 'eve_56("https://www.raptorsupplies.com/pd/aurand/s2k7")',
        'eve_57' : 'eve_57("https://www.raptorsupplies.com/pd/aurand/s2k7")',
        'eve_80' :  'eve_80("https://www.raptorsupplies.com/p1/akro-mils/30080-series-shelf-bin")',
        'eve_317' : 'eve_317("https://www.raptorsupplies.com/pd/morse-drum/86")',
        'eve_404' :  'eve_404("https://www.raptorsupplies.com/pd/morse-drum/92")',
        #End product static 12

        # Branding Page 12
        'eve_363' : 'eve_363("https://www.raptorsupplies.com/branding/display-ads")',
        'eve_364' : 'eve_364("https://www.raptorsupplies.com/branding/display-ads")',
        'eve_365' : 'eve_365("https://www.raptorsupplies.com/branding/display-ads")',
        'eve_366' : 'eve_366("https://www.raptorsupplies.com/branding/display-ads")',
        'eve_368' : 'eve_368("https://www.raptorsupplies.com/branding/recent-user")',
        'eve_369' : 'eve_369("https://www.raptorsupplies.com/branding/recent-user")',
        'eve_370' : 'eve_370("https://www.raptorsupplies.com/branding/recent-user")',
        'eve_371' : 'eve_371("https://www.raptorsupplies.com/branding/recent-user")',
        #End Branding 20    

        #b2b-benefits 20
        "eve_250" : 'eve_250("https://www.raptorsupplies.com/b2b-benefits")',
        "eve_251" : 'eve_251("https://www.raptorsupplies.com/b2b-benefits")',
        "eve_252" : 'eve_252("https://www.raptorsupplies.com/b2b-benefits")',
        #End b2b-benefits 23
        
        #Mobile View 23
        'eve_212' : 'eve_212("https://www.raptorsupplies.com/")',
        'eve_213' : 'eve_213("https://www.raptorsupplies.com/")',
        'eve_214' : 'eve_214("https://www.raptorsupplies.com/")',
        'eve_215' : 'eve_215("https://www.raptorsupplies.com/")',
        'eve_216' : 'eve_216("https://www.raptorsupplies.com/")',
        'eve_217' : 'eve_217("https://www.raptorsupplies.com/")',
        'eve_218' : 'eve_218("https://www.raptorsupplies.com/")',
        'eve_219' : 'eve_219("https://www.raptorsupplies.com/")',
        'eve_220' : 'eve_220("https://www.raptorsupplies.com/")',
        'eve_221' : 'eve_221("https://www.raptorsupplies.com/")',
        'eve_222' : 'eve_222("https://www.raptorsupplies.com")',
        'eve_223' : 'eve_223("https://www.raptorsupplies.com")',
        'eve_224' : 'eve_224("https://www.raptorsupplies.com/c/disc-backup-pads")',
        'eve_229' : 'eve_229("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_230' : 'eve_230("https://www.raptorsupplies.com/pd/vestil/fmdl-2-lds-r3")',
        'eve_231' : 'eve_231("https://www.raptorsupplies.com/pd/morse-drum/91")',
        # End Mobile view  43

        # contact us 39
        'eve_236' : 'eve_236("https://www.raptorsupplies.com/contact")',
        'eve_237' : 'eve_237("https://www.raptorsupplies.com/contact")',
        'eve_238' : 'eve_238("https://www.raptorsupplies.com/contact")',
        'eve_239' : 'eve_239("https://www.raptorsupplies.com/contact")',
        'eve_240' : 'eve_240("https://www.raptorsupplies.com/contact")',
        'eve_241' : 'eve_241("https://www.raptorsupplies.com/contact")',   
        'eve_242' : 'eve_242("https://www.raptorsupplies.com/contact")',
        'eve_243' : 'eve_243("https://www.raptorsupplies.com/contact")',
        'eve_244' : 'eve_244("https://www.raptorsupplies.com/contact")',
        #end Contact Us 52

        # about us 52
        'eve_245' : 'eve_245("https://www.raptorsupplies.com/about-us")',
        'eve_246' : 'eve_246("https://www.raptorsupplies.com/about-us")',
        'eve_247' : 'eve_247("https://www.raptorsupplies.com/about-us")',
        'eve_248' : 'eve_248("https://www.raptorsupplies.com/about-us")',
        # end about us 56

        # Home page 56
        # 'eve_116' : 'eve_116("https://www.raptorsupplies.com/")',
        'eve_117' : 'eve_117("https://www.raptorsupplies.com/")',
        'eve_118' : 'eve_118("https://www.raptorsupplies.com/")',
        'eve_120' : 'eve_120("https://www.raptorsupplies.com/")',
        'eve_121' : 'eve_121("https://www.raptorsupplies.com/")',
        'eve_122' : 'eve_122("https://www.raptorsupplies.com/")',
        # Home page 62

        # L1 and L2 62
        'eve_104' : 'eve_104("https://www.raptorsupplies.com/l1/abrasives")',
        'eve_105' : 'eve_105("https://www.raptorsupplies.com/l1/abrasives")',
        'eve_106' : 'eve_106("https://www.raptorsupplies.com/l1/abrasives")',
        'eve_107' : 'eve_107("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        # End L1 and L2 66

        # RFQ Pop-up 66
        'eve_40' : 'eve_40("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_41' : 'eve_41("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_42' : 'eve_42("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_43' : 'eve_43("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_44' : 'eve_44("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_402' : 'eve_402("https://www.raptorsupplies.com/pd/morse-drum/91")',
        # END RFQ 72

        # website 72
        'eve_90' : 'eve_90("https://www.raptorsupplies.com/")',
        'eve_94' : 'eve_94("https://www.raptorsupplies.com/l1/abrasives")',
        'eve_96' : 'eve_96("https://www.raptorsupplies.com/")',
        'eve_98' : 'eve_98("https://www.raptorsupplies.com/login")',
        'eve_99' : 'eve_99("https://www.raptorsupplies.com/login")',
        'eve_100' : 'eve_100("https://www.raptorsupplies.com/login")',
        'eve_290' : 'eve_290("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        'eve_291' : 'eve_291("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        'eve_292' : 'eve_292("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        'eve_293' : 'eve_293("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        'eve_294' : 'eve_294("https://www.raptorsupplies.com/pd/proto/jsf20m")', 
        'eve_295' : 'eve_295("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        # End Website 84

        # credit card form 84
        'eve_158' : 'eve_158("https://www.raptorsupplies.com/credit-account-application")',
        'eve_159' : 'eve_159("https://www.raptorsupplies.com/credit-account-application")',
        'eve_160' : 'eve_160("https://www.raptorsupplies.com/credit-account-application")',
        'eve_161' : 'eve_161("https://www.raptorsupplies.com/credit-account-application")',
        'eve_162' : 'eve_162("https://www.raptorsupplies.com/credit-account-application")',
        'eve_163' : 'eve_163("https://www.raptorsupplies.com/credit-account-application")',
        'eve_164' : 'eve_164("https://www.raptorsupplies.com/credit-account-application")',
        'eve_166' : 'eve_166("https://www.raptorsupplies.com/credit-account-application")',
        'eve_168' : 'eve_168("https://www.raptorsupplies.com/credit-account-application")',
        'eve_169' : 'eve_169("https://www.raptorsupplies.com/credit-account-application")',
        'eve_170' : 'eve_170("https://www.raptorsupplies.com/credit-account-application")',
        'eve_171' : 'eve_171("https://www.raptorsupplies.com/credit-account-application")',
        #End Credit card Form 96

        # vendor-registration 96
        'eve_134' : 'eve_134("https://www.raptorsupplies.com/vendor-registration")',
        'eve_132' : 'eve_132("https://www.raptorsupplies.com/vendor-registration")',
        'eve_133' : 'eve_133("https://www.raptorsupplies.com/vendor-registration")', 
        # End vendor-registration 99

        #Discontinued item 99
        'eve_386' : 'eve_386("https://www.raptorsupplies.com/obsolete-brand-pages")',
        'eve_388' :  'eve_388("https://www.raptorsupplies.com/obsolete/ampg")',
        'eve_389' :  'eve_389("https://www.raptorsupplies.com/obsolete/ampg")',
        'eve_390' :  'eve_390("https://www.raptorsupplies.com/obsolete/ampg")',
        'eve_393' :  'eve_393("https://www.raptorsupplies.com/obsolete/ampg")',
        'eve_397' :  'eve_397("https://www.raptorsupplies.com/obsolete/ampg")',
        'eve_403' :  'eve_403("https://www.raptorsupplies.com/obsolete/ampg")',
        #Discontinued item 106

        #No Search Result 106
        'eve_377' :  'eve_377("https://www.raptorsupplies.com/s/no-results?q=bdndbjfjf")',
        'eve_378' :  'eve_378("https://www.raptorsupplies.com/s/no-results?q=bdndbjfjf")',
        'eve_379' :  'eve_379("https://www.raptorsupplies.com/s/no-results?q=bdndbjfjf")',
        'eve_380' :  'eve_380("https://www.raptorsupplies.com/s/no-results?q=bdndbjfjf")',
        'eve_381' :  'eve_381("https://www.raptorsupplies.com/s/no-results?q=bdndbjfjf")',
        # No Search Result 111
    

        'eve_9' : 'eve_9("https://www.raptorsupplies.com/")',
        'eve_13' : 'eve_13("https://www.raptorsupplies.com/")',
        'eve_16' : 'eve_16("https://www.raptorsupplies.com/")',
        'eve_18' : 'eve_18("https://www.raptorsupplies.com/")',
        'eve_76' : 'eve_76("https://www.raptorsupplies.com/")',
        'eve_89' : 'eve_89("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_302' : 'eve_302("https://www.raptorsupplies.com/")',
        'eve_304' : 'eve_304("https://www.raptorsupplies.com/")',
        'eve_354' : 'eve_354("https://www.raptorsupplies.com/b/allegro-safety")',
        'eve_355' : 'eve_355("https://www.raptorsupplies.com/b/allegro-safety")',
        'eve_356' : 'eve_356("https://www.raptorsupplies.com/b/allegro-safety")',
        'eve_77' : 'eve_77("https://www.raptorsupplies.com/where-we-deliver")',
        'eve_78' : 'eve_78("https://www.raptorsupplies.com/where-we-deliver")',
        'eve_64' : 'eve_64("https://www.raptorsupplies.com/")',
        'eve_253' : 'eve_253("https://www.raptorsupplies.com/terms-conditions")',
        'eve_254' : 'eve_254("https://www.raptorsupplies.com/return-policy")',
        'eve_319' : 'eve_319("https://www.raptorsupplies.com/c/fasteners/c3/adhesive-anchors")',
        'eve_59' : 'eve_59("https://www.raptorsupplies.com/b/ad-weighing")',
        'eve_61' : 'eve_61("https://www.raptorsupplies.com/b/char-lynn")',
        'eve_62' : 'eve_62("https://www.raptorsupplies.com/b/char-lynn")',
        'eve_63' : 'eve_63("https://www.raptorsupplies.com/b/char-lynn")',
        'eve_79' : 'eve_79("https://www.raptorsupplies.com/where-we-deliver")',
        'eve_86' : 'eve_86("https://www.raptorsupplies.com/where-we-deliver")',
        'eve_87' : 'eve_87("https://www.raptorsupplies.com/where-we-deliver")',
        'eve_88' : 'eve_88("https://www.raptorsupplies.com/where-we-deliver")',
        'eve_335' : 'eve_335("https://www.raptorsupplies.com/create")',
        'eve_336' : 'eve_336("https://www.raptorsupplies.com/create")',
        'eve_337' : 'eve_337("https://www.raptorsupplies.com/create")',
        # 'eve_338' : 'eve_338("https://www.raptorsupplies.com/create")',
        'eve_339' : 'eve_339("https://www.raptorsupplies.com/create")',
        'eve_15' : 'eve_15("https://www.raptorsupplies.com/pd/3m/483-ab9hrk")',
        'eve_116' : 'eve_116("https://www.raptorsupplies.com/")',
        'eve_269' : 'eve_269("https://www.raptorsupplies.com/")',
        'eve_122' :  'eve_122("https://www.raptorsupplies.com/")',
        'eve_270' :  'eve_270("https://www.raptorsupplies.com/")',
        'eve_271' :  'eve_271("https://www.raptorsupplies.com/")',
        'eve_267' :  'eve_267("https://www.raptorsupplies.com/")',
        'eve_266' :  'eve_266("https://www.raptorsupplies.com/")',
        'eve_21' :  'eve_21("https://www.raptorsupplies.com/")',
        'eve_249' :  'eve_249("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_344' :  'eve_344("https://www.raptorsupplies.com/check/cart")',
        'eve_272' :  'eve_272("https://www.raptorsupplies.com/s?q=1234")',
        'eve_273' :  'eve_273("https://www.raptorsupplies.com/s?q=1234")',
        'eve_12' :  'eve_12("https://www.raptorsupplies.com/")',
        'eve_198' :  'eve_198("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_294' :  'eve_294("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_274'  :  'eve_274("https://www.raptorsupplies.com/s?q=m1")',
        'eve_275'  :  'eve_275("https://www.raptorsupplies.com/s?q=m1")',
        'eve_276'  :  'eve_276("https://www.raptorsupplies.com/s?q=m1")',
        'eve_69'  : 'eve_69("https://www.raptorsupplies.com/c/fasteners/c3/hex-head-cap-screws")',
        'eve_71'  : 'eve_71("https://www.raptorsupplies.com/c/fasteners/c4/nylon-hex-head-cap-screws")',
        'eve_109' : 'eve_109("https://www.raptorsupplies.com/c/drum-lifters")',
        'eve_70'  :  'eve_70("https://www.raptorsupplies.com/c/fasteners/c3/hex-head-cap-screws")',
        'eve_285' : 'eve_285("https://www.raptorsupplies.com/c/fork-mounted-drum-handling-equipment")',
        'eve_73'  :  'eve_73("https://www.raptorsupplies.com/c/fasteners/p/1-4-20-coarse-plain-nylon-hex-head-cap-screws")',
        'eve_113':  'eve_113("https://www.raptorsupplies.com/p/tough-guy/counter-duster")',
        'eve_114':  'eve_114("https://www.raptorsupplies.com/p/tough-guy/counter-duster")',
        'eve_115':  'eve_115("https://www.raptorsupplies.com/p/remco/ust-medium-bench-brushes")',
        'eve_347':  'eve_347("https://www.raptorsupplies.com/c/fasteners/p/1-4-20-coarse-plain-nylon-hex-head-cap-screws")',
        'eve_286' : 'eve_286("https://www.raptorsupplies.com/submit-purchase-order")',
        'eve_287' : 'eve_287("https://www.raptorsupplies.com/submit-purchase-order")',
        'eve_282' :  'eve_282("https://www.raptorsupplies.com/c/fork-mounted-drum-handling-equipment")',
        'eve_284' :  'eve_284("https://www.raptorsupplies.com/c/fork-mounted-drum-handling-equipment")',
        'eve_124' : 'eve_124("https://www.raptorsupplies.com/request-for-quote")',
        'eve_125' : 'eve_125("https://www.raptorsupplies.com/request-for-quote")',
        'eve_126' : 'eve_126("https://www.raptorsupplies.com/request-for-quote")',
        'eve_127' : 'eve_127("https://www.raptorsupplies.com/request-for-quote")',
        'eve_128' : 'eve_128("https://www.raptorsupplies.com/request-for-quote")',
        'eve_384' : 'eve_384("https://www.raptorsupplies.com/request-for-quote")',
        'eve_383' : 'eve_383("https://www.raptorsupplies.com/request-for-quote")',
        'eve_283' :  'eve_283("https://www.raptorsupplies.com/c/fork-mounted-drum-handling-equipment")',
        

        #checkout 
        'eve_192' : 'eve_192("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        'eve_193' : 'eve_193("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_194' : 'eve_194("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_195' : 'eve_195("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_196' : 'eve_196("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_197' : 'eve_197("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_198' : 'eve_198("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_199' : 'eve_199("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_200' : 'eve_200("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_201' :  'eve_201("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_202' :  'eve_202("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_203' :  'eve_203("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_204' :  'eve_204("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_205':'eve_205("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_206':'eve_206("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_207':'eve_207("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_208':'eve_208("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_209':'eve_209("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_210':'eve_210("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_211':'eve_211("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_334':'eve_334("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_396':'eve_396("https://www.raptorsupplies.com/pd/morse-drum/91")',
        #shopping cart
        'eve_350':'eve_350("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_352':'eve_352("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_179':'eve_179("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_180':'eve_180("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_181':'eve_181("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_182':'eve_182("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_184':'eve_184("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_185':'eve_185("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_186':'eve_186("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_187':'eve_187("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_97':'eve_97("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_399':'eve_399("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_400':'eve_400("https://www.raptorsupplies.com/pd/morse-drum/91")',
     
      }  

    testing = RawEventsTesting()
    # keys = list(program_dict.keys())
    # start_index = 171
    # for i, key in enumerate(keys[start_index:176], start_index):
    #     print(i, ">>>>>>>>>>> Working Template >>>>>>>>>", key), eval(f"testing.{program_dict[key]}")
    #     time.sleep(5)
    for key in keys_to_run:
        if key in program_dict:
            print(">>>>>>>>>>> Working Template >>>>>>>>>", key)
            eval(f"testing.{program_dict[key]}")
            time.sleep(2)

    testing.driver_quit()
# keys_to_run = ["eve_284", "eve_21", "eve_158", "eve_159", "eve_160", "eve_162", "eve_249", "eve_344", "eve_267", "eve_338", "eve_99"]
keys_to_run = ["eve_158"]

run_program()



