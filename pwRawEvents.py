import time
import pyautogui
from EventPlaywright import EventAutomation


class RawEventsTesting(EventAutomation):

    def __init__(self):
        super().__init__()
    
    #prodct page 
    def eve_24(self, url):
        self.request_func(url)
        related_pd = '//*[@id="eve_24"]'  #24
        self.finds_elements(related_pd)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '24'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_25(self, url):
        self.request_func(url)
        view_more_btn = '//*[@id="eve_25"]'  #25
        self.finds_elements(view_more_btn)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '25'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_26(self, url):
        self.request_func(url)
        related_pd_cart = '//*[@class="cartBtn related_product_cart"]' 
        self.finds_elements(related_pd_cart)
        self.print_visitor_id()
        con = "BP"
        val1 = '# Product Tiltle'
        val2 = ''
        eve_id = '26'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_52(self, url):
        self.request_func(url)
        time.sleep(2)
        self.finds_elements('//*[@id="eve_52"]/a')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '52'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_53(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_52"]/div[4]/div')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '53'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_54(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_52"]/a')
        self.back()
        recently_view_pd = '//*[@id="eve_54"]'  #54
        self.finds_elements(recently_view_pd)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '54'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_55(self, url):
        self.request_func(url)
        product_click = '//*[@id="eve_55"]'  # 55
        self.finds_elements(product_click)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '55'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_56(self, url):
        self.request_func(url)
        # self.element_hover('(//*[@class="includes_item"])[5]')
        left_click = '//*[@id="eve_57"]'  # 57
        self.finds_elements(left_click)
        left_click = '//*[@id="eve_56"]'  # 56
        self.finds_elements(left_click)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '56'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_57(self, url):
        self.request_func(url)
        left_click = '//*[@id="eve_57"]'  # 57
        self.finds_elements(left_click)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '57'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_80(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="junking_color"]/li[2]/a')
        print('filter')
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '80'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_317(self, url):
        self.request_func(url)
        self.chat_box_close()
        other_also_viewed_cart = '//*[@class="rpt_green_btn rfq-btn"]'  
        self.finds_elements(other_also_viewed_cart)
        self.chat_box_close()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '317'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_404(self, url):
        self.request_func(url)
        rfq = '//*[@class="rfq-btn"]'
        self.finds_elements(rfq)
        self.print_visitor_id()
        con = ""
        val1 = 'VAl'
        val2 = 'mpn'
        eve_id = '404'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)
    # branding Page
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
    
    #b2b benefits

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
        self.back()
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
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '250'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    # about us

    def eve_245(self, url):
        self.request_func(url)
        time.sleep(1)
        self.finds_elements('//*[@id="eve_245"]')
        self.back()
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
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '246'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_247(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_247"]')
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '247'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    def eve_248(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_248"]')
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '248'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    #contact us

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
    
    # Home page
    def eve_116(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="promotionalslid"]/div[2]/button[2]'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="promotionalslid"]/div[1]/div/div[4]/div/div/div')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        
        val2 = '#URL'
        eve_id = '116'
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
    
    def eve_118(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="eve_118"]'
        self.finds_elements(comment)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#name'
        val2 = '#URL'
        eve_id = '118'
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

    def eve_121(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="eve_121"]'
        self.finds_elements(comment)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '121'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id) 


    def eve_122(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="eve_122"]/div[1]/div/h4/a'
        self.finds_elements(comment)
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#blog_title'
        val2 = ''
        eve_id = '122'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    #L1 And L2

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
    
    #RFQ Pop-up 
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
    
    # Website
    def eve_290(self, url):
        self.request_func(url)
        add_to_cart = "//*[@id='eve_38']"

        self.finds_elements(add_to_cart)
        self.chat_box_close()
        time.sleep(2)
        self.finds_elements("//*[@id='eve_290']")
        # self.driver.execute_script("arguments[0].click();", add_Quantity)

        # self.finds_elements(add_Quantity)
        self.print_visitor_id()
        con = "BP"
        val1 = '# Quantity Before'
        val2 = '# Quantity After'
        eve_id = '290'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_291(self, url):
        self.request_func(url)
        add_to_cart = "//*[@id='eve_38']"
        # self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        self.finds_elements("//*[@id='eve_290']")
        # self.driver.execute_script("arguments[0].click();", add_Quantity)
        self.finds_elements("(//*[@id='eve_291'])")
        # self.driver.execute_script("arguments[0].click();", reduce_Quantity)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Title'
        val2 = ''
        eve_id = '291'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_292(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        # self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Trash_bin = self.finds_elements("//*[@id='eve_292']")
        # self.driver.execute_script("arguments[0].click();", click_On_Trash_bin)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Title'
        val2 = ''
        eve_id = '292'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_293(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        self.finds_elements("//*[@id='eve_293']/a")

        self.print_visitor_id()
        con = "BP"
        val1 = 'Title'
        val2 = 'Subtotal with Currency'
        eve_id = '293'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_294(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        self.finds_elements("//*[@id='eve_294']/a")
        self.back()
        time.sleep(5)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Title'
        val2 = 'Subtotal with Currency'
        eve_id = '294'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_295(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        self.finds_elements("//*[@id='eve_295']")

        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '295'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    
    # Discontinued 
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
    def eve_388(self, url):
        self.request_func(url)
        comment = '//*[@id="maindis"]/div/table/tbody/tr[1]'
        self.finds_elements(comment)
        # self.back()
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '388'
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
    def eve_393(self, url):
        self.request_func(url)
        comment = '//*[@id="maindis"]/div/table/tbody/tr[1]/td[5]/button'
        self.finds_elements(comment)
        # self.back()
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '393'
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

    #search result

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
    def eve_274(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_274"]')
        # self.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '274'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_275(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_275"]')
        # self.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '275'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    def eve_276(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_276"]')
        # self.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '276'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    # Form No search reasult 
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
    
    # Form credit card
    def eve_158(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_163"]', 'company name')
        self.finds_elements('//*[@id="eve_164"]', '1234567')
        self.finds_elements('//*[@id="eve_166"]', '12')
        self.finds_elements('//*[@id="eve_161"]/option[2]')
        self.finds_elements('//*[@id="eve_162"]', '1234567')
        self.finds_elements('//*[@id="eve_168"]', 'Akshat Vila')
        self.finds_elements('//*[@id="eve_169"]', 'delhi')
        self.finds_elements('//*[@id="eve_170"]', '110044')
        self.finds_elements(' //*[@id="eve_171"]/option[7]')
        self.finds_elements('//*[@id="next-btn2"]')
        self.finds_elements('//*[@id="eve_158"]', 'Arch')
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
        self.finds_elements('//*[@id="eve_159"]', 'rahul@raptorsupplies.co.uk')
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
        # self.back()
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
    
    # Form Vendor registration 
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


    # Form Request A qout
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
    
    # Form Sbmit purchase

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
    # where we deliver

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
    def eve_79(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_77"]','a')
        self.finds_elements('//*[@id="wherewedeliverul"]/li[1]/div/a')
        self.back()
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
        # self.back()
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
        # self.back()
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
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#item'
        val2 = '#language'
        eve_id = '88'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    #brand page
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
    def eve_63(self, url):
        self.request_func(url)
        self.finds_elements('//*[@class="rfq-btn"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '63'
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
    
    #category
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
    
    # signup
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
    def eve_254(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_254"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '254'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    #My account
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
    
    # garinger
    def eve_249(self, url):
        self.request_func(url)
        self.finds_elements("(//*[@id='eve_249'])")
        
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = '# url'
        eve_id = '249'
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
    def eve_344(self, url):
        self.request_func(url)
        time.sleep(3)
        # self.finds_elements("//*[@id='eve_344']")
        self.reload()
        time.sleep(2)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '344'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)
    # terms and conditions
    def eve_253(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_253"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '253'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)

    #Header    
    def eve_9(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_9']")
        # self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '9'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_13(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_13']")
        # self.driver.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '13'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_16(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_16']")
        pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '16'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_18(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_18']")
        pyautogui.press('enter')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '18'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)
    def eve_76(self, url):
        self.request_func(url)
        self.finds_elements("//*[@class='connect_us contactus']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '76'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_89(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_89']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '89'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_302(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_302']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '302'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_304(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_304']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '304'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)
    
    #footer
    def eve_21(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_21"]/ul/li[3]/a')
        
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '21'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    #Category forklft
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
    
    def eve_69(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_69"]'
        self.finds_elements(comment)
        self.back()
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = '#title'
        val2 = 'image'
        eve_id = '69'
        self.report_genrate(self.print_visitor_id(),con,val1,val2,eve_id)
    
    def eve_71(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_71"]/label/div[1]/img'
        self.finds_elements(comment)
        self.back()
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = '#category'
        val2 = 'Title'
        eve_id = '71'
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
        
        # about us 23
        'eve_245' : 'eve_245("https://www.raptorsupplies.com/about-us")',
        'eve_246' : 'eve_246("https://www.raptorsupplies.com/about-us")',
        'eve_247' : 'eve_247("https://www.raptorsupplies.com/about-us")',
        'eve_248' : 'eve_248("https://www.raptorsupplies.com/about-us")',
        # end about us 27

        # contact us 27
        'eve_236' : 'eve_236("https://www.raptorsupplies.com/contact")',
        'eve_237' : 'eve_237("https://www.raptorsupplies.com/contact")',
        'eve_238' : 'eve_238("https://www.raptorsupplies.com/contact")',
        'eve_239' : 'eve_239("https://www.raptorsupplies.com/contact")',
        'eve_240' : 'eve_240("https://www.raptorsupplies.com/contact")',
        'eve_241' : 'eve_241("https://www.raptorsupplies.com/contact")',   
        'eve_242' : 'eve_242("https://www.raptorsupplies.com/contact")',
        'eve_243' : 'eve_243("https://www.raptorsupplies.com/contact")',
        'eve_244' : 'eve_244("https://www.raptorsupplies.com/contact")',
        #end Contact Us 36

        # Home page 36
        'eve_116' : 'eve_116("https://www.raptorsupplies.com/")',
        'eve_117' : 'eve_117("https://www.raptorsupplies.com/")',
        'eve_118' : 'eve_118("https://www.raptorsupplies.com/")',
        'eve_120' : 'eve_120("https://www.raptorsupplies.com/")',
        'eve_121' : 'eve_121("https://www.raptorsupplies.com/")',
        'eve_122' : 'eve_122("https://www.raptorsupplies.com/")',
        # Home page 42

        # L1 and L2 42
        'eve_104' : 'eve_104("https://www.raptorsupplies.com/l1/abrasives")',
        'eve_105' : 'eve_105("https://www.raptorsupplies.com/l1/abrasives")',
        'eve_106' : 'eve_106("https://www.raptorsupplies.com/l1/abrasives")',
        'eve_107' : 'eve_107("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        # End L1 and L2 46

        # RFQ Pop-up 46
        'eve_40' : 'eve_40("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_41' : 'eve_41("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_42' : 'eve_42("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_43' : 'eve_43("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_44' : 'eve_44("https://www.raptorsupplies.com/pd/morse-drum/91")',
        # END RFQ 51

        # website 51
        'eve_290' : 'eve_290("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        'eve_291' : 'eve_291("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        'eve_292' : 'eve_292("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        'eve_293' : 'eve_293("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        'eve_294' : 'eve_294("https://www.raptorsupplies.com/pd/proto/jsf20m")', 
        'eve_295' : 'eve_295("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        # End Website 57

        #Discontinued item 57
        'eve_386' : 'eve_386("https://www.raptorsupplies.com/obsolete-brand-pages")',
        'eve_388' :  'eve_388("https://www.raptorsupplies.com/obsolete/ampg")',
        'eve_389' :  'eve_389("https://www.raptorsupplies.com/obsolete/ampg")',
        'eve_390' :  'eve_390("https://www.raptorsupplies.com/obsolete/ampg")',
        'eve_393' :  'eve_393("https://www.raptorsupplies.com/obsolete/ampg")',
        'eve_397' :  'eve_397("https://www.raptorsupplies.com/obsolete/ampg")',
        'eve_403' :  'eve_403("https://www.raptorsupplies.com/obsolete/ampg")',
        #Discontinued item 64

        #search result 64
        'eve_272' :  'eve_272("https://www.raptorsupplies.com/s?q=1234")',
        'eve_273' :  'eve_273("https://www.raptorsupplies.com/s?q=1234")',
        'eve_274'  :  'eve_274("https://www.raptorsupplies.com/s?q=m1")',
        'eve_275'  :  'eve_275("https://www.raptorsupplies.com/s?q=m1")',
        'eve_276'  :  'eve_276("https://www.raptorsupplies.com/s?q=m1")',

        #No Search Result 69
        'eve_377' :  'eve_377("https://www.raptorsupplies.com/s/no-results?q=bdndbjfjf")',
        'eve_378' :  'eve_378("https://www.raptorsupplies.com/s/no-results?q=bdndbjfjf")',
        'eve_379' :  'eve_379("https://www.raptorsupplies.com/s/no-results?q=bdndbjfjf")',
        'eve_380' :  'eve_380("https://www.raptorsupplies.com/s/no-results?q=bdndbjfjf")',
        'eve_381' :  'eve_381("https://www.raptorsupplies.com/s/no-results?q=bdndbjfjf")',
        # No Search Result 74

        # form credit card form 74
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
        #End Credit card Form 86

        # vendor-registration 87
        
        'eve_132' : 'eve_132("https://www.raptorsupplies.com/vendor-registration")',
        'eve_133' : 'eve_133("https://www.raptorsupplies.com/vendor-registration")', 
        'eve_134' : 'eve_134("https://www.raptorsupplies.com/vendor-registration")',
        # End vendor-registration 99

        # Form Rquest a qoute
        'eve_124' : 'eve_124("https://www.raptorsupplies.com/request-for-quote")',
        'eve_125' : 'eve_125("https://www.raptorsupplies.com/request-for-quote")',
        'eve_126' : 'eve_126("https://www.raptorsupplies.com/request-for-quote")',
        'eve_127' : 'eve_127("https://www.raptorsupplies.com/request-for-quote")',
        'eve_128' : 'eve_128("https://www.raptorsupplies.com/request-for-quote")',
        'eve_384' : 'eve_384("https://www.raptorsupplies.com/request-for-quote")',
        'eve_383' : 'eve_383("https://www.raptorsupplies.com/request-for-quote")',

        #Form Submit purchase order

        'eve_286' : 'eve_286("https://www.raptorsupplies.com/submit-purchase-order")',
        'eve_287' : 'eve_287("https://www.raptorsupplies.com/submit-purchase-order")',
        # where we deliver
        'eve_77' : 'eve_77("https://www.raptorsupplies.com/where-we-deliver")',
        'eve_78' : 'eve_78("https://www.raptorsupplies.com/where-we-deliver")',
        'eve_79' : 'eve_79("https://www.raptorsupplies.com/where-we-deliver")',
        'eve_86' : 'eve_86("https://www.raptorsupplies.com/where-we-deliver")',
        'eve_87' : 'eve_87("https://www.raptorsupplies.com/where-we-deliver")',
        'eve_88' : 'eve_88("https://www.raptorsupplies.com/where-we-deliver")',

        # brand page
        'eve_59' : 'eve_59("https://www.raptorsupplies.com/b/ad-weighing")',
        'eve_61' : 'eve_61("https://www.raptorsupplies.com/b/char-lynn")',
        'eve_62' : 'eve_62("https://www.raptorsupplies.com/b/char-lynn")',
        'eve_63' : 'eve_63("https://www.raptorsupplies.com/b/char-lynn")',
        'eve_354' : 'eve_354("https://www.raptorsupplies.com/b/allegro-safety")',
        'eve_355' : 'eve_355("https://www.raptorsupplies.com/b/allegro-safety")',
        'eve_356' : 'eve_356("https://www.raptorsupplies.com/b/allegro-safety")',

        #category
        'eve_70'  :  'eve_70("https://www.raptorsupplies.com/c/fasteners/c3/hex-head-cap-screws")',
        # Filter (Compare) forklft
        'eve_282' :  'eve_282("https://www.raptorsupplies.com/c/fork-mounted-drum-handling-equipment")',
        'eve_284' :  'eve_284("https://www.raptorsupplies.com/c/fork-mounted-drum-handling-equipment")',

        # sign up 
        'eve_335' : 'eve_335("https://www.raptorsupplies.com/create")',
        'eve_336' : 'eve_336("https://www.raptorsupplies.com/create")',
        'eve_337' : 'eve_337("https://www.raptorsupplies.com/create")',
        'eve_338' : 'eve_338("https://www.raptorsupplies.com/create")',
        'eve_339' : 'eve_339("https://www.raptorsupplies.com/create")',

        # return policy
        'eve_254' : 'eve_254("https://www.raptorsupplies.com/return-policy")',

        # my account
        'eve_269' : 'eve_269("https://www.raptorsupplies.com/")',
        'eve_270' :  'eve_270("https://www.raptorsupplies.com/")',
        'eve_271' :  'eve_271("https://www.raptorsupplies.com/")',
        'eve_267' :  'eve_267("https://www.raptorsupplies.com/")',
        'eve_266' :  'eve_266("https://www.raptorsupplies.com/")',

        # grainger
        'eve_249' :  'eve_249("https://www.raptorsupplies.com/ww-grainger-dealer")',

        #
        'eve_283' :  'eve_283("https://www.raptorsupplies.com/c/fork-mounted-drum-handling-equipment")',

        #
        'eve_344' :  'eve_344("https://www.raptorsupplies.com/check/cart")',

        # terms and conditions
        'eve_253' : 'eve_253("https://www.raptorsupplies.com/terms-conditions")',

        #Header
        'eve_9': 'eve_9("https://www.raptorsupplies.com/")',
        'eve_13': 'eve_13("https://www.raptorsupplies.com/")',
        'eve_16': 'eve_16("https://www.raptorsupplies.com/")',
        'eve_18': 'eve_18("https://www.raptorsupplies.com/")',
        'eve_76': 'eve_76("https://www.raptorsupplies.com/")',
        'eve_89': 'eve_89("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_302': 'eve_302("https://www.raptorsupplies.com/")',
        'eve_304': 'eve_304("https://www.raptorsupplies.com/")',

        #footer
        'eve_21' :  'eve_21("https://www.raptorsupplies.com/")',

        #
        'eve_285' : 'eve_285("https://www.raptorsupplies.com/c/fork-mounted-drum-handling-equipment")',

        #
        'eve_69'  : 'eve_69("https://www.raptorsupplies.com/c/fasteners/c3/hex-head-cap-screws")',
        'eve_71'  : 'eve_71("https://www.raptorsupplies.com/c/fasteners/c4/nylon-hex-head-cap-screws")',
        'eve_285' : 'eve_285("https://www.raptorsupplies.com/c/fork-mounted-drum-handling-equipment")',
        'eve_319' : 'eve_319("https://www.raptorsupplies.com/c/fasteners/c3/adhesive-anchors")',
      }  

    testing = RawEventsTesting()
    # keys = list(program_dict.keys())
    # start_index = 127
    # for i, key in enumerate(keys[start_index:], start_index):
    #     print(i, ">>>>>>>>>>> Working Template >>>>>>>>>", key), eval(f"testing.{program_dict[key]}")
    #     time.sleep(2)
    for key in keys_to_run:
        if key in program_dict:
            print(">>>>>>>>>>> Working Template >>>>>>>>>", key)
            eval(f"testing.{program_dict[key]}")
            time.sleep(2)

    testing.driver_quit()

keys_to_run = ["eve_71","eve_319"]

run_program()



