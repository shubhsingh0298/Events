import time
import pyautogui
from EventPlaywright import EventAutomation


class RawEventsTesting(EventAutomation):

    def __init__(self):
        super().__init__()
    #product 
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

    def eve_354(self, url):
        self.request_func(url)
        self.finds_elements('//*[@name="name"]', 'rahul')  #354
        print('Name Field')
        self.finds_elements('//*[@id="brand_form"]/div/div[7]/button')  #357, 358
        print('Sumbit Click')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '354'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_355(self, url):
        self.request_func(url)
        self.finds_elements('//*[@name="email"]', 'rahul@raptorsupplies.co.uk')  #355
        print("Email Field")
        self.finds_elements('//*[@class="discoun_brand_sem_btn-default sendbutton"]')  #357, 358
        print('Sumbit Click')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '355'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_356(self, url):
        self.request_func(url)
        self.finds_elements('//*[@name="phone"]', '9999999999')  #356
        print('Number Field')
        self.finds_elements('//*[@class="discoun_brand_sem_btn-default sendbutton"]')  #357, 358
        print('Sumbit Click')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '356'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_124(self, url):
        self.request_func(url)
        name_in_Form = "(//*[@id='eve_124'])"
        self.finds_elements(name_in_Form, 'xyz')
        click_On_Get_A_Quote = "(//*[text()='Get Quote Now'])"
        self.finds_elements(click_On_Get_A_Quote)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Text'
        val2 = ''
        eve_id = '124'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_125(self, url):
        self.request_func(url)

        #RFQ Email
        email_in_Form = "//*[@id='eve_125']"
        self.finds_elements(email_in_Form, 'shubham@raptorsupplies.co.uk')
        #Click on Get a Quote
        click_On_Get_A_Quote = "(//*[text()='Get Quote Now'])"
        self.finds_elements(click_On_Get_A_Quote)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Text'
        val2 = ''
        eve_id = '125'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_126(self, url):
        self.request_func(url)
        phoneNo_in_Form = '#eve_126'
        self.finds_elements(phoneNo_in_Form, '8294966962')
        click_On_Get_A_Quote = "(//*[text()='Get Quote Now'])"
        self.finds_elements(click_On_Get_A_Quote)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Text'
        val2 = ''
        eve_id = '126'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_127(self, url):
        self.request_func(url)
        countryDropdown_in_Form = "(//*[@id='eve_127'])"
        self.finds_elements(countryDropdown_in_Form, 'Brazil')
        click_On_Get_A_Quote = "(//*[text()='Get Quote Now'])"
        self.finds_elements(click_On_Get_A_Quote)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Text'
        val2 = ''
        eve_id = '127'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_128(self, url):
        self.request_func(url)
        self.chat_box_close()
        #RFQ What items do  you need
        Items = "(//*[@id='eve_128'])"
        self.finds_elements(Items, 'Electronics')
        #Click on Get a Quote
        click_On_Get_A_Quote = "(//*[text()='Get Quote Now'])"
        self.finds_elements(click_On_Get_A_Quote)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Text'
        val2 = ''
        eve_id = '128'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

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
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

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
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

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
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

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
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_44(self, url):
        self.request_func(url)
        time.sleep(1)
        self.finds_elements("//*[@id='main_rfq_btn']")
        time.sleep(1)
        self.chat_box_close()
        select_locator = "select#eve_44"
        self.page.wait_for_selector(select_locator)
        option_text = "India"
        self.select_option_by_text(self.page, select_locator, option_text)
        self.print_visitor_id()
        con = "BP"
        val1 = '#country name'
        val2 = '#new country name'
        eve_id = '44'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

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

    def eve_272(self, url):
        self.request_func(url)
        self.finds_elements("//*[@class='brandproductbox brandproductbox2 search_cards_innerWrap box_shadow_hover']/a")
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Result Number'
        val2 = ''
        eve_id = '272'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_273(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='sortName']")
        self.finds_elements('//*[@class="parent"]//ul//li')
        self.print_visitor_id()
        con = ""
        val1 = 'Name'
        val2 = ''
        eve_id = '273'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_274(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_274"]')
        # self.driver.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '274'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_275(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_275"]')
        # self.driver.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '275'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_276(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_276"]')
        # self.driver.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '276'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

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

    def eve_192(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        time.sleep(5)
        email_Address = "#customer-email"
        self.finds_elements(email_Address, 'shubham@raptorsupplies.co.uk')
        first_Name = 'input[name="firstname"]'
        self.finds_elements(first_Name, 'Rahul')
        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '192'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_193(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        time.sleep(5)
        company_Name = 'input[name="company"]'
        self.finds_elements(company_Name, 'Raptor')
        address = 'input[name="street[0]"]'
        self.finds_elements(address, 'UK')
        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '193'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_194(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)

        company_Name = 'input[name="company"]'
        self.finds_elements(company_Name, 'Raptor')
        address = 'input[name="street[0]"]'
        self.finds_elements(address, 'UK')
        city_Name = 'input[name="city"]'
        self.finds_elements(city_Name, 'abc')
        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '194'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_195(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        city_Name = 'input[name="city"]'
        self.finds_elements(city_Name, 'delhi')
        company_Name = 'input[name="company"]'
        self.finds_elements(company_Name, 'Raptor')
        # country_Dropdown = 'select[name="country_id"]'
        # self.finds_elements(country_Dropdown, 'Oman')

        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '195'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_196(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        country_Dropdown = 'select[name="country_id"]'
        self.finds_elements(country_Dropdown, 'India')
        state_Or_Province = 'select[name="region_id"]'
        self.finds_elements(state_Or_Province, 'Goa')
        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '196'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_197(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        country_Dropdown = 'select[name="country_id"]'
        self.finds_elements(country_Dropdown, 'India')
        #State dropdown
        state_Or_Province = 'select[name="region_id"]'
        self.finds_elements(state_Or_Province, 'Assam')
        #Postal code
        postal_Code = 'input[name="postcode"]'
        self.finds_elements(postal_Code, '123456')

        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '197'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_198(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        postal_Code = 'input[name="postcode"]'
        self.finds_elements(postal_Code, '123456')
        phone_number = 'input[name="telephone"]'
        self.finds_elements(phone_number, '1234567890')
        company_Name = 'input[name="company"]'
        self.finds_elements(company_Name, 'Raptor')
        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '198'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_199(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        #Contact number
        phone_number = 'input[name="telephone"]'
        self.finds_elements(phone_number, '1234567890')
        #Click on continue or submit
        click_On_continue = 'input[name="postcode"]'
        self.finds_elements(click_On_continue,'123456')
        self.print_visitor_id()
        con = "BP"
        val1 = 'Text'
        val2 = ''
        eve_id = '199'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_200(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        #Email Id
        email_Address = "#customer-email"
        self.finds_elements(email_Address, 'shubham@raptorsupplies.co.uk')
        #First Name
        first_Name = "//*[@name='firstname']"
        self.finds_elements(first_Name, 'Abc')
        #Last Name
        last_Name = "(//*[@name='lastname'])"
        self.finds_elements(last_Name, 'Kumar')
        #Company Name
        company_Name = "(//*[@name='company'])"
        self.finds_elements(company_Name, 'Raptor')
        #Address
        address = "(//*[@name='street[0]'])"
        self.finds_elements(address, 'UK')
        #City_Name
        city_Name = "(//*[@name='city'])"
        self.finds_elements(city_Name, 'abc')
        #Country dropdown
        country_Dropdown = "(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown, 'India')
        #State dropdown
        state_Or_Province = "(//*[@name='region_id'])"
        self.finds_elements(state_Or_Province, 'Goa')
        # Postal code
        postal_Code = "(//*[@name='postcode'])"
        self.finds_elements(postal_Code, '123456')
        #Contact number
        phone_number = "(//*[@name='telephone'])"
        self.finds_elements(phone_number, '1234567890')
        self.disable_element('#eve_200')


        self.print_visitor_id()
        con = "BPN"
        val1 = 'Email'
        val2 = ''
        eve_id = '200'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_201(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        # Email Id
        email_Address = "#customer-email"
        self.finds_elements(email_Address, 'shubham@raptorsupplies.co.uk')
        # First Name
        first_Name = "//*[@name='firstname']"
        self.finds_elements(first_Name, 'Abc')
        # Last Name
        last_Name = "(//*[@name='lastname'])"
        self.finds_elements(last_Name, 'Kumar')
        # Company Name
        company_Name = "(//*[@name='company'])"
        self.finds_elements(company_Name, 'Raptor')
        # Address
        address = "(//*[@name='street[0]'])"
        self.finds_elements(address, 'UK')
        # City_Name
        city_Name = "(//*[@name='city'])"
        self.finds_elements(city_Name, 'abc')
        # Country dropdown
        country_Dropdown = "(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown, 'India')
        # State dropdown
        state_Or_Province = "(//*[@name='region_id'])"
        self.finds_elements(state_Or_Province, 'Goa')
        # Postal code
        postal_Code = "(//*[@name='postcode'])"
        self.finds_elements(postal_Code, '123456')
        # Contact number
        phone_number = "(//*[@name='telephone'])"
        self.finds_elements(phone_number, '1234567890')
        self.disable_element('#eve_200')
        self.get_by_label("Economy (6 - 10 days)")
        # page.get_by_label("Economy (6 - 10 days)").check()
        # page.get_by_role("row", name="Express (5 - 7 days) $").click()
        # page.get_by_label("Ex-Works Pickup").check()
        self.print_visitor_id()
        con = "BP"
        val1 = '#Freight Amount'
        val2 = 'shiping method'
        eve_id = '201'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_203(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        # Email Id
        email_Address = "#customer-email"
        self.finds_elements(email_Address, 'shubham@raptorsupplies.co.uk')
        # First Name
        first_Name = "//*[@name='firstname']"
        self.finds_elements(first_Name, 'Abc')
        # Last Name
        last_Name = "(//*[@name='lastname'])"
        self.finds_elements(last_Name, 'Kumar')
        # Company Name
        company_Name = "(//*[@name='company'])"
        self.finds_elements(company_Name, 'Raptor')
        # Address
        address = "(//*[@name='street[0]'])"
        self.finds_elements(address, 'UK')
        # City_Name
        city_Name = "(//*[@name='city'])"
        self.finds_elements(city_Name, 'abc')
        # Country dropdown
        country_Dropdown = "(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown, 'India')
        # State dropdown
        state_Or_Province = "(//*[@name='region_id'])"
        self.finds_elements(state_Or_Province, 'Goa')
        # Postal code
        postal_Code = "(//*[@name='postcode'])"
        self.finds_elements(postal_Code, '123456')
        # Contact number
        phone_number = "(//*[@name='telephone'])"
        self.finds_elements(phone_number, '1234567890')
        self.disable_element('#eve_200')
        self.get_by_label("Ex-Works Pickup")
        self.page.get_by_text("FedEx - International Priority").click()

        self.print_visitor_id()
        con = "BP"
        val1 = 'Courier Name'
        val2 = ''
        eve_id = '203'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_204(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        # Email Id
        email_Address = "#customer-email"
        self.finds_elements(email_Address, 'shubham@raptorsupplies.co.uk')
        # First Name
        first_Name = "//*[@name='firstname']"
        self.finds_elements(first_Name, 'Abc')
        # Last Name
        last_Name = "(//*[@name='lastname'])"
        self.finds_elements(last_Name, 'Kumar')
        # Company Name
        company_Name = "(//*[@name='company'])"
        self.finds_elements(company_Name, 'Raptor')
        # Address
        address = "(//*[@name='street[0]'])"
        self.finds_elements(address, 'UK')
        # City_Name
        city_Name = "(//*[@name='city'])"
        self.finds_elements(city_Name, 'abc')
        # Country dropdown
        country_Dropdown = "(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown, 'India')
        # State dropdown
        state_Or_Province = "(//*[@name='region_id'])"
        self.finds_elements(state_Or_Province, 'Goa')
        # Postal code
        postal_Code = "(//*[@name='postcode'])"
        self.finds_elements(postal_Code, '123456')
        # Contact number
        phone_number = "(//*[@name='telephone'])"
        self.finds_elements(phone_number, '1234567890')
        self.disable_element('#eve_200')
        self.get_by_label("Ex-Works Pickup")
        self.page.get_by_text("FedEx - International Priority").click()
        #Pass ExWork-Account Number
        account_Number = "//*[@id='eve_204']"
        self.finds_elements(account_Number, '24654743254')
        click_On_Payment = "(//*[@id='proceed_payment'])"
        self.finds_elements(click_On_Payment)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Text'
        val2 = ''
        eve_id = '204'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_205(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        # Email Id
        email_Address = "#customer-email"
        self.finds_elements(email_Address, 'shubham@raptorsupplies.co.uk')
        # First Name
        first_Name = "//*[@name='firstname']"
        self.finds_elements(first_Name, 'Abc')
        # Last Name
        last_Name = "(//*[@name='lastname'])"
        self.finds_elements(last_Name, 'Kumar')
        # Company Name
        company_Name = "(//*[@name='company'])"
        self.finds_elements(company_Name, 'Raptor')
        # Address
        address = "(//*[@name='street[0]'])"
        self.finds_elements(address, 'UK')
        # City_Name
        city_Name = "(//*[@name='city'])"
        self.finds_elements(city_Name, 'abc')
        # Country dropdown
        country_Dropdown = "(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown, 'India')
        # State dropdown
        state_Or_Province = "(//*[@name='region_id'])"
        self.finds_elements(state_Or_Province, 'Goa')
        # Postal code
        postal_Code = "(//*[@name='postcode'])"
        self.finds_elements(postal_Code, '123456')
        # Contact number
        phone_number = "(//*[@name='telephone'])"
        self.finds_elements(phone_number, '1234567890')
        self.disable_element('#eve_200')
        self.get_by_label("Ex-Works Pickup")
        self.page.get_by_text("FedEx - International Priority").click()
        # Pass ExWork-Account Number
        account_Number = "//*[@id='eve_204']"
        self.finds_elements(account_Number, '24654743254')
        click_On_Payment = "//*[@id='proceed_payment']"
        self.finds_elements(click_On_Payment)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '205'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_206(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        # Email Id
        email_Address = "#customer-email"
        self.finds_elements(email_Address, 'shubham@raptorsupplies.co.uk')
        # First Name
        first_Name = "//*[@name='firstname']"
        self.finds_elements(first_Name, 'Abc')
        # Last Name
        last_Name = "(//*[@name='lastname'])"
        self.finds_elements(last_Name, 'Kumar')
        # Company Name
        company_Name = "(//*[@name='company'])"
        self.finds_elements(company_Name, 'Raptor')
        # Address
        address = "(//*[@name='street[0]'])"
        self.finds_elements(address, 'UK')
        # City_Name
        city_Name = "(//*[@name='city'])"
        self.finds_elements(city_Name, 'abc')
        # Country dropdown
        country_Dropdown = "(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown, 'India')
        # State dropdown
        state_Or_Province = "(//*[@name='region_id'])"
        self.finds_elements(state_Or_Province, 'Goa')
        # Postal code
        postal_Code = "(//*[@name='postcode'])"
        self.finds_elements(postal_Code, '123456')
        # Contact number
        phone_number = "(//*[@name='telephone'])"
        self.finds_elements(phone_number, '1234567890')
        self.disable_element('#eve_200')
        self.get_by_label("Ex-Works Pickup")
        self.page.get_by_text("FedEx - International Priority").click()
        # Pass ExWork-Account Number
        account_Number = "//*[@id='eve_204']"
        self.finds_elements(account_Number, '24654743254')
        click_On_Payment = "(//*[@id='proceed_payment'])"
        self.finds_elements(click_On_Payment)
        self.page.get_by_text("NET30 Payment").click()
        self.print_visitor_id()
        con = "BP"
        val1 = 'Name of Payment mode'
        val2 = ''
        eve_id = '206'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_207(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        # Email Id
        email_Address = "#customer-email"
        self.finds_elements(email_Address, 'shubham@raptorsupplies.co.uk')
        # First Name
        first_Name = "//*[@name='firstname']"
        self.finds_elements(first_Name, 'Abc')
        # Last Name
        last_Name = "(//*[@name='lastname'])"
        self.finds_elements(last_Name, 'Kumar')
        # Company Name
        company_Name = "(//*[@name='company'])"
        self.finds_elements(company_Name, 'Raptor')
        # Address
        address = "(//*[@name='street[0]'])"
        self.finds_elements(address, 'UK')
        # City_Name
        city_Name = "(//*[@name='city'])"
        self.finds_elements(city_Name, 'abc')
        # Country dropdown
        country_Dropdown = "(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown, 'India')
        # State dropdown
        state_Or_Province = "(//*[@name='region_id'])"
        self.finds_elements(state_Or_Province, 'Goa')
        # Postal code
        postal_Code = "(//*[@name='postcode'])"
        self.finds_elements(postal_Code, '123456')
        # Contact number
        phone_number = "(//*[@name='telephone'])"
        self.finds_elements(phone_number, '1234567890')
        self.disable_element('#eve_200')
        self.get_by_label("Ex-Works Pickup")
        self.page.get_by_text("FedEx - International Priority").click()
        # Pass ExWork-Account Number
        account_Number = "//*[@id='eve_204']"
        self.finds_elements(account_Number, '24654743254')
        click_On_Payment = "(//*[@id='proceed_payment'])"
        self.finds_elements(click_On_Payment)
        self.page.get_by_text("NET30 Payment").click()
        purschase_no = "//*[@id='eve_209']"
        self.finds_elements(purschase_no, '6547685')
        #Click on checkbox of credit card
        net_payment_Checkbox = "//*[@id='net_check']"
        self.finds_elements(net_payment_Checkbox)
        #Click on Place order
        place_Order="(//*[@id='net_real'])"
        self.finds_elements(place_Order)

        self.print_visitor_id()
        con = "BPN"
        val1 = 'Subtotal with Currency'
        val2 = ''
        eve_id = '207'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)
    def eve_209(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        # Email Id
        email_Address = "#customer-email"
        self.finds_elements(email_Address, 'shubham@raptorsupplies.co.uk')
        # First Name
        first_Name = "//*[@name='firstname']"
        self.finds_elements(first_Name, 'Abc')
        # Last Name
        last_Name = "(//*[@name='lastname'])"
        self.finds_elements(last_Name, 'Kumar')
        # Company Name
        company_Name = "(//*[@name='company'])"
        self.finds_elements(company_Name, 'Raptor')
        # Address
        address = "(//*[@name='street[0]'])"
        self.finds_elements(address, 'UK')
        # City_Name
        city_Name = "(//*[@name='city'])"
        self.finds_elements(city_Name, 'abc')
        # Country dropdown
        country_Dropdown = "(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown, 'India')
        # State dropdown
        state_Or_Province = "(//*[@name='region_id'])"
        self.finds_elements(state_Or_Province, 'Goa')
        # Postal code
        postal_Code = "(//*[@name='postcode'])"
        self.finds_elements(postal_Code, '123456')
        # Contact number
        phone_number = "(//*[@name='telephone'])"
        self.finds_elements(phone_number, '1234567890')
        self.disable_element('#eve_200')
        self.get_by_label("Ex-Works Pickup")
        self.page.get_by_text("FedEx - International Priority").click()
        # Pass ExWork-Account Number
        account_Number = "//*[@id='eve_204']"
        self.finds_elements(account_Number, '24654743254')
        click_On_Payment = "(//*[@id='proceed_payment'])"
        self.finds_elements(click_On_Payment)
        self.page.get_by_text("NET30 Payment").click()
        purschase_no = "//*[@id='eve_209']"
        self.finds_elements(purschase_no, '6547685')
        #Click on checkbox of credit card
        net_payment_Checkbox = "//*[@id='net_check']"
        self.finds_elements(net_payment_Checkbox)
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '209'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)
    def eve_210(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        # Email Id
        email_Address = "#customer-email"
        self.finds_elements(email_Address, 'shubham@raptorsupplies.co.uk')
        # First Name
        first_Name = "//*[@name='firstname']"
        self.finds_elements(first_Name, 'Abc')
        # Last Name
        last_Name = "(//*[@name='lastname'])"
        self.finds_elements(last_Name, 'Kumar')
        # Company Name
        company_Name = "(//*[@name='company'])"
        self.finds_elements(company_Name, 'Raptor')
        # Address
        address = "(//*[@name='street[0]'])"
        self.finds_elements(address, 'UK')
        # City_Name
        city_Name = "(//*[@name='city'])"
        self.finds_elements(city_Name, 'abc')
        # Country dropdown
        country_Dropdown = "(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown, 'India')
        # State dropdown
        state_Or_Province = "(//*[@name='region_id'])"
        self.finds_elements(state_Or_Province, 'Goa')
        # Postal code
        postal_Code = "(//*[@name='postcode'])"
        self.finds_elements(postal_Code, '123456')
        # Contact number
        phone_number = "(//*[@name='telephone'])"
        self.finds_elements(phone_number, '1234567890')
        self.disable_element('#eve_200')
        self.get_by_label("Ex-Works Pickup")
        self.page.get_by_text("FedEx - International Priority").click()
        # Pass ExWork-Account Number
        account_Number = "//*[@id='eve_204']"
        self.finds_elements(account_Number, '24654743254')
        click_On_Payment = "(//*[@id='proceed_payment'])"
        self.finds_elements(click_On_Payment)
        self.page.get_by_text("Proforma Invoice").click()
        purchase_Order = "(//*[@id='eve_210'])"
        self.finds_elements(purchase_Order, '4587698')
        profroma_Invoice_Checkbox = "//*[@id='performa_check']"
        self.finds_elements(profroma_Invoice_Checkbox)
        #Place order 
        # place_Order = "(//*[@id='performa_real'])"
        # self.finds_elements(place_Order)

        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '210'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_211(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        # Email Id
        email_Address = "#customer-email"
        self.finds_elements(email_Address, 'shubham@raptorsupplies.co.uk')
        # First Name
        first_Name = "//*[@name='firstname']"
        self.finds_elements(first_Name, 'Abc')
        # Last Name
        last_Name = "(//*[@name='lastname'])"
        self.finds_elements(last_Name, 'Kumar')
        # Company Name
        company_Name = "(//*[@name='company'])"
        self.finds_elements(company_Name, 'Raptor')
        # Address
        address = "(//*[@name='street[0]'])"
        self.finds_elements(address, 'UK')
        # City_Name
        city_Name = "(//*[@name='city'])"
        self.finds_elements(city_Name, 'abc')
        # Country dropdown
        country_Dropdown = "(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown, 'India')
        # State dropdown
        state_Or_Province = "(//*[@name='region_id'])"
        self.finds_elements(state_Or_Province, 'Goa')
        # Postal code
        postal_Code = "(//*[@name='postcode'])"
        self.finds_elements(postal_Code, '123456')
        # Contact number
        phone_number = "(//*[@name='telephone'])"
        self.finds_elements(phone_number, '1234567890')
        self.disable_element('#eve_200')
        self.get_by_label("Ex-Works Pickup")
        self.page.get_by_text("FedEx - International Priority").click()
        # Pass ExWork-Account Number
        account_Number = "//*[@id='eve_204']"
        self.finds_elements(account_Number, '24654743254')
        click_On_Payment = "(//*[@id='proceed_payment'])"
        self.finds_elements(click_On_Payment)
        self.page.get_by_text("Proforma Invoice").click()
        purchase_Order = "(//*[@id='eve_210'])"
        self.finds_elements(purchase_Order, '4587698')
        profroma_Invoice_Checkbox = "(//*[@id='performa_check'])"
        self.finds_elements(profroma_Invoice_Checkbox)
        # Place order
        place_Order = "(//*[@id='performa_real'])"
        self.finds_elements(place_Order)
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Email'
        val2 = ''
        eve_id = '211'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_334(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        # Email Id
        email_Address = "#customer-email"
        self.finds_elements(email_Address, 'shubham@raptorsupplies.co.uk')
        # First Name
        first_Name = "//*[@name='firstname']"
        self.finds_elements(first_Name, 'Abc')
        # Last Name
        last_Name = "(//*[@name='lastname'])"
        self.finds_elements(last_Name, 'Kumar')
        # Company Name
        company_Name = "(//*[@name='company'])"
        self.finds_elements(company_Name, 'Raptor')
        # Address
        address = "(//*[@name='street[0]'])"
        self.finds_elements(address, 'UK')
        # City_Name
        city_Name = "(//*[@name='city'])"
        self.finds_elements(city_Name, 'abc')
        # Country dropdown
        country_Dropdown = "(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown, 'India')
        # State dropdown
        state_Or_Province = "(//*[@name='region_id'])"
        self.finds_elements(state_Or_Province, 'Goa')
        # Postal code
        postal_Code = "(//*[@name='postcode'])"
        self.finds_elements(postal_Code, '123456')
        # Contact number
        phone_number = "(//*[@name='telephone'])"
        self.finds_elements(phone_number, '1234567890')
        self.disable_element('#eve_200')
        #Click on edit option for shipping details
        edit_Option = "//*[@class='edit_shipping_info']"
        self.finds_elements(edit_Option)
        #Edit city name
        edit_City = "(//*[@name='city'])"
        self.finds_elements(edit_City)
        self.disable_element('#eve_200')
        expres_mode = "(//*[text()='Express (5 - 7 days)'])"
        self.finds_elements(expres_mode)
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Section Name'
        val2 = ''
        eve_id = '334'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_396(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_Checkout = "//*[text()='Checkout']"
        self.finds_elements(click_On_Checkout)
        # Email Id
        email_Address = "#customer-email"
        self.finds_elements(email_Address, 'shubham@raptorsupplies.co.uk')
        # First Name
        first_Name = "//*[@name='firstname']"
        self.finds_elements(first_Name, 'Abc')
        # Last Name
        last_Name = "(//*[@name='lastname'])"
        self.finds_elements(last_Name, 'Kumar')
        # Company Name
        company_Name = "(//*[@name='company'])"
        self.finds_elements(company_Name, 'Raptor')
        # Address
        address = "(//*[@name='street[0]'])"
        self.finds_elements(address, 'UK')
        # City_Name
        city_Name = "(//*[@name='city'])"
        self.finds_elements(city_Name, 'abc')
        # Country dropdown
        country_Dropdown = "(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown, 'India')
        # State dropdown
        state_Or_Province = "(//*[@name='region_id'])"
        self.finds_elements(state_Or_Province, 'Goa')
        # Postal code
        postal_Code = "(//*[@name='postcode'])"
        self.finds_elements(postal_Code, '123456')
        # Contact number
        phone_number = "(//*[@name='telephone'])"
        self.finds_elements(phone_number, '1234567890')
        uncheck_Billing_Info = "//*[@id='eve_396']"
        self.finds_elements(uncheck_Billing_Info)

        self.print_visitor_id()
        con = "BP"
        val1 = 'Select/ Unselect'
        val2 = ''
        eve_id = '396'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)
    #shopping
    def eve_350(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart = "//*[@id='eve_293']"
        self.finds_elements(click_On_View_Cart)
        print_button = "//*[@id='eve_350']"
        self.finds_elements(print_button)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '350'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_179(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        # self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart = "(//*[@id='eve_293'])"
        self.finds_elements(click_On_View_Cart)
        # close_popup="(//*[@id='Path_5'])"
        # self.finds_elements(close_popup)
        click_On_Product = '//*[@class="product_details_inner"]/a'
        self.finds_elements(click_On_Product)
        self.print_visitor_id()
        con = "BP"
        val1 = 'SKU'
        val2 = 'Title'
        eve_id = '179'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_180(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        # self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart = "(//*[@id='eve_293'])"
        self.finds_elements(click_On_View_Cart)
        # Add_Quantity
        add_Quantity = "(//*[@id='eve_180'])"
        self.finds_elements(add_Quantity)
        self.print_visitor_id()
        con = "BP"
        val1 = '# Quantity Before'
        val2 = '# Quantity After'
        eve_id = '180'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_181(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        # self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart = "(//*[@id='eve_293'])"
        self.finds_elements(click_On_View_Cart)
        # Add_Quantity
        add_Quantity = "(//*[@id='eve_180'])"
        self.finds_elements(add_Quantity)
        # Reduce Quantity
        reduce_Quantity = "(//*[@id='eve_181'])"
        self.finds_elements(reduce_Quantity)
        self.print_visitor_id()
        con = "BP"
        val1 = '# Quantity Before'
        val2 = '# Quantity After'
        eve_id = '181'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_182(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        # self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart = "(//*[@id='eve_293'])"
        self.finds_elements(click_On_View_Cart)
        # Trash Bin
        click_On_Trash_bin = "(//*[@id='eve_182'])"
        self.finds_elements(click_On_Trash_bin)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Title'
        val2 = '# '
        eve_id = '182'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_184(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        # self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart = "(//*[@id='eve_293'])"
        self.finds_elements(click_On_View_Cart)
        # Country Dropdown
        click_On_Country_Dropdown = "(//*[@alt='country-flag'])"
        self.finds_elements(click_On_Country_Dropdown)
        change_country = "(//*[text()='Change Country'])"
        self.finds_elements(change_country)
        country_dropdown = "(//*[@id='top_country_list'])"
        self.finds_elements(country_dropdown, "India")
        self.print_visitor_id()
        con = "BP"
        val1 = 'Current Country'
        val2 = 'Selected Country'
        eve_id = '184'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_185(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        # self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart = "(//*[@id='eve_293'])"
        self.finds_elements(click_On_View_Cart)
        # Shipping Country Details
        country_Shipping = "(//*[@name='country_id'])"
        self.finds_elements(country_Shipping, 'Bangladesh')
        # Mode of Shipping
        try:
            self.driver.find_element(By.XPATH,
                                     '//*[@class="table-checkout-shipping-method shipping_info_label_wrp"]').find_element(
                By.TAG_NAME, 'td').click()
        except Exception as e:
            print(e)

        # ExWorks_Pickup="(//*[@id='s_method_freeshipping_freeshipping'])"
        # self.finds_elements(ExWorks_Pickup)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Mode of Shipment'
        val2 = 'Freight Charge'
        eve_id = '185'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_186(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        # self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart = "(//*[@id='eve_293'])"
        self.finds_elements(click_On_View_Cart)
        # Shipping Country Details
        country_Shipping = "(//*[@name='country_id'])"
        self.finds_elements(country_Shipping, 'Bangladesh')
        # Mode of Shipping
        # select_Express="(//*[@id='s_method_matrixrate_matrixrate_19244'])"
        # self.finds_elements(select_Express)
        # Discount Code
        apply_Discount_Code = "(//*[@id='coupon_code'])"
        self.finds_elements(apply_Discount_Code, 'FAB5')
        click_On_Apply = "(//*[@id='eve_186'])"
        self.finds_elements(click_On_Apply)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Discount code | <Discount Status(Applied/"Please enter valid Coupan>'
        val2 = 'Subtotal with Currecny'
        eve_id = '186'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_187(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        # self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart = "(//*[@id='eve_293'])"
        self.finds_elements(click_On_View_Cart)
        # Shipping Country Details
        # self.finds_elements(apply_Discount_Code,'FAB5')
        # click_On_Apply="(//*[@id='eve_186'])"
        # self.finds_elements( click_On_Apply)
        # Checkout_Button
        click_On_Checkout_Button = "(//*[@id='eve_187'])"
        self.finds_elements(click_On_Checkout_Button)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = 'Subtotal with Currecny'
        eve_id = '187'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_190(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        # self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart = "(//*[@id='eve_293'])"
        self.finds_elements(click_On_View_Cart)
        click_on_TC = '(//*[@id="eve_190"])'
        self.finds_elements(click_on_TC)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Text (Email id)'
        val2 = ''
        eve_id = '190'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_188(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        # self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart = "//*[@id='eve_293']"
        self.finds_elements(click_On_View_Cart)
        enter_email = '//*[@id="eve_188"]'
        self.finds_elements(enter_email, "shubham@raptorsupplies.co.uk")
        self.finds_elements('//*[@id="eve_349"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Text (Email id)'
        val2 = ''
        eve_id = '188'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_352(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        # self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart = "(//*[@id='eve_293'])"
        self.finds_elements(click_On_View_Cart)
        delete_popup = "(//*[@id='eve_182'])"
        self.finds_elements(delete_popup)
        remove = "(//*[@id='eve_352'])"
        self.finds_elements(remove)

        self.print_visitor_id()
        con = "BP"
        val1 = 'SKU | Quantity | item Value'
        val2 = 'Type of Click ("Cancel"/"Remove"/"Cross")'
        eve_id = '352'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_97(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart = "//*[@id='eve_293']"
        self.finds_elements(click_On_View_Cart)
        trust_Pilot = "//*[@id='eve_97']"
        self.finds_elements(trust_Pilot)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '97'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_399(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        # self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart = "(//*[@id='eve_293'])"
        self.finds_elements(click_On_View_Cart)
        save_pdf = "(//*[@id='eve_350'])"
        self.finds_elements(save_pdf)
        pdf = "(//*[@class='print-cart save-as-pdf'])"
        self.finds_elements(pdf)

        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '399'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_400(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        # self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        self.chat_box_close()
        click_On_View_Cart = "(//*[@id='eve_293'])"
        self.finds_elements(click_On_View_Cart)
        # Discount Code
        apply_Discount_Code = "(//*[@id='coupon_code'])"
        self.finds_elements(apply_Discount_Code, 'FAB5')
        click_On_Apply = "(//*[@id='eve_186'])"
        self.finds_elements(click_On_Apply)
        cross = '(//*[@id="Group_5"])'
        self.finds_elements(cross)
        remove_discount = "(//*[@id='eve_400'])"
        self.finds_elements(remove_discount)
        self.print_visitor_id()
        con = "BP"
        val1 = 'Coupon Code'
        val2 = ''
        eve_id = '400'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

def run_program():
    program_dict = {

        # Product 0
        'eve_24': 'eve_24("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_25': 'eve_25("https://www.raptorsupplies.com/pd/dayton/6k844")',
        'eve_26': 'eve_26("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_52': 'eve_52("https://www.raptorsupplies.com/pd/morse-drum/86")',
        'eve_53': 'eve_53("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_54': 'eve_54("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_55': 'eve_55("https://www.raptorsupplies.com/pd/aurand/s2k7")',
        'eve_56': 'eve_56("https://www.raptorsupplies.com/pd/aurand/s2k7")',
        'eve_57': 'eve_57("https://www.raptorsupplies.com/pd/aurand/s2k7")',
        'eve_80': 'eve_80("https://www.raptorsupplies.com/p1/akro-mils/30080-series-shelf-bin")',
        'eve_317': 'eve_317("https://www.raptorsupplies.com/pd/morse-drum/86")',
        'eve_404': 'eve_404("https://www.raptorsupplies.com/pd/morse-drum/92")',
        #End product static 12
        #brand page 12
        'eve_354': 'eve_354("https://www.raptorsupplies.com/b/allegro-safety")',
        'eve_355': 'eve_355("https://www.raptorsupplies.com/b/allegro-safety")',
        'eve_356': 'eve_356("https://www.raptorsupplies.com/b/allegro-safety")',
        #Form Request a Quote 15
        'eve_124': 'eve_124("https://www.raptorsupplies.com/request-for-quote")',
        'eve_125': 'eve_125("https://www.raptorsupplies.com/request-for-quote")',
        'eve_126': 'eve_126("https://www.raptorsupplies.com/request-for-quote")',
        'eve_127': 'eve_127("https://www.raptorsupplies.com/request-for-quote")',
        'eve_128': 'eve_128("https://www.raptorsupplies.com/request-for-quote")',
        # RFQ Pop-up 20
        'eve_40': 'eve_40("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_41': 'eve_41("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_42': 'eve_42("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_43': 'eve_43("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_44': 'eve_44("https://www.raptorsupplies.com/pd/morse-drum/91")',
        # END RFQ 24
        # website 25
        'eve_290': 'eve_290("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        'eve_291': 'eve_291("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        'eve_292': 'eve_292("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        'eve_293': 'eve_293("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        'eve_294': 'eve_294("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        'eve_295': 'eve_295("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        # End Website 30
        # 31
        'eve_272': 'eve_272("https://www.raptorsupplies.com/s?q=1234")',
        'eve_273': 'eve_273("https://www.raptorsupplies.com/s?q=1234")',
        'eve_274': 'eve_274("https://www.raptorsupplies.com/s?q=m1")',
        'eve_275': 'eve_275("https://www.raptorsupplies.com/s?q=m1")',
        'eve_276': 'eve_276("https://www.raptorsupplies.com/s?q=m1")',
        # 36
        'eve_9': 'eve_9("https://www.raptorsupplies.com/")',
        'eve_13': 'eve_13("https://www.raptorsupplies.com/")',
        'eve_16': 'eve_16("https://www.raptorsupplies.com/")',
        'eve_18': 'eve_18("https://www.raptorsupplies.com/")',
        'eve_76': 'eve_76("https://www.raptorsupplies.com/")',
        'eve_89': 'eve_89("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_302': 'eve_302("https://www.raptorsupplies.com/")',
        'eve_304': 'eve_304("https://www.raptorsupplies.com/")',
        'eve_344': 'eve_344("https://www.raptorsupplies.com/check/cart")',
        #44
        #checkout 45
        'eve_192': 'eve_192("https://www.raptorsupplies.com/pd/proto/jsf20m")',
        'eve_193': 'eve_193("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_194': 'eve_194("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_195': 'eve_195("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_196': 'eve_196("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_197': 'eve_197("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_198': 'eve_198("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_199': 'eve_199("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_200': 'eve_200("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_201': 'eve_201("https://www.raptorsupplies.com/pd/morse-drum/86")',
        'eve_203': 'eve_203("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_204': 'eve_204("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_205': 'eve_205("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_206': 'eve_206("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_207': 'eve_207("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_209': 'eve_209("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_210': 'eve_210("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_211': 'eve_211("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_334': 'eve_334("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_396': 'eve_396("https://www.raptorsupplies.com/pd/morse-drum/91")',
        #checkout end 64
        #shopping cart 65
        'eve_97': 'eve_97("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_179': 'eve_179("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_180': 'eve_180("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_181': 'eve_181("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_182': 'eve_182("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_184': 'eve_184("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_185': 'eve_185("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_186': 'eve_186("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_187': 'eve_187("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_350': 'eve_350("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_352': 'eve_352("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_399': 'eve_399("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_400': 'eve_400("https://www.raptorsupplies.com/pd/morse-drum/91")',
    }

    testing = RawEventsTesting()
    keys = list(program_dict.keys())
    start_index = 40
    for i, key in enumerate(keys[start_index:45], start_index):
        print(i, ">>>>>>>>>>> Working Template >>>>>>>>>", key), eval(f"testing.{program_dict[key]}")
        time.sleep(2)
    # for key in keys_to_run:
    #     if key in program_dict:
    #         print(">>>>>>>>>>> Working Template >>>>>>>>>", key)
    #         eval(f"testing.{program_dict[key]}")
    #         time.sleep(2)

    testing.driver_quit()


# keys_to_run = ["eve_284", "eve_21", "eve_158", "eve_159", "eve_160", "eve_162", "eve_249", "eve_344", "eve_267", "eve_338", "eve_99"]
# keys_to_run = ["eve_158"]

run_program()
