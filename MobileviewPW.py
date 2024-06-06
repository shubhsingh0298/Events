import time
from EventAutomationBaseClass import EventAutomation
from selenium.webdriver.chrome.options import ChromiumOptions

class RawEventsTesting(EventAutomation):
     def __init__(self):
        options = ChromiumOptions()  
        super().__init__(options)
        options = ChromiumOptions()
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        super().__init__(options)   
          
     def eve_212(self, url):
        self.mobile_screen_request(url)
        # self.chat_box_close()
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
        time.sleep(10)
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
        # time.sleep(10)
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        self.finds_elements("//span[@id='eve_214' and @class='category_click']")
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '214'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
     def eve_215(self, url):
        self.mobile_screen_request(url)
        # time.sleep(10)
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        print('icon click')
        self.finds_elements("//span[@id='eve_215' and @class ='brands_click']")
        print('brand click')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '215'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
     def eve_216(self, url):
        self.mobile_screen_request(url)
        # time.sleep(10)
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        self.finds_elements('//*[@id="eve_212"]')
        print('sign in')
        self.finds_elements('//*[@id="email"]', 'shubham@raptorsupplies.co.uk')
        print('username')
        self.finds_elements('//*[@id="pass"]', 'Shubham@123')
        print('password')
        self.chat_box_close()
        self.finds_elements('//*[@id="send2"]')
        print('login')
        # self.driver.back()
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        print('icon click')
        self.finds_elements("//*[@id='eve_216']/span")  
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
        self.finds_elements('//*[@id="eve_212"]')
        print('sign in')
        self.finds_elements('//*[@id="email"]', 'shubham@raptorsupplies.co.uk')
        print('username')
        self.finds_elements('//*[@id="pass"]', 'Shubham@123')
        print('password')
        self.chat_box_close()
        self.finds_elements('//*[@id="send2"]')
        print('login')
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        print('icon click')
        self.finds_elements("//*[@id='eve_217']/span")
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
        self.finds_elements('//*[@id="eve_212"]')
        print('sign in')
        self.finds_elements('//*[@id="email"]', 'shubham@raptorsupplies.co.uk')
        print('username')
        self.finds_elements('//*[@id="pass"]', 'Shubham@123')
        print('password')
        self.chat_box_close()
        self.finds_elements('//*[@id="send2"]')
        print('login')
        self.finds_elements('//*[@class="sprite mobile-toggle"]')
        print('icon click')
        self.finds_elements("//*[@id='eve_218']/span[1]")
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
        # self.chat_box_close()
        self.finds_elements( "//a[@href='/faq']")
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
        self.finds_elements("//a[@href='/terms-conditions']")
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
        self.finds_elements('//*[@id="eve_223"]/li[2]')
        
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

     def eve_227(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        # self.chat_box_close()
        self.finds_elements("//*[contains(@class, 'filter-title') and text()='Brand']")
        time.sleep(3)
        self.finds_elements('//*[@id="brandFilter"]/div/label[1]')
        self.finds_elements('//*[@id="eve_224"]')
        element = self.driver.find_element(By.ID, 'abc')
        self.driver.execute_script("arguments[0].click();", element)
        self.print_visitor_id()
        con = "BP"
        val1 = '# Filter_name'
        val2 = '# filter1 value1 | value 2..'
        eve_id = '227'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)
    
     def eve_228_l2(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        # self.chat_box_close()
        self.finds_elements('//*[@id="at_brand"]')
        time.sleep(3)
        self.finds_elements('//*[@id="brandFilter"]/div/label[1]')
        self.finds_elements("//*[@id='fil 465895' and text()='3M']")
        self.print_visitor_id()
        con = "BP"
        val1 = '# Filter_name'
        val2 = '# filter1 value1 | value 2..'
        eve_id = '228'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)
     def eve_228_fastner(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        # self.chat_box_close()
        self.finds_elements('//*[@id="at_brand"]')
        time.sleep(3)
        self.finds_elements('//*[@id="brandFilter"]/div/label[1]')
        # self.finds_elements("//span[@class='filter-title' and text()='Brand']")
        self.finds_elements("//*[@id='fil 466048' and text()='ANVIL']")
        self.print_visitor_id()
        con = "BP"
        val1 = '# Filter_name'
        val2 = '# filter1 value1 | value 2..'
        eve_id = '228'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)
     def eve_15_pd(self, url):
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
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)
     def eve_15_mother(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='addto_cart']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        time.sleep(2)
        close_cart_popup = '//*[@id="eve_295"]'
        self.finds_elements(close_cart_popup)
        shop_cart = "//span[@class='cart_icon add-to-cart-button']"
        self.finds_elements(shop_cart)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#pd count'
        val2 = ''
        eve_id = '15'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)
     def eve_15_l3(self, url):
        self.request_func(url)
        add_to_cart = "//*[@id='atc_0']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        time.sleep(2)
        close_cart_popup = '//*[@id="eve_295"]'
        self.finds_elements(close_cart_popup)
        shop_cart = "//span[@class='cart_icon add-to-cart-button']"
        self.finds_elements(shop_cart)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#pd count'
        val2 = ''
        eve_id = '15'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)
     def eve_15_brand(self, url):
        self.request_func(url)
        shop_cart = "//span[@class='cart_icon add-to-cart-button']"
        self.finds_elements(shop_cart)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#pd count'
        val2 = ''
        eve_id = '15'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)
     def eve_15_l2(self, url):
        self.request_func(url)
        shop_cart = "//span[@class='cart_icon add-to-cart-button']"
        self.finds_elements(shop_cart)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#pd count'
        val2 = ''
        eve_id = '15'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)
     def eve_15_home(self, url):
        self.request_func(url)
        shop_cart = "//span[@class='cart_icon add-to-cart-button']"
        self.finds_elements(shop_cart)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#pd count'
        val2 = ''
        eve_id = '15'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)

     def eve_15_grainger(self,url):
        self.request_func(url)
        shop_cart = "//span[@class='cart_icon add-to-cart-button']"
        self.finds_elements(shop_cart)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#pd count'
        val2 = ''
        eve_id = '15'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)


     def eve_224_l2(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '224'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)
     def eve_224_l3(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '224'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)
     def eve_224_bfc(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '224'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)
     def eve_224_p(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '224'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)
     def eve_224_c3(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '224'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)

      def eve_224_c4(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '224'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)

     def eve_225_c3(self,url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        time.sleep(2)
        self.finds_elements("//h4[contains(@class, 'filter-title') and text()='Length']")
        self.finds_elements("//*[@id='96']")
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '225'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)

      def eve_225_c4(self,url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        time.sleep(2) 
        self.finds_elements("//h4[contains(@class, 'filter-title') and text()='Length']")
        self.finds_elements("//*[@id='1085']")
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '225'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)

      def eve_225_l2(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        time.sleep(2)
        self.finds_elements("//span[contains(@class, 'filter-title') and text()='Brand']")
        self.finds_elements("//*[@id='brandFilter']/div/label[1]")
        self.print_visitor_id()
        con = ""
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '225'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)
   
      def eve_225_l3(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        time.sleep(2)
        self.finds_elements("//span[contains(@class, 'filter-title') and text()='Item']")
        self.finds_elements("//*[@id='469097']")
        self.print_visitor_id()
        con = ""
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '225'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)
    
      def eve_225_bfc(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        time.sleep(2)
        self.finds_elements("//span[contains(@class, 'filter-title') and text()='Item']")
        self.finds_elements("//*[@id='510828']")
        self.print_visitor_id()
        con = ""
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '225'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)
    
     def eve_225_p(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        time.sleep(2)
        self.finds_elements("//span[@class='filter-title' and text()='Item']")
        self.finds_elements("//label[@id='487359' and @class='nkVisible']")
        self.print_visitor_id()
        con = ""
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '225'
        self.report_genrate_global(self.print_visitor_id(),con,val1,val2,eve_id,url)

      def eve_226_l3(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.finds_elements("//h4[contains(@class, 'filter-title') and text()='Length']")
        self.finds_elements("//div[@class='serachfilter']/input[@class='search-query filter_Fastener_search']","8")
        self.finds_elements("//*[@id='filtersection']/div[1]/div/div[1]/span")
        self.print_visitor_id()
        con = ""
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '226'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

      def eve_226_l4(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.finds_elements("//h4[contains(@class, 'filter-title') and text()='Thread Length']")
        self.finds_elements("//div[@class='serachfilter']/input[@class='search-query filter_Fastener_search']", "3/8")
        self.finds_elements("//*[@id='filtersection']/div[1]/div/div[1]/span")
        self.print_visitor_id()
        con = ""
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '226'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

      def eve_226_mother(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.finds_elements("//*[@id='at_22542']")
        self.finds_elements("//*[@id='a_22542']", "8")
        self.finds_elements("/html/body/section[2]/div/div/div[1]/aside/div/div/div[2]/div/div/div/div/div[1]/span/i")
        self.print_visitor_id()
        con = ""
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '226'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)
def run_program():
    program_dict = {

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
        #end idx=15
        #Global
        #idx=16
        'eve_227' : 'eve_227("https://www.raptorsupplies.com/l2/abrasive-accessories")',
       
        'eve_228_l2' : 'eve_228_l2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_228_fastner' : 'eve_228_fastner("https://www.raptorsupplies.com/fasteners/anchors")',
        
        'eve_15_home':'eve_15_home("https://www.raptorsupplies.com/")',
        'eve_15_l2':'eve_15_l2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_15_brand':'eve_15_brand("https://www.raptorsupplies.com/b/3m")',
        'eve_15_mother':'eve_15_mother("https://www.raptorsupplies.com/p/norton/mandrel-assembly")',
        'eve_15_grainger':'eve_15_grainger("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_15_l3':'eve_15_l3("https://www.raptorsupplies.com/c/abrasive-mandrels")',
        'eve_15_pd':'eve_15_pd("https://www.raptorsupplies.com/pd/norton/66261059422")',
        
        'eve_224_l2':'eve_224_l2("https://www.raptorsupplies.com/l2/bags-and-bag-accessories")',
        'eve_224_l3':'eve_224_l3("https://www.raptorsupplies.com/c/non-adhesive-material-cutter-accessories")',
        'eve_224_bfc':'eve_224_bfc("https://www.raptorsupplies.com/c/respirator-accessories/3m")',
        'eve_224_p':'eve_224_p("https://www.raptorsupplies.com/p/norton/mandrel-assembly")',
        'eve_224_c3':'eve_224_c3("https://www.raptorsupplies.com/c/fasteners/c3/adhesive-anchor-accessories")',
        'eve_224_c4':'eve_224_c4("https://www.raptorsupplies.com/c/fasteners/c4/grade-18-8-stainless-steel-hex-head-cap-screws")',
        
        'eve_225_l2':'eve_225_l2("https://www.raptorsupplies.com/l2/bags-and-bag-accessories")',
        'eve_225_l3':'eve_225_l3("https://www.raptorsupplies.com/c/non-adhesive-material-cutter-accessories")',
        'eve_225_bfc':'eve_225_bfc("https://www.raptorsupplies.com/c/respirator-accessories/3m")',
        'eve_225_p':'eve_225_p("https://www.raptorsupplies.com/p/norton/mandrel-assembly")',
        'eve_225_c3':'eve_225_c3("https://www.raptorsupplies.com/c/fasteners/c3/adhesive-anchor-accessories")',
        'eve_225_c4':'eve_225_c4("https://www.raptorsupplies.com/c/fasteners/c4/grade-18-8-stainless-steel-hex-head-cap-screws")',
        
        'eve_226_l4': 'eve_226_l4("https://www.raptorsupplies.com/c/fasteners/c4/grade-18-8-stainless-steel-hex-head-cap-screws")',
        'eve_226_mother': 'eve_226_mother("https://www.raptorsupplies.com/c/fasteners/p/epoxy-adhesive-anchors")',
        'eve_226_l3': 'eve_226_l3("https://www.raptorsupplies.com/c/fasteners/c3/adhesive-anchor-accessories")',
        }
    testing = RawEventsTesting()
    keys = list(program_dict.keys())
    # start_index = 34
    # for i, key in enumerate(keys[start_index:], start_index):
    #     print(i, ">>>>>>>>>>> Working Template >>>>>>>>>", key), eval(f"testing.{program_dict[key]}")
    #     time.sleep(5)
    for key in keys_to_run:
        if key in program_dict:
            print(">>>>>>>>>>> Working Template >>>>>>>>>", key)
            eval(f"testing.{program_dict[key]}")
            # time.sleep(2)

    testing.driver_quit()
keys_to_run = ["eve_226_mother"]
run_program()

