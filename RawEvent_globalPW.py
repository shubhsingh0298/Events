import time
import pyautogui
from EventPlaywright import EventAutomation


class RawEventsTesting(EventAutomation):
    def __init__(self):
        super().__init__()

    def eve_22_pd(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_22"]/li[4]/a')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '22'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_22_mother(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_22"]/div/ul/li[3]/a')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '22'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_22_category(self, url):
        self.request_func(url)
        self.reload()
        self.finds_elements('//*[@id="eve_22"]/div/ul/li[3]/a')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '22'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_22_brand(self, url):
        self.request_func(url)
        self.reload()
        self.finds_elements('//*[@id="eve_22"]/li[2]/a')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '22'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_22_brand_l3(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_22"]/div/ul/li[3]/a')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '22'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_22_l1(self, url):
        self.request_func(url)
        self.reload()
        self.finds_elements('//*[@id="eve_22"]/div/ul/li[1]/a')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '22'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_22_l2(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_22"]/div/ul/li[2]/a')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '22'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_22_fastener(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_22"]/div/ul/li[3]/a')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '22'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_265_brand(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_265"]/ul/li[1]/a')
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Name'
        val2 = 'url'
        eve_id = '265'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_265_brand_list(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_265"]/ul/li[1]/a')
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Name'
        val2 = 'url'
        eve_id = '265'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_58_cat(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_58"]')
        self.print_visitor_id()
        con = "BP"
        val1 = 'Name'
        val2 = ''
        eve_id = '58'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_58_more(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="view-btn"]')
        self.print_visitor_id()
        con = "BP"
        val1 = 'Name'
        val2 = ''
        eve_id = '58'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_58_less(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="view-btn"]')
        time.sleep(1)
        self.finds_elements('//*[@id="view-btn"]')
        self.print_visitor_id()
        con = "BP"
        val1 = 'Name'
        val2 = ''
        eve_id = '58'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_28_default(self, url):
        self.request_func(url)
        brand_name = '//*[@id="eve_28"]'  #28
        self.finds_elements(brand_name)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '28'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_28_include(self, url):
        self.request_func(url)
        brand_name = '//*[@id="eve_28"]'  #28
        self.finds_elements(brand_name)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '28'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_28_p1(self, url):
        self.request_func(url)
        brand_name = '//*[@id="eve_28"]'  #28
        self.finds_elements(brand_name)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '28'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_29_default(self, url):
        self.request_func(url)
        self.trust_pilot_click('//*[@id="eve_29"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '29'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_29_include(self, url):
        self.request_func(url)
        self.trust_pilot_click('//*[@id="eve_29"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '29'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_29_p1(self, url):
        self.request_func(url)
        self.trust_pilot_click('//*[@id="eve_29"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '29'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_32_default(self, url):
        self.request_func(url)
        small_image = '//*[@id="eve_32"]/div/a[2]'  #32  //*[@id="eve_32"]/div/a[2]/img
        self.finds_elements(small_image)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '32'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_32_include(self, url):
        self.request_func(url)
        small_image = '//*[@id="eve_32"]/div/a'  #32  //*[@id="eve_32"]/div/a[2]/img
        self.finds_elements(small_image)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '32'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_32_p1(self, url):
        self.request_func(url)
        small_image = '//*[@id="eve_32"]/div/a'  #32  //*[@id="eve_32"]/div/a[2]/img
        self.finds_elements(small_image)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '32'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_33_default(self, url):

        self.request_func(url)
        time.sleep(2)
        self.finds_elements('//*[@class="share-icon"]')
        print("yesss")
        self.finds_elements('//*[@id="eve_33"]')  #33
        pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '33'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_33_include(self, url):
        self.request_func(url)
        time.sleep(2)
        self.finds_elements('//*[@class="share-icon"]')
        print("yesss")
        self.finds_elements('//*[@id="eve_33"]')  #33
        pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '33'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_33_p1(self, url):
        self.request_func(url)
        time.sleep(2)
        self.finds_elements('//*[@class="share-icon"]')
        print("yesss")
        self.finds_elements('//*[@id="eve_33"]')  #33
        pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '33'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_34_default(self, url):
        self.request_func(url)
        # time.sleep(2)
        share_icon = '//*[@class="share-icon"]'
        self.finds_elements(share_icon)
        share_whatsapp = '//*[@id="eve_34"]'  #34
        self.finds_elements(share_whatsapp)
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '34'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_34_include(self, url):
        self.request_func(url)
        # time.sleep(2)
        share_icon = '//*[@class="share-icon"]'
        self.finds_elements(share_icon)
        share_whatsapp = '//*[@id="eve_34"]'  #34
        self.finds_elements(share_whatsapp)
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '34'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_34_p1(self, url):
        self.request_func(url)
        # time.sleep(2)
        share_icon = '//*[@class="share-icon"]'
        self.finds_elements(share_icon)
        share_whatsapp = '//*[@id="eve_34"]'  #34
        self.finds_elements(share_whatsapp)
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '34'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_35_default(self, url):
        self.request_func(url)
        # time.sleep(2)
        share_icon = '//*[@class="share-icon"]'
        self.finds_elements(share_icon)
        share_button_copy = '//*[@id="eve_35"]'  #35
        self.finds_elements(share_button_copy)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '35'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_35_include(self, url):
        self.request_func(url)
        # time.sleep(2)
        share_icon = '//*[@class="share-icon"]'
        self.finds_elements(share_icon)
        share_button_copy = '//*[@id="eve_35"]'  #35
        self.finds_elements(share_button_copy)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '35'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_35_p1(self, url):
        self.request_func(url)
        # time.sleep(2)
        share_icon = '//*[@class="share-icon"]'
        self.finds_elements(share_icon)
        share_button_copy = '//*[@id="eve_35"]'  #35
        self.finds_elements(share_button_copy)
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '35'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_101_default(self, url):
        self.request_func(url)
        check_availability = '//*[@id="eve_101"]'  #101
        self.finds_elements(check_availability)
        self.chat_box_close()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '101'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_101_include(self, url):
        self.request_func(url)
        check_availability = '//*[@id="eve_101"]'  #101
        self.finds_elements(check_availability)
        self.chat_box_close()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '101'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_38_default(self, url):
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
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_38_include(self, url):
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
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_38_p1(self, url):
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
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_39_default(self, url):
        self.request_func(url)
        rfq = "//*[@id='main_rfq_btn']"
        self.element_hover(rfq)
        self.finds_elements(rfq)
        self.print_visitor_id()
        con = "BP"
        val1 = '# Quantity'
        val2 = ''
        eve_id = '39'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_39_include(self, url):
        self.request_func(url)
        rfq = "//*[@id='main_rfq_btn']"
        self.element_hover(rfq)
        self.finds_elements(rfq)
        self.print_visitor_id()
        con = "BP"
        val1 = '# Quantity'
        val2 = ''
        eve_id = '39'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_39_p1(self, url):
        self.request_func(url)
        rfq = "//*[@id='eve_39']"
        self.element_hover(rfq)
        self.finds_elements(rfq)
        self.print_visitor_id()
        con = "BP"
        val1 = '# Quantity'
        val2 = ''
        eve_id = '39'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_51_default(self, url):
        self.request_func(url)
        content_menu = '//*[@id="eve_51"]/li[2]/a'
        self.finds_elements(content_menu)
        self.print_visitor_id()

        con = "BP"
        val1 = '# field'
        val2 = ''
        eve_id = '51'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_51_include(self, url):
        self.request_func(url)
        content_menu = '//*[@id="eve_51"]/li[2]/a'
        self.finds_elements(content_menu)
        self.print_visitor_id()

        con = "BP"
        val1 = '# field'
        val2 = ''
        eve_id = '51'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_51_p1(self, url):
        self.request_func(url)
        content_menu = '//*[@id="tabs"]/li[2]'
        self.finds_elements(content_menu)
        self.print_visitor_id()

        con = "BP"
        val1 = '# field'
        val2 = ''
        eve_id = '51'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_93_home(self, url):
        self.request_func(url)
        explore_more = '//*[@id="eve_93"]/div/ul/li[7]/a'
        self.finds_elements(explore_more)
        self.print_visitor_id()
        con = "BPN"
        val1 = 'name'
        val2 = ''
        eve_id = '93'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_93_l2(self, url):
        self.request_func(url)
        explore_more = '//*[@id="eve_93"]/div/ul/li[7]/a'
        self.finds_elements(explore_more)
        self.print_visitor_id()
        con = "BPN"
        val1 = 'name'
        val2 = ''
        eve_id = '93'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_93_l3(self, url):
        self.request_func(url)
        explore_more = '//*[@id="eve_93"]/div/ul/li[1]/a'
        self.finds_elements(explore_more)
        self.print_visitor_id()
        con = "BPN"
        val1 = 'name'
        val2 = ''
        eve_id = '93'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_93_p(self, url):
        self.request_func(url)
        explore_more = '//*[@id="eve_93"]/div[2]/ul/li[2]/a'
        self.finds_elements(explore_more)
        self.print_visitor_id()
        con = "BPN"
        val1 = 'name'
        val2 = ''
        eve_id = '93'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_93_pd(self, url):
        self.request_func(url)
        explore_more = '//*[@id="eve_93"]/div[2]/ul/li[2]/a'
        self.finds_elements(explore_more)
        self.print_visitor_id()
        con = "BPN"
        val1 = 'name'
        val2 = ''
        eve_id = '93'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_93_b(self, url):
        self.request_func(url)
        explore_more = '//*[@id="eve_93"]/div/ul/li[6]/a'
        self.finds_elements(explore_more)
        self.print_visitor_id()
        con = "BPN"
        val1 = 'name'
        val2 = ''
        eve_id = '93'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_93_bfc(self, url):
        self.request_func(url)
        explore_more = '//*[@id="eve_93"]/div/ul/li[6]/a'
        self.finds_elements(explore_more)
        self.print_visitor_id()
        con = "BPN"
        val1 = 'name'
        val2 = ''
        eve_id = '93'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_307_grainer(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_307"]'
        self.finds_elements(comment, 'Shubham')
        self.finds_elements('//*[@id="mcmaster_enquiry_button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '307'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_307_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_307"]'
        self.finds_elements(comment, 'Shubham')
        self.finds_elements('//*[@id="mcmaster_enquiry_button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '307'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_307_zeus(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_307"]'
        self.finds_elements(comment, 'Shubham')
        self.finds_elements('//*[@id="mcmaster_enquiry_button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '307'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_308_grainer(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_308"]'
        self.finds_elements(comment, 'shubham@raptorsupplies.co.uk')
        self.finds_elements('//*[@id="mcmaster_enquiry_button"]')
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '308'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_308_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_308"]'
        self.finds_elements(comment, 'shubham@raptorsupplies.co.uk')
        self.finds_elements('//*[@id="mcmaster_enquiry_button"]')
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '308'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_308_zeus(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_308"]'
        self.finds_elements(comment, 'shubham@raptorsupplies.co.uk')
        self.finds_elements('//*[@id="mcmaster_enquiry_button"]')
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = ''
        eve_id = '308'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_309_grainer(self, url):
        self.request_func(url)
        pn = '//*[@id="eve_309"]'
        self.finds_elements(pn, '8294966962')
        self.finds_elements('//*[@id="mcmaster_enquiry_button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# num'
        val2 = ''
        eve_id = '309'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_309_mro(self, url):
        self.request_func(url)
        pn = '//*[@id="eve_309"]'
        self.finds_elements(pn, '8294966962')
        self.finds_elements('//*[@id="mcmaster_enquiry_button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# num'
        val2 = ''
        eve_id = '309'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_309_zeus(self, url):
        self.request_func(url)
        pn = '//*[@id="eve_309"]'
        self.finds_elements(pn, '8294966962')
        self.finds_elements('//*[@id="mcmaster_enquiry_button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# num'
        val2 = ''
        eve_id = '309'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_310_grainer(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_310"]'
        self.finds_elements(comment, '99')
        self.finds_elements('//*[@id="mcmaster_enquiry_button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '310'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_310_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_310"]'
        self.finds_elements(comment, '99')
        self.finds_elements('//*[@id="mcmaster_enquiry_button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '310'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_310_zeus(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_310"]'
        self.finds_elements(comment, '99')
        self.finds_elements('//*[@id="mcmaster_enquiry_button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '310'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_311_grainer(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_311"]'
        self.finds_elements(comment, '9')
        self.finds_elements('//*[@id="mcmaster_enquiry_button"]')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = ""
        val1 = ''
        val2 = ''
        eve_id = '311'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_311_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_311"]'
        self.finds_elements(comment, '9')
        self.finds_elements('//*[@id="mcmaster_enquiry_button"]')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = ""
        val1 = ''
        val2 = ''
        eve_id = '311'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_311_zeus(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_311"]'
        self.finds_elements(comment, '9')
        self.finds_elements('//*[@id="mcmaster_enquiry_button"]')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = ""
        val1 = ''
        val2 = ''
        eve_id = '311'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_92_blog(self, url):
        self.request_func(url)
        blog_view_all = "//*[@id='eve_92']"
        self.finds_elements(blog_view_all)
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'url'
        val2 = ''
        eve_id = '92'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_345_b(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="all-product"]/div[2]/a[1]')
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#page'
        val2 = ''
        eve_id = '345'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_345_l3(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="loadPage"]/a[1]')
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#page'
        val2 = ''
        eve_id = '345'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_345_bfc(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="loadPage"]/a[1]')
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#page'
        val2 = ''
        eve_id = '345'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_72_fastener_listview(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="listViewSwitch"]')
        self.finds_elements('//*[@class="buttonBox add_cart hz_moth_Fastener_click"]')
        # self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#mothertitle'
        val2 = 'viewtitle'
        eve_id = '72'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_72_fastener_gridview(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="gridViewSwitch"]')
        self.finds_elements('//*[@class="buttonBox add_cart"]')
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#mothertitle'
        val2 = 'viewtitle'
        eve_id = '72'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_72_fastener_defaultview(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_72"]')
        # self.finds_elements('/html/body/div[4]/div/div[2]/div/div[5]/div[2]/div[3]/div/div[3]')
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#mothertitle'
        val2 = ''
        eve_id = '72'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_72_nonfastener_listtview(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="listViewSwitch"]')
        # self.finds_elements('//*[@id="add_cart list_view"]')
        self.finds_elements('//*[@id="defaultView"]/div/div[1]/div/div[6]')
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#mothertitle'
        val2 = 'viewtitle'
        eve_id = '72'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_72_nonfastener_gridview(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="gridViewSwitch"]')
        self.finds_elements('//*[@id="defaultView"]/div/div[1]/div/div[5]')
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#mothertitle'
        val2 = 'viewtitle'
        eve_id = '72'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_72_nonfastener_defaultview(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="defaultViewSwitch"]')
        self.finds_elements('//*[@id="defaultView"]/section[1]/h2/a')
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#mothertitle'
        val2 = 'viewtitle'
        eve_id = '72'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_103_nonfastener_defaultview(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="defaultViewSwitch"]')
        self.finds_elements('//*[@class="add_cart caterfq"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#Product Title '
        val2 = 'View name'
        eve_id = '103'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_103_nonfastener_gridview(self, url):
        self.request_func(url)
        self.page.locator("#gridViewSwitch").click()
        element_xpath = '//*[@id="defaultView"]/div/div[5]/div/div[6]/div'
        self.page.wait_for_selector(element_xpath)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Product Title '
        val2 = 'View name'
        eve_id = '103'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_103_nonfastener_gridview(self, url):
        self.request_func(url)
        self.page.locator("#gridViewSwitch").click()
        self.finds_elements('//*[@class="add_cart caterfq"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#Product Title '
        val2 = 'View name'
        eve_id = '103'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_103_nonfastener_listtview(self, url):
        self.request_func(url)
        self.page.wait_for_selector("#listViewSwitch").click()
        self.finds_elements('//*[@id="defaultView"]/div/div[2]/div/div[6]')
        # self.finds_elements('//*[@id="parent_"]/table/tbody/tr[1]/td[4]/div/span')
        self.print_visitor_id()
        con = "BP"
        val1 = '#Product Title '
        val2 = 'View name'
        eve_id = '103'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_103_fastener_defaultview(self, url):
        self.request_func(url)
        self.chat_box_close()
        self.finds_elements("//span[@class='na' and @align='center']")
        self.finds_elements("//*[@id='eve_103']")
        self.print_visitor_id()
        con = "BP"
        val1 = '#Product Title '
        val2 = 'View name'
        eve_id = '103'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_148_home_git(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_148"]'
        self.finds_elements(comment, 'Shubham')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '148'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_148_git(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_148"]'
        self.finds_elements(comment, 'Shubham')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '148'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_148_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_148"]'
        self.finds_elements(comment, 'Shubham')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '148'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_148_bfc_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_148"]'
        self.finds_elements(comment, 'Shubham')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '148'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_148_motherlist_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_148"]'
        self.finds_elements(comment, 'Shubham')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '148'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_148_l3_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_148"]'
        self.finds_elements(comment, 'Shubham')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '148'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_149_home_git(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_149"]'
        self.finds_elements(comment, 'shubham@raptorsupplies.co.uk')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '149'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_149_git(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_149"]'
        self.finds_elements(comment, 'shubham@raptorsupplies.co.uk')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '149'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_149_l3_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_149"]'
        self.finds_elements(comment, 'shubham@raptorsupplies.co.uk')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '149'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_149_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_149"]'
        self.finds_elements(comment, 'shubham@raptorsupplies.co.uk')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '149'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_149_bfc_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_149"]'
        self.finds_elements(comment, 'shubham@raptorsupplies.co.uk')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '149'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_149_motherlist_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_149"]'
        self.finds_elements(comment, 'shubham@raptorsupplies.co.uk')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '149'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_150_home_git(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_150"]'
        self.finds_elements(comment, '999999999')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '150'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_150_git(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_150"]'
        self.finds_elements(comment, '999999999')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '150'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_150_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_150"]'
        self.finds_elements(comment, '999999999')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '150'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_150_bfc_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_150"]'
        self.finds_elements(comment, '999999999')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '150'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_150_motherlist_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_150"]'
        self.finds_elements(comment, '999999999')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '150'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_150_l3_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_149"]'
        self.finds_elements(comment, 'shubham@raptorsupplies.co.uk')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '149'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_151_home_git(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_151"]'
        self.finds_elements(comment, 'testing')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '151'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_151_git(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_151"]'
        self.finds_elements(comment, 'testing')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '151'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_151_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_151"]'
        self.finds_elements(comment, 'testing')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '151'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_151_bfc_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_151"]'
        self.finds_elements(comment, 'testing')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '151'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_151_motherlist_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_151"]'
        self.finds_elements(comment, 'testing')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '151'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_151_l3_mro(self, url):
        self.request_func(url)
        comment = '//*[@id="eve_149"]'
        self.finds_elements(comment, 'shubham@raptorsupplies.co.uk')
        self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '# text'
        val2 = ''
        eve_id = '149'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_109_nonfastener_listtview(self, url):
        self.request_func(url)
        comment = '//*[@id="listViewSwitch"]'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="row0_0"]/td[2]')
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Product Title'
        val2 = 'View name '
        eve_id = '109'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_109_nonfastener_gridview(self, url):
        self.request_func(url)
        comment = '//*[@id="gridViewSwitch"]'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="defaultView"]/div/div[2]/div/div[2]/h3/a')

        self.print_visitor_id()
        con = "BPN"
        val1 = '#Product Title'
        val2 = 'View name '
        eve_id = '109'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_109_nonfastener_defaultview(self, url):
        self.request_func(url)
        comment = '//*[@id="row0_0"]/td[4]'
        # self.finds_elements(comment)
        self.finds_elements(comment)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Product Title'
        val2 = 'View name '
        eve_id = '109'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_109_fastener_listtview(self, url):
        self.request_func(url)
        comment = '//*[@id="listViewSwitch"]'
        self.finds_elements(comment)
        self.finds_elements('//*[@class="category-card-col"][3]/div/div/img')

        self.print_visitor_id()
        con = "BPN"
        val1 = '#Product Title'
        val2 = 'View name '
        eve_id = '109'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_109_fastener_gridview(self, url):
        self.request_func(url)
        comment = '//*[@id="gridViewSwitch"]'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="eve_109"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Product Title'
        val2 = 'View name '
        eve_id = '109'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_109_fastener_defaultview(self, url):
        self.request_func(url)
        comment = '//*[@id="defaultViewSwitch"]/span/i'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="row1_0"]/td[2]')
        self.finds_elements(' //*[@id="prodetail_71661"]/td/div/div[2]/div/div[1]/a/p')

        self.print_visitor_id()
        con = "BPN"
        val1 = '#Product Title'
        val2 = 'View name '
        eve_id = '109'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_110_fastener_defaultview(self, url):
        self.request_func(url)
        comment = '//*[@id="defaultViewSwitch"]/span/i'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="row1_0"]/td[3]')
        self.finds_elements('//*[@id="eve_110"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#Product Title/Model Number'
        val2 = 'Viewname'
        eve_id = '110'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_110_fastener_listtview(self, url):
        self.request_func(url)
        comment = '//*[@id="listViewSwitch"]/span/i'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="atc_2"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#Product Title/Model Number'
        val2 = 'Viewname'
        eve_id = '110'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_110_fastener_gridtview(self, url):
        self.request_func(url)
        comment = '//*[@id="gridViewSwitch"]/span/i'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="atc_1"]/button')
        self.print_visitor_id()
        con = "BP"
        val1 = '#Product Title/Model Number'
        val2 = 'Viewname'
        eve_id = '110'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_110_nonfastener_defaultview(self, url):
        self.request_func(url)
        # comment = '//*[@id="defaultViewSwitch"]'
        # self.finds_elements(comment)
        self.finds_elements('//*[@id="atc_2"]/span')
        self.print_visitor_id()
        con = "BP"
        val1 = '#Product Title/Model Number'
        val2 = 'Viewname'
        eve_id = '110'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_110_nonfastener_gridview(self, url):
        self.request_func(url)
        comment = '//*[@id="gridViewSwitch"]'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="atc_1"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#Product Title/Model Number'
        val2 = 'Viewname'
        eve_id = '110'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_110_nonfastener_listtview(self, url):
        self.request_func(url)
        comment = '//*[@id="listViewSwitch"]'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="atc_0"]')
        # self.finds_elements('//*[@id="parent_"]/table/tbody/tr[1]/td[6]/div/span')

        self.print_visitor_id()
        con = "BP"
        val1 = '#Product Title/Model Number'
        val2 = 'Viewname'
        eve_id = '110'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_111_fastener_listtview(self, url):
        self.request_func(url)
        comment = '//*[@id="listViewSwitch"]/span/i'
        self.finds_elements(comment)
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#previouse view'
        val2 = '#nextview'
        eve_id = '111'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_111_fastener_gridtview(self, url):
        self.request_func(url)
        comment = '//*[@id="gridViewSwitch"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#previouse view'
        val2 = '#nextview'
        eve_id = '111'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_111_fastener_defaultview(self, url):
        self.request_func(url)
        comment = '//*[@id="defaultViewSwitch"]/span/i'
        self.finds_elements(comment)
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#previouse view'
        val2 = '#nextview'
        eve_id = '111'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_111_nonfastener_listtview(self, url):
        self.request_func(url)
        comment = '//*[@id="listViewSwitch"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#previouse view'
        val2 = '#nextview'
        eve_id = '111'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_111_nonfastener_gridview(self, url):
        self.request_func(url)
        comment = '//*[@id="gridViewSwitch"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#previouse view'
        val2 = '#nextview'
        eve_id = '111'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_111_nonfastener_defaultview(self, url):
        self.request_func(url)
        comment = '//*[@id="defaultViewSwitch"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@class="submit-button"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#previouse view'
        val2 = '#nextview'
        eve_id = '111'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_65_fastener_L4(self, url):
        self.request_func(url)
        comment = '//*[@id="1159"]/span'
        self.finds_elements(comment)
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Filter name'
        val2 = '#value1 | #value2 | #value3'
        eve_id = '65'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_65_fastener_L5(self, url):
        self.request_func(url)
        comment = '//*[@id="1085"]/span'
        self.finds_elements(comment)
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Filter name'
        val2 = '#value1 | #value2 | #value3'
        eve_id = '65'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_65_L2(self, url):
        self.request_func(url)
        comment = '//*[@id="brandFilter"]/div/label[1]/span'
        self.finds_elements(comment)
        #self.back()
        self.print_visitor_id()
        con = "BP"
        val1 = '#Filter name'
        val2 = '#value1 | #value2 | #value3'
        eve_id = '65'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_65_L3(self, url):
        self.request_func(url)
        comment = '//*[@id="655840"]/span'
        self.finds_elements(comment)
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Filter name'
        val2 = '#value1 | #value2 | #value3'
        eve_id = '65'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_65_mother(self, url):
        self.request_func(url)
        comment = '//*[@id="512649"]'
        self.finds_elements(comment)
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Filter name'
        val2 = '#value1 | #value2 | #value3'
        eve_id = '65'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_65_fastener_search(self, url):
        self.request_func(url)
        comment = '//*[@id="Item"]/label[1]/span'
        self.finds_elements(comment)
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Filter name'
        val2 = '#value1 | #value2 | #value3'
        eve_id = '65'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_66_fastener_L4(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="a_30157"]'
        self.finds_elements(comment, 'vestil')
        pyautogui.press('enter')
        # self.finds_elements('//*[@id="eve_284"]')
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Filter name'

        val2 = 'position'
        eve_id = '66'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_66_fastener_L5(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="a_25668"]'
        self.finds_elements(comment, 'vestil')
        pyautogui.press('enter')
        # self.finds_elements('//*[@id="eve_284"]')
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Filter name'

        val2 = 'position'
        eve_id = '66'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_66_L3(self, url):
        self.request_func(url)
        self.page.get_by_role("heading", name="Item").get_by_role("button").click()
        time.sleep(1)
        self.page.locator("#a_31154").fill("Adaptor")
        self.page.locator("#a_31154").click()
        self.page.locator("[id=\"\\34 90494\"] span").click()
        self.print_visitor_id()
        con = "BP"
        val1 = '#Filter name'

        val2 = 'position'
        eve_id = '66'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_66_L2(self, url):
        self.request_func(url)
        self.page.get_by_role("heading", name="Brand").get_by_role("button").click()
        self.page.locator("#a_brand").click()
        self.page.locator("#a_brand").fill("AMS")
        pyautogui.press('enter')
        # self.finds_elements('//*[@id="eve_284"]')
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Filter name'

        val2 = 'position'
        eve_id = '66'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_66_mother(self, url):
        self.request_func(url)

        self.page.get_by_role("heading", name="HP").get_by_role("button").click()
        self.page.locator("#a_25030").fill("1")
        self.page.locator("[id=\"\\31 84269\"]").nth(2).click()
        self.print_visitor_id()
        con = "BP"
        val1 = '#Filter name'

        val2 = 'position'
        eve_id = '66'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_67_fastener_L4(self, url):
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
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_67_fastener_L5(self, url):
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
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_67_L2(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="brandFilter"]/div/label[1]/span'
        self.finds_elements(comment)
        self.finds_elements('//*[@id="abc"]')
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Filter name'
        val2 = '#filtervale'
        eve_id = '67'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_67_L3(self, url):
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
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_67_mother(self, url):
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
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_67_fastener_search(self, url):
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
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_68_fastener_L4(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="a_49"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@id="eve_284"]')f
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Filter name'
        val2 = 'filter value'
        eve_id = '68'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_68_fastener_L5(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="a_46356"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@id="eve_284"]')f
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Filter name'
        val2 = 'filter value'
        eve_id = '68'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_68_L2(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="a_469661"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@id="eve_284"]')f
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Filter name'
        val2 = 'filter value'
        eve_id = '68'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_68_L3(self, url):
        self.request_func(url)
        # self.chat_box_close()
        comment = '//*[@id="eve_68"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@id="eve_284"]')f
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Filter name'
        val2 = 'filter value'
        eve_id = '68'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_68_mother(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="a_230093"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@id="eve_284"]')f
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BP"
        val1 = '#Filter name'
        val2 = 'filter value'
        eve_id = '68'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_68_search(self, url):
        self.request_func(url)
        self.chat_box_close()
        comment = '//*[@id="eve_68"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@id="eve_284"]')f
        # self.finds_elements(comment)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#Filter name'
        val2 = 'filter value'
        eve_id = '68'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_113_nonfasteners(self, url):
        self.request_func(url)

        self.finds_elements('//*[@id="parent_"]/table/tbody/tr[1]')
        self.print_visitor_id()
        con = "BPN"
        val1 = '#text'
        val2 = '#text'
        eve_id = '113'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_113_fasteners_grid(self, url):
        self.request_func(url)

        self.finds_elements('//*[@id="gridViewSwitch"]')
        time.sleep(2)
        self.finds_elements('//*[@class="product-desc-wrap"]/div/h3/a')
        # self.finds_elements('//*[@id="gridViewSwitch"]')
        self.print_visitor_id()
        con = "BPN"
        val1 = '#text'
        val2 = '#text'
        eve_id = '113'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_113_fasteners_default(self, url):
        self.request_func(url)

        self.finds_elements('//*[@id="row1"]/td[2]/span')
        self.finds_elements('//*[@id="prodetail_4813223"]/td/div/div[2]/div/div[1]/h4/a')

        self.print_visitor_id()
        con = "BP"
        val1 = '#text'
        val2 = '#text'
        eve_id = '113'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_114_nonfasteners(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="parent_"]/table/tbody/tr[1]/td[12]/div/span')
        self.print_visitor_id()
        con = "BP"
        val1 = '#quantity | Title'
        val2 = 'View name'
        eve_id = '114'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_114_fasteners_grid(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="gridViewSwitch"]/i')
        self.finds_elements('//*[@id="voltagepop_71660"]/button')
        self.print_visitor_id()
        con = "BP"
        val1 = '#quantity | Title'
        val2 = 'View name'
        eve_id = '114'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_114_fasteners_default(self, url):
        self.request_func(url)
        # self.finds_elements('//*[@id="defaultViewSwitch"]')
        self.finds_elements('//*[@id="row1"]/td[3]')
        self.finds_elements('//*[@id="voltagepop_554666"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#quantity | Title'
        val2 = 'View name'
        eve_id = '114'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_115_nonfasteners(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="5268652"]')

        self.print_visitor_id()
        con = "BP"
        val1 = '#title'
        val2 = ''
        eve_id = '115'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_115_fasteners_grid(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="gridViewSwitch"]')
        self.finds_elements('//*[@id="4553147"]')
        # self.finds_elements('//*[@id="4553147"]')

        self.print_visitor_id()
        con = "BP"
        val1 = '#title'
        val2 = '#viewname'
        eve_id = '115'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_115_fasteners_default(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="row1"]/td[3]/span')
        self.finds_elements('//*[@id="4553118"]')

        self.print_visitor_id()
        con = "BP"
        val1 = '#title'
        val2 = '#viewname'
        eve_id = '115'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_347_fasteners_grid(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="gridViewSwitch"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#privous view'
        val2 = 'Next veiw'
        eve_id = '347'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_347_fasteners_default(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="defaultViewSwitch"]')
        self.print_visitor_id()
        con = "BP"
        val1 = '#privous view'
        val2 = 'Next veiw'
        eve_id = '347'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_299_home(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_299']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '299'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_299_l2(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_299']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '299'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_299_brand(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_299']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '299'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_299_mother(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_299']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '299'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_299_grainger(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_299']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '299'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_299_l3(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_299']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '299'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_299_desktop(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_299']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '299'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_299_mobile(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='eve_299']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '299'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_299_myaccount(self, url):
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
        self.finds_elements("//*[@id='eve_299']")
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '299'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_300_home(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_299']")
        self.finds_elements("//*[@id='eve_300']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#cat name'
        val2 = ''
        eve_id = '300'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_300_l2(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_299']")
        self.finds_elements("//*[@id='eve_300']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#cat name'
        val2 = ''
        eve_id = '300'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_300_brand(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_299']")
        self.finds_elements("//*[@id='eve_300']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#cat name'
        val2 = ''
        eve_id = '300'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_300_mother(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_299']")
        self.finds_elements("//*[@id='eve_300']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#cat name'
        val2 = ''
        eve_id = '300'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_300_grainger(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_299']")
        self.finds_elements("//*[@id='eve_300']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#cat name'
        val2 = ''
        eve_id = '300'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_300_l3(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_299']")
        self.finds_elements("//*[@id='eve_300']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#cat name'
        val2 = ''
        eve_id = '300'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_300_desktop(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_299']")
        self.finds_elements("//*[@id='eve_300']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#cat name'
        val2 = ''
        eve_id = '300'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_300_mobile(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_299']")
        self.finds_elements("//*[@id='eve_300']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#cat name'
        val2 = ''
        eve_id = '300'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_300_myaccount(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_13"]')
        print('sign in')
        self.finds_elements('//*[@id="email"]', 'mailto:devanshu@nextgenesolutions.com')
        print('username')
        self.finds_elements('//*[@id="pass"]', 'Devanshu@123')
        print('password')
        self.chat_box_close()
        self.finds_elements('//*[@id="send2"]')
        print('login')
        self.element_hover("//*[@id='eve_299']")
        self.finds_elements("//*[@id='eve_300']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#cat name'
        val2 = ''
        eve_id = '300'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_303_home(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_302']")
        self.finds_elements("//*[@id='eve_303']/div/a")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#brand name'
        val2 = ''
        eve_id = '303'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_303_l2(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_302']")
        self.finds_elements("//*[@id='eve_303']/div/a")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#brand name'
        val2 = ''
        eve_id = '303'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_303_brand(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_302']")
        self.finds_elements("//*[@id='eve_303']/div/a")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#brand name'
        val2 = ''
        eve_id = '303'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_303_mother(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_302']")
        self.finds_elements("//*[@id='eve_303']/div/a")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#brand name'
        val2 = ''
        eve_id = '303'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_303_grainger(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_302']")
        self.finds_elements("//*[@id='eve_303']/div/a")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#brand name'
        val2 = ''
        eve_id = '303'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_303_l3(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_302']")
        self.finds_elements("//*[@id='eve_303']/div/a")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#brand name'
        val2 = ''
        eve_id = '303'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_303_desktop(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_302']")
        self.finds_elements("//*[@id='eve_303']/div/a")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#brand name'
        val2 = ''
        eve_id = '303'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_303_mobile(self, url):
        self.request_func(url)
        self.element_hover("//*[@id='eve_302']")
        self.finds_elements("//*[@id='eve_303']/div/a")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#brand name'
        val2 = ''
        eve_id = '303'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_303_myaccount(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_13"]')
        print('sign in')
        self.finds_elements('//*[@id="email"]', 'mailto:devanshu@nextgenesolutions.com')
        print('username')
        self.finds_elements('//*[@id="pass"]', 'Devanshu@123')
        print('password')
        self.chat_box_close()
        self.finds_elements('//*[@id="send2"]')
        print('login')
        self.element_hover("//*[@id='eve_302']")
        self.finds_elements("//*[@id='eve_303']/div/a")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#brand name'
        val2 = ''
        eve_id = '303'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_306_home(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@class='country-change']")
        self.finds_elements("//*[@id='top_country_list']", 'Thailand')
        self.finds_elements("//*[@class='currency_update']")
        time.sleep(4)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@id='eve_306']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#lang name'
        val2 = 'url'
        eve_id = '306'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_306_l2(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@class='lang country-change']")
        self.finds_elements("//*[@id='top_country_list']", 'Thailand')
        self.finds_elements("//*[@class='currency_update']")
        time.sleep(4)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@id='eve_306']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#lang name'
        val2 = 'url'
        eve_id = '306'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_306_brand(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@class='lang country-change']")
        self.finds_elements("//*[@id='top_country_list']", 'Thailand')
        self.finds_elements("//*[@class='currency_update']")
        time.sleep(4)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@id='eve_306']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#lang name'
        val2 = 'url'
        eve_id = '306'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_306_mother(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@class='lang country-change']")
        self.finds_elements("//*[@id='top_country_list']", 'Thailand')
        self.finds_elements("//*[@class='currency_update']")
        time.sleep(4)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@id='eve_306']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#lang name'
        val2 = 'url'
        eve_id = '306'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_306_grainger(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@class='lang country-change']")
        self.finds_elements("//*[@id='top_country_list']", 'Thailand')
        self.finds_elements("//*[@class='currency_update']")
        time.sleep(4)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@id='eve_306']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#lang name'
        val2 = 'url'
        eve_id = '306'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_306_l3(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@class='lang country-change']")
        self.finds_elements("//*[@id='top_country_list']", 'Thailand')
        self.finds_elements("//*[@class='currency_update']")
        time.sleep(4)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@id='eve_306']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#lang name'
        val2 = 'url'
        eve_id = '306'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_306_desktop(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@class='lang country-change']")
        self.finds_elements("//*[@id='top_country_list']", 'Thailand')
        self.finds_elements("//*[@class='currency_update']")
        time.sleep(4)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@id='eve_306']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#lang name'
        val2 = 'url'
        eve_id = '306'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_306_mobile(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@class='country-change']")
        self.finds_elements("//*[@id='top_country_list']", 'Thailand')
        self.finds_elements("//*[@class='currency_update']")
        time.sleep(4)
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@id='eve_306']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#lang name'
        val2 = 'url'
        eve_id = '306'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_306_myaccount(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_13"]')
        print('sign in')
        self.finds_elements('//*[@id="email"]', 'mailto:devanshu@nextgenesolutions.com')
        print('username')
        self.finds_elements('//*[@id="pass"]', 'Devanshu@123')
        print('password')
        self.chat_box_close()
        self.finds_elements('//*[@id="send2"]')
        print('login')
        self.element_hover("//*[@class='flag']")
        self.finds_elements("//*[@id='eve_306']")
        self.print_visitor_id()
        con = "BPN"
        val1 = '#lang name'
        val2 = 'url'
        eve_id = '306'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_home(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_l2(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_brand(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_mother(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_grainger(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_l3(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_desktop(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_mobile(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_myaccount(self, url):
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
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_home(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_l2(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_brand(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_mother(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_grainger(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_l3(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_desktop(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_mobile(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_myaccount(self, url):
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
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_360_product(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/div[2]')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'val1'
        val2 = 'val2'
        eve_id = '360'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_360_category(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/div[2]')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'val1'
        val2 = 'val2'
        eve_id = '360'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_360_brand(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/div[2]')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'val1'
        val2 = 'val2'
        eve_id = '360'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_360_l1(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/div[2]')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'val1'
        val2 = 'val2'
        eve_id = '360'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_360_l2(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/div[2]')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'val1'
        val2 = 'val2'
        eve_id = '360'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_360_bfc(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/div[2]')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'val1'
        val2 = 'val2'
        eve_id = '360'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_360_mother(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/div[2]')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'val1'
        val2 = 'val2'
        eve_id = '360'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_home(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_l2(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_brand(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_mother(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_grainger(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_l3(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_desktop(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_mobile(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_361_myaccount(self, url):
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
        self.finds_elements("//*[@id='search']", 'qh7')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li/a/div/form/button')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '361'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_home(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_l2(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_brand(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_mother(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_grainger(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_l3(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_desktop(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_mobile(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_362_myaccount(self, url):
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
        self.finds_elements("//*[@id='search']", 'q')
        self.finds_elements('//*[@id="search_autocomplete"]/div/ul/li[3]/a/div/span')
        #self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = 'Position | Item Name'
        val2 = ''
        eve_id = '362'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_64_home(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_64"]')  #//*[@id="eve_64"]
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '64'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_64_l2(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_64"]')  #//*[@id="eve_64"]
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '64'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_64_brand(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_64"]')  #//*[@id="eve_64"]
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '64'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_64_bfc(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_64"]')  #//*[@id="eve_64"]
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '64'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_64_mother(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_64"]')  #//*[@id="eve_64"]
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '64'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_64_l3(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_64"]')  #//*[@id="eve_64"]
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '64'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_64_product(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_64"]')  #//*[@id="eve_64"]
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '64'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

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
        con = "BP"
        val1 = '# Filter_name'
        val2 = '# filter1 value1 | value 2..'
        eve_id = '228'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_228_fastner(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.chat_box_close()
        self.finds_elements('//*[@id="at_brand"]')
        time.sleep(3)
        self.finds_elements('//*[@id="brandFilter"]/div/label[1]')
        self.finds_elements('//*[@id="close"]/span')
        self.finds_elements('//*[@id="xyz"]')

        self.print_visitor_id()
        con = "BP"
        val1 = '# Filter_name'
        val2 = '# filter1 value1 | value 2..'
        eve_id = '228'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

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
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

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
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

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
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_15_mother(self, url):
        self.request_func(url)
        add_to_cart = "//*[@class='addto_cart']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        time.sleep(2)
        close_cart_popup = '//*[@id="eve_295"]'
        self.finds_elements(close_cart_popup)
        shop_cart = '//*[@class="counter"]'
        self.finds_elements(shop_cart)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#pd count'
        val2 = ''
        eve_id = '15'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_15_l3(self, url):
        self.request_func(url)
        add_to_cart = "//*[@id='atc_0']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        time.sleep(2)
        close_cart_popup = '//*[@id="eve_295"]'
        self.finds_elements(close_cart_popup)
        shop_cart = '//*[@id="eve_15"]'
        self.finds_elements(shop_cart)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#pd count'
        val2 = ''
        eve_id = '15'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_15_brand(self, url):
        self.request_func(url)
        shop_cart = '//*[@id="cart-counter"]'
        self.finds_elements(shop_cart)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#pd count'
        val2 = ''
        eve_id = '15'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_15_l2(self, url):
        self.request_func(url)
        shop_cart = '//*[@class="counter"]'
        self.finds_elements(shop_cart)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#pd count'
        val2 = ''
        eve_id = '15'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_15_home(self, url):
        self.request_func(url)
        shop_cart = '//*[@id="eve_15"]'
        self.finds_elements(shop_cart)
        self.print_visitor_id()
        con = "BPN"
        val1 = '#pd count'
        val2 = ''
        eve_id = '15'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_224_l2(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '224'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_224_l3(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '224'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_224_bfc(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '224'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_224_p(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '224'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_224_c3(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '224'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_224_c4(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '224'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_225_l2(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        time.sleep(2)
        # self.finds_elements('//*[@id="at_23339"]/span[2]') 
        self.finds_elements('document.querySelector("#at_brand").click()')
        # self.finds_elements('//*[@class="fileter-inner"]/label/span')
        # self.finds_elements('//*[@id="at_brand"]')
        self.finds_elements('//*[@id="brandFilter"]/div/label[1]/span')
        self.print_visitor_id()
        con = ""
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '225'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_225_l3(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        time.sleep(2)
        # self.finds_elements('//*[@id="at_23339"]/span[2]') 
        self.finds_elements('document.querySelector("#at_31154").click()')
        # self.finds_elements('//*[@class="fileter-inner"]/label/span')
        # self.finds_elements('//*[@id="at_brand"]')
        self.finds_elements('//*[@id="469097"]/span')
        self.print_visitor_id()
        con = ""
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '225'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_225_bfc(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        time.sleep(2)
        self.finds_elements('document.querySelector("#at_31154").click()')
        # self.finds_elements('//*[@class="fileter-inner"]/label/span')
        # self.finds_elements('//*[@id="at_brand"]')
        self.finds_elements('//*[@id="510828"]/span')
        self.print_visitor_id()
        con = ""
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '225'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_225_p(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        time.sleep(2)
        # self.finds_elements('//*[@id="at_23339"]/span[2]') 
        self.finds_elements('document.querySelector("#at_31154").click()')
        # self.finds_elements('//*[@class="fileter-inner"]/label/span')
        # self.finds_elements('//*[@id="at_brand"]')
        self.finds_elements('//*[@id="487359"]')
        self.print_visitor_id()
        con = ""
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '225'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_5_home(self, url):
        self.request_func(url)
        self.page.wait_for_selector("#search").click()
        self.page.wait_for_selector("#search").fill('q')
        time.sleep(2)
        self.finds_elements('#searchBtn')
        time.sleep(6)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '5'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_5_L2(self, url):
        self.request_func(url)
        self.page.wait_for_selector("#search").click()
        self.page.wait_for_selector("#search").fill('q')
        time.sleep(2)
        self.finds_elements('#searchBtn')
        time.sleep(8)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '5'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_5_brand(self, url):
        self.request_func(url)

        self.page.wait_for_selector("#search").click()
        self.page.wait_for_selector("#search").fill('q')
        time.sleep(2)
        self.finds_elements('#searchBtn')
        time.sleep(6)

        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '5'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_5_mother(self, url):
        self.request_func(url)
        self.page.wait_for_selector("#search").click()
        time.sleep(2)
        self.page.wait_for_selector("#search").fill('q')
        self.finds_elements('#searchBtn')
        time.sleep(6)

        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '5'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_5_L3(self, url):
        self.request_func(url)
        self.page.wait_for_selector("#search").click()
        time.sleep(2)
        self.page.wait_for_selector("#search").fill('q')
        self.finds_elements('#searchBtn')
        time.sleep(6)

        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '5'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_5_product_desk(self, url):
        self.request_func(url)
        self.page.wait_for_selector("#search").click()
        time.sleep(2)
        self.page.wait_for_selector("#search").fill('q')
        self.finds_elements('#searchBtn')
        time.sleep(6)

        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '5'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_5_product_mobile(self, url):
        self.mobile_screen_request(url)
        self.page.wait_for_selector("#search").click()
        time.sleep(2)
        self.page.wait_for_selector("#search").fill('q')
        self.finds_elements('#searchBtn')
        time.sleep(6)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '5'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_5_account(self, url):
        # self.request_func(url)
        self.request_func(url)
        # self.finds_elements('//*[@id="eve_13"]')
        # print('sign in')
        self.finds_elements('//*[@id="email"]', 'devanshu@nextgenesolutions.com')
        print('username')
        self.finds_elements('//*[@id="pass"]', 'Devanshu@123')
        print('password')
        self.chat_box_close()
        self.finds_elements('//*[@id="send2"]')
        print('login')
        self.finds_elements("//*[@id='search']", 'dyton')
        pyautogui.press('enter')
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '5'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_6_home(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", 'asdfghjklsdfgh')
        self.finds_elements('#searchBtn')
        # self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '6'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_6_L2(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", '1asdgasg')
        self.finds_elements('#searchBtn')
        time.sleep(4)
        self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '6'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_6_brand(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", '1asdgasg')
        self.finds_elements('#searchBtn')
        time.sleep(4)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '6'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_6_mother(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", '1asdgasg')
        self.finds_elements('#searchBtn')
        time.sleep(4)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '6'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_6_grainger(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", '1asdgasg')
        self.finds_elements('#searchBtn')
        time.sleep(4)
        self.print_visitor_id()

        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '6'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_6_L3(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", '1asdgasg')
        self.finds_elements('#searchBtn')
        time.sleep(4)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '6'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_6_product_desk(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", '1asdgasg')
        self.finds_elements('#searchBtn')
        time.sleep(4)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '6'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_6_product_mobile(self, url):
        self.mobile_screen_request(url)
        self.finds_elements("//*[@id='search']", '1asdgasg')
        time.sleep(4)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '6'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_6_account(self, url):
        self.request_func(url)
        self.finds_elements("//*[@id='search']", '1asdgasg')
        # pyautogui.press('enter')
        time.sleep(4)
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '6'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_7_home(self, url):
        self.request_func(url)
        self.page.wait_for_selector("#search").click()
        time.sleep(2)
        self.page.wait_for_selector("#search").fill('morse')
        logo_element = self.page.query_selector('.logo')
        if logo_element:
            logo_element.click()
        else:
            self.page.click("body")
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '7'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_7_L2(self, url):
        self.request_func(url)
        self.page.wait_for_selector("#search").click()
        time.sleep(2)
        self.page.wait_for_selector("#search").fill('morse')
        logo_element = self.page.query_selector('.logo')
        if logo_element:
            logo_element.click()
        else:
            self.page.click("body")
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '7'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_7_brand(self, url):
        self.request_func(url)
        self.page.wait_for_selector("#search").click()
        time.sleep(2)
        self.page.wait_for_selector("#search").fill('morse')
        logo_element = self.page.query_selector('.logo')
        if logo_element:
            logo_element.click()
        else:
            self.page.click("body")
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '7'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_7_mother(self, url):
        self.request_func(url)
        self.page.wait_for_selector("#search").click()
        time.sleep(2)
        self.page.wait_for_selector("#search").fill('morse')
        logo_element = self.page.query_selector('.logo')
        if logo_element:
            logo_element.click()
        else:
            self.page.click("body")
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '7'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_7_grainger(self, url):
        self.request_func(url)
        self.page.wait_for_selector("#search").click()
        time.sleep(2)
        self.page.wait_for_selector("#search").fill('morse')
        logo_element = self.page.query_selector('.logo')
        if logo_element:
            logo_element.click()
        else:
            self.page.click("body")
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '7'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_7_L3(self, url):
        self.request_func(url)
        self.page.wait_for_selector("#search").click()
        time.sleep(2)
        self.page.wait_for_selector("#search").fill('morse')
        logo_element = self.page.query_selector('.logo')
        if logo_element:
            logo_element.click()
        else:
            self.page.click("body")
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '7'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_7_product_desk(self, url):
        self.request_func(url)
        self.page.wait_for_selector("#search").click()
        time.sleep(2)
        self.page.wait_for_selector("#search").fill('morse')
        logo_element = self.page.query_selector('.logo')
        if logo_element:
            logo_element.click()
        else:
            self.page.click("body")
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '7'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_7_product_mobile(self, url):
        self.mobile_screen_request(url)
        #    self.request_func(url)
        comment = '//*[@id="search"]'
        self.finds_elements(comment, 'morse')
        self.finds_elements('//*[@id="eve_9"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '7'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_7_account(self, url):
        self.request_func(url)
        comment = '//*[@id="search"]'
        self.finds_elements(comment, 'morse')
        self.finds_elements('//*[@id="eve_9"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '7'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_8_home(self, url):
        self.request_func(url)
        comment = '//*[@id="search"]'
        self.finds_elements(comment)
        # pyautogui.press('enter')
        # self.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '8'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_8_L2(self, url):
        self.request_func(url)
        comment = '//*[@id="search"]'
        self.finds_elements(comment)
        # pyautogui.press('enter')
        # self.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '8'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_8_brand(self, url):
        self.request_func(url)
        comment = '//*[@id="search"]'
        self.finds_elements(comment)
        # pyautogui.press('enter')
        # self.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '8'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_8_mother(self, url):
        self.request_func(url)
        comment = '//*[@id="search"]'
        self.finds_elements(comment)
        # pyautogui.press('enter')
        # self.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '8'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_8_grainger(self, url):
        self.request_func(url)
        comment = '//*[@id="search"]'
        self.finds_elements(comment)
        # pyautogui.press('enter')
        # self.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '8'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_8_L3(self, url):
        self.request_func(url)
        comment = '//*[@id="search"]'
        self.finds_elements(comment)
        # self.finds_elements('//*[@id="eve_9"]')
        # self.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '8'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_8_product_desk(self, url):
        self.request_func(url)
        comment = '//*[@id="search"]'
        self.finds_elements(comment)
        # pyautogui.press('enter')
        # self.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '8'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_8_product_mobile(self, url):
        self.mobile_screen_request(url)
        comment = '//*[@id="search"]'
        self.finds_elements(comment)
        # pyautogui.press('enter')
        #self.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '8'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_8_account(self, url):
        self.request_func(url)
        # self.finds_elements('//*[@id="eve_13"]')
        # print('sign in')
        self.finds_elements('//*[@id="email"]', 'devanshu@nextgenesolutions.com')
        print('username')
        self.finds_elements('//*[@id="pass"]', 'Devanshu@123')
        print('password')
        self.chat_box_close()
        self.finds_elements('//*[@id="send2"]')
        print('login')
        self.finds_elements("//*[@id='search']", 'dyton')
        pyautogui.press('enter')
        self.back()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '8'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_73_fasteners(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="row1"]/td[3]')
        self.print_visitor_id()
        con = "BP"
        val1 = 'Title'
        val2 = 'View name'
        eve_id = '73'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_226_l3(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.finds_elements('//h4[text()="Length"]')
        self.finds_elements('//input[@class="search-query filter_Fastener_search"]', 'abc')
        self.finds_elements('//*[@id="filtersection"]/div[2]/div/div[1]/span')
        self.print_visitor_id()
        con = ""
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '226'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_226_l4(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.finds_elements('//*[text()="Thread Length"]')
        #self.finds_elements('//*[@class="search-query filter_Fastener_search"]')
        self.finds_elements('//input[@class="search-query filter_Fastener_search"]', '3/8')
        self.finds_elements('//*[@id="filtersection"]/div[2]/div/div[1]/span')
        #self.finds_elements('///span[@class="searchicon"]')
        self.print_visitor_id()
        con = ""
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '226'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_226_mother(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="eve_224"]')
        self.finds_elements('//*[text()="Thread Length"]')
        self.finds_elements('//input[@class="search-query filter_Fastener_search"]', 'abc')
        self.finds_elements('//*[@id="filtersection"]/div[2]/div/div[1]/span')
        #self.finds_elements('//span[@class="searchicon"]')
        self.print_visitor_id()
        con = ""
        val1 = '#Filter type'
        val2 = 'filter type value'
        eve_id = '226'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_402_brand(self, url):
        self.request_func(url)
        self.finds_elements('//*[@class="rfq-btn"]')
        self.finds_elements('//*[@id="eve_402"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '402'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_402_l3_default(self, url):
        self.request_func(url)
        self.finds_elements('//*[@class="add_cart caterfq"]')
        self.finds_elements('//*[@id="eve_402"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '402'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_402_l3_grid(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="eve_111"]')
        self.finds_elements('//div[text()="RFQ"]')
        self.finds_elements('//*[@id="eve_402"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '402'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_402_l3_list(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="listViewSwitch"]')
        self.finds_elements('//div[text()="RFQ"]')
        self.finds_elements('//*[@id="eve_402"]')

        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '402'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_402_l4_default(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="row1_2"]/td[2]')
        self.finds_elements('//div[text()="RFQ"]')
        self.finds_elements('//*[@id="eve_402"]')

        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '402'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_402_mother_fastner(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="row1"]')
        self.finds_elements('//*[@id="4880880"]')
        self.finds_elements('//*[@id="eve_402"]')

        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '402'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_402_mother_nonfastner(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="4948952"]')
        self.finds_elements('//*[@id="eve_402"]')

        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '402'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_402_desktop_pd(self, url):
        self.request_func(url)
        self.finds_elements('//*[@id="main_rfq_btn"]')
        self.finds_elements('//*[@id="eve_402"]')

        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '402'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_12_home(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements('//*[@class="country-change"]')
        self.finds_elements('//*[@id="top_country_list"]', 'United Kingdom')
        time.sleep(2)
        self.finds_elements('//*[@id="eve_12"]')
        # self.chat_box_close()
        # self.finds_elements('//*[@class="submenu"]/li[3]')
        # pyautogui.press('enter')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = 'Name'
        eve_id = '12'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_12_l2(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements('//span[text()="Change Country"]')
        self.finds_elements('//*[@id="top_country_list"]', 'India')
        time.sleep(2)
        self.finds_elements('//*[@id="eve_12"]')
        # self.chat_box_close()
        # self.finds_elements('//*[@class="submenu"]/li[3]')
        # pyautogui.press('enter')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = 'Name'
        eve_id = '12'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_12_brand(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements('//span[text()="Change Country"]')
        self.finds_elements('//*[@id="top_country_list"]', 'Togo')
        time.sleep(2)
        self.finds_elements('//*[@id="eve_12"]')
        # self.chat_box_close()
        # self.finds_elements('//*[@class="submenu"]/li[3]')
        # pyautogui.press('enter')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = 'Name'
        eve_id = '12'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_12_mother(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements('//span[text()="Change Country"]')
        self.finds_elements('//*[@id="top_country_list"]', 'Austria')
        time.sleep(2)
        self.finds_elements('//*[@id="eve_12"]')
        # self.chat_box_close()
        # self.finds_elements('//*[@class="submenu"]/li[3]')
        # pyautogui.press('enter')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = 'Name'
        eve_id = '12'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_12_grainger(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements('//span[text()="Change Country"]')
        self.finds_elements('//*[@id="top_country_list"]', 'Benin')
        time.sleep(2)
        self.finds_elements('//*[@id="eve_12"]')
        # self.chat_box_close()
        # self.finds_elements('//*[@class="submenu"]/li[3]')
        # pyautogui.press('enter')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = 'Name'
        eve_id = '12'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_12_l3(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements('//span[text()="Change Country"]')
        self.finds_elements('//*[@id="top_country_list"]', 'Germany')
        time.sleep(2)
        self.finds_elements('//*[@id="eve_12"]')
        # self.chat_box_close()
        # self.finds_elements('//*[@class="submenu"]/li[3]')
        # pyautogui.press('enter')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = 'Name'
        eve_id = '12'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_12_desktop_pd(self, url):
        self.request_func(url)
        self.element_hover("//*[@class='flag']")
        self.finds_elements('//span[text()="Change Country"]')
        self.finds_elements('//*[@id="top_country_list"]', 'Iraq')
        time.sleep(2)
        self.finds_elements('//*[@id="eve_12"]')
        # self.chat_box_close()
        # self.finds_elements('//*[@class="submenu"]/li[3]')
        # pyautogui.press('enter')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = 'Name'
        eve_id = '12'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_12_mobile_pd(self, url):
        self.mobile_screen_request(url)
        self.finds_elements('//*[@id="myHeader"]/div[1]/div[1]/span')
        self.finds_elements("//*[name()='svg' and @class='bi bi-globe2']")
        #self.finds_elements('//span[text()="Change Country"]')
        self.finds_elements('//*[@id="top_country_list"]', 'Japan')
        self.finds_elements('//*[@id="eve_12"]')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = 'Name'
        eve_id = '12'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_98_brandlist(self, url):
        self.request_func(url)
        email = '//*[@id="mailto1"]'
        self.finds_elements(email)
        pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '98'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_98_signin(self, url):
        self.request_func(url)
        email = '//*[@id="mailto1"]'
        self.finds_elements(email)
        pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '98'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_98_grainger(self, url):
        self.request_func(url)
        # self.chat_box_close()
        email = '//*[@id="eve_98"]'
        self.finds_elements(email)
        # pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '98'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_99_brandlist(self, url):
        self.request_func(url)
        self.chat_box_close()
        phone = '//a[@href="tel:+44 203 287 5224"]'
        self.finds_elements(phone)
        pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '99'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_99_signin(self, url):
        self.request_func(url)
        self.chat_box_close()
        phone = '//*[@id="eve_99"]'
        self.finds_elements(phone)
        pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '99'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_99_grainger(self, url):
        self.request_func(url)
        # self.chat_box_close()
        phone = '//*[@id="eve_99"]'
        self.finds_elements(phone)
        # pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '99'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_100_brandlist(self, url):
        self.request_func(url)
        self.chat_box_close()
        phone = '//a[@href="/whatsapp?click=d_clink"]'
        self.finds_elements(phone)
        pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '100'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_100_signin(self, url):
        self.request_func(url)
        self.chat_box_close()
        phone = '//a[@href="/whatsapp?click=d_clink"]'
        self.finds_elements(phone)
        pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '100'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_100_grainger(self, url):
        self.request_func(url)
        self.chat_box_close()
        phone = '//a[@href="/whatsapp?click=d_clink"]'
        self.finds_elements(phone)
        # pyautogui.press('esc')
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '100'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_96_homepage(self, url):
        self.request_func(url)
        explore_pd = '//a[@href="https://www.raptorsupplies.com/pd/lovejoy/68514411512"]'
        self.finds_elements(explore_pd)
        self.print_visitor_id()
        con = "BPN"
        val1 = 'NAME'
        val2 = 'URL'
        eve_id = '96'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_96_product(self, url):
        self.request_func(url)
        explore_pd = '//a[text()="SEALMASTER CRFCF-PN23"]'
        self.finds_elements(explore_pd)
        self.print_visitor_id()
        con = "BPN"
        val1 = 'NAME'
        val2 = 'URL'
        eve_id = '96'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_94_l1(self, url):
        self.request_func(url)
        self.chat_box_close()
        self.page.wait_for_selector('a[href*="whatsapp"]').click()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '94'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_94_l2(self, url):
        self.request_func(url)
        self.chat_box_close()
        self.page.wait_for_selector('a[href*="whatsapp"]').click()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '94'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_94_l3(self, url):
        self.request_func(url)
        self.chat_box_close()
        self.page.wait_for_selector('a[href*="whatsapp"]').click()
        # whatsapp = '//*[@id="eve_94"]/a'
        # self.finds_elements(whatsapp)
        # self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '94'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_94_mother(self, url):
        self.request_func(url)
        self.chat_box_close()
        self.page.wait_for_selector('a[href*="whatsapp"]').click()
        # whatsapp = '//a[text()=" Chat with us now"]'
        # self.finds_elements(whatsapp)
        # self.back()
        self.print_visitor_id()
        con = "BPN"
        val1 = ''
        val2 = ''
        eve_id = '94'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_90_home(self, url):
        self.request_func(url)
        self.reload()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '90'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_90_L1(self, url):
        self.request_func(url)
        self.reload()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '90'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_90_L2(self, url):
        self.request_func(url)
        self.reload()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '90'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_90_L3(self, url):
        self.request_func(url)
        self.reload()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '90'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_90_BFC(self, url):
        self.request_func(url)
        self.reload()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '90'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_90_Fasteners_L4(self, url):
        self.request_func(url)
        self.reload()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '90'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_90_mother(self, url):
        self.request_func(url)
        self.reload()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '90'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_90_product(self, url):
        self.request_func(url)
        self.reload()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '90'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    def eve_90_P1(self, url):
        self.request_func(url)
        self.reload()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '90'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)

    
    def eve_90_brand(self, url):
        self.request_func(url)
        self.reload()
        self.print_visitor_id()
        con = "BP"
        val1 = ''
        val2 = ''
        eve_id = '90'
        self.report_genrate_global(self.print_visitor_id(), con, val1, val2, eve_id, url)
def run_program():
    program_dict = {
        'eve_22_pd': 'eve_22_pd("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_22_mother': 'eve_22_mother("https://www.raptorsupplies.com/p/b-p-manufacturing/s-series-1000lbs-convertible-hand-truck")',
        'eve_22_category': 'eve_22_category("https://www.raptorsupplies.com/c/disc-pad-face-plates-and-hubs")',
        'eve_22_brand': 'eve_22_brand("https://www.raptorsupplies.com/b/bp-mfg")',
        'eve_22_brand_l3': 'eve_22_brand_l3("https://www.raptorsupplies.com/c/convertible-hand-trucks/bp-mfg")',
        'eve_22_l1': 'eve_22_l1("https://www.raptorsupplies.com/l1/abrasives")',
        'eve_22_l2': 'eve_22_l2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_22_fastener': 'eve_22_fastener("https://www.raptorsupplies.com/c/fasteners/c5/plain-grade-18-8-stainless-steel-hex-head-cap-screws")',

        'eve_265_brand': 'eve_265_brand("https://www.raptorsupplies.com/b")',
        'eve_265_brand_list': 'eve_265_brand_list("https://www.raptorsupplies.com/b/d")',

        'eve_58_cat': 'eve_58_cat("https://www.raptorsupplies.com/b/ad-weighing")',
        'eve_58_more': 'eve_58_more("https://www.raptorsupplies.com/b/3m")',
        'eve_58_less': 'eve_58_less("https://www.raptorsupplies.com/b/allegro-safety")',

        'eve_28_default': 'eve_28_default("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_28_include': 'eve_28_include("https://www.raptorsupplies.com/pd/aurand/s2k7")',
        'eve_28_p1': 'eve_28_p1("https://www.raptorsupplies.com/p1/akro-mils/30080-series-shelf-bin")',

        'eve_29_default': 'eve_29_default("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_29_include': 'eve_29_include("https://www.raptorsupplies.com/pd/aurand/s2k7")',
        'eve_29_p1': 'eve_29_p1("https://www.raptorsupplies.com/p1/akro-mils/30080-series-shelf-bin")',

        'eve_32_default': 'eve_32_default("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_32_include': 'eve_32_include("https://www.raptorsupplies.com/pd/aurand/k7-1v")',
        'eve_32_p1': 'eve_32_p1("https://www.raptorsupplies.com/p1/akro-mils/30080-series-shelf-bin")',

        'eve_33_default': 'eve_33_default("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_33_include': 'eve_33_include("https://www.raptorsupplies.com/pd/aurand/k7-1v")',
        'eve_33_p1': 'eve_33_p1("https://www.raptorsupplies.com/p1/akro-mils/30080-series-shelf-bin")',

        'eve_34_default': 'eve_34_default("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_34_include': 'eve_34_include("https://www.raptorsupplies.com/pd/aurand/k7-1v")',
        'eve_34_p1': 'eve_34_p1("https://www.raptorsupplies.com/p1/akro-mils/30080-series-shelf-bin")',

        'eve_35_default': 'eve_35_default("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_35_include': 'eve_35_include("https://www.raptorsupplies.com/pd/aurand/k7-1v")',
        'eve_35_p1': 'eve_35_p1("https://www.raptorsupplies.com/p1/akro-mils/30080-series-shelf-bin")',

        'eve_101_default': 'eve_101_default("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_101_include': 'eve_101_include("https://www.raptorsupplies.com/pd/aurand/k7-1v")',

        'eve_38_default': 'eve_38_default("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_38_include': 'eve_38_include("https://www.raptorsupplies.com/pd/aurand/k7-1v")',
        'eve_38_p1': 'eve_38_p1("https://www.raptorsupplies.com/p1/akro-mils/30080-series-shelf-bin")',

        'eve_39_default': 'eve_39_default("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_39_include': 'eve_39_include("https://www.raptorsupplies.com/pd/aurand/k7-1v")',
        'eve_39_p1': 'eve_39_p1("https://www.raptorsupplies.com/p1/akro-mils/30080-series-shelf-bin")',

        'eve_51_default': 'eve_51_default("https://www.raptorsupplies.com/pd/morse-drum/92")',
        'eve_51_include': 'eve_51_include("https://www.raptorsupplies.com/pd/aurand/k7-1v")',
        'eve_51_p1': 'eve_51_p1("https://www.raptorsupplies.com/p1/akro-mils/30080-series-shelf-bin")',

        'eve_93_home': 'eve_93_home("https://www.raptorsupplies.com/")',
        'eve_93_l2': 'eve_93_l2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_93_l3': 'eve_93_l3("https://www.raptorsupplies.com/c/abrasive-mandrels")',
        'eve_93_p': 'eve_93_p("https://www.raptorsupplies.com/p/norton/mandrel-assembly")',
        'eve_93_pd': 'eve_93_pd("https://www.raptorsupplies.com/pd/norton/66261059422")',
        'eve_93_b': 'eve_93_b("https://www.raptorsupplies.com/b/3m")',
        'eve_93_bfc': 'eve_93_bfc("https://www.raptorsupplies.com/c/respirator-accessories/3m")',

        'eve_307_mro': 'eve_307_mro("https://www.raptorsupplies.com/mro-supplier")',
        'eve_307_grainer': 'eve_307_grainer("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_307_zeus': 'eve_307_zeus("https://www.raptorsupplies.com/b/zeus")',

        'eve_308_mro': 'eve_308_mro("https://www.raptorsupplies.com/mro-supplier")',
        'eve_308_grainer': 'eve_308_grainer("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_308_zeus': 'eve_308_zeus("https://www.raptorsupplies.com/b/zeus")',

        'eve_309_mro': 'eve_309_mro("https://www.raptorsupplies.com/mro-supplier")',
        'eve_309_grainer': 'eve_309_grainer("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_309_zeus': 'eve_309_zeus("https://www.raptorsupplies.com/b/zeus")',

        'eve_310_mro': 'eve_310_mro("https://www.raptorsupplies.com/mro-supplier")',
        'eve_310_grainer': 'eve_310_grainer("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_310_zeus': 'eve_310_zeus("https://www.raptorsupplies.com/b/zeus")',

        'eve_311_mro': 'eve_311_mro("https://www.raptorsupplies.com/mro-supplier")',
        'eve_311_grainer': 'eve_311_grainer("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_311_zeus': 'eve_311_zeus("https://www.raptorsupplies.com/b/zeus")',

        'eve_92_blog': 'eve_92_blog("https://www.raptorsupplies.com/")',

        'eve_345_b': 'eve_345_b("https://www.raptorsupplies.com/b/char-lynn")',
        'eve_345_l3': 'eve_345_l3("https://www.raptorsupplies.com/c/hydraulic-filters")',
        'eve_345_bfc': 'eve_345_bfc("https://www.raptorsupplies.com/c/hydraulic-filters/main-filter-inc")',

        'eve_72_fastener_listview': 'eve_72_fastener_listview("https://www.raptorsupplies.com/c/fasteners/c3/adhesive-anchors")',
        'eve_72_fastener_gridview': 'eve_72_fastener_gridview("https://www.raptorsupplies.com/c/fasteners/c3/adhesive-anchor-accessories")',
        'eve_72_fastener_defaultview': 'eve_72_fastener_defaultview("https://www.raptorsupplies.com/c/fasteners/c3/hammer-drive-pin-anchors")',
        'eve_72_nonfastener_listtview': 'eve_72_nonfastener_listtview("https://www.raptorsupplies.com/c/test-equipment")',
        'eve_72_nonfastener_gridview': 'eve_72_nonfastener_gridview("https://www.raptorsupplies.com/c/cabinet-accessory")',
        'eve_72_nonfastener_defaultview': 'eve_72_nonfastener_defaultview("https://www.raptorsupplies.com/c/fiber-optic-adapters")',

        'eve_103_nonfastener_listtview': 'eve_103_nonfastener_listtview("https://www.raptorsupplies.com/c/test-equipment")',
        'eve_103_nonfastener_gridview': 'eve_103_nonfastener_gridview("https://www.raptorsupplies.com/c/cabinet-accessory")',
        'eve_103_nonfastener_defaultview': 'eve_103_nonfastener_defaultview("https://www.raptorsupplies.com/c/ethernet-switches")',
        'eve_103_fastener_defaultview': 'eve_103_fastener_defaultview("https://www.raptorsupplies.com/c/fasteners/c4/adjustable-band-hangers-with-felt-lining")',

        'eve_148_home_git': 'eve_148_home_git("https://www.raptorsupplies.com/")',
        'eve_148_git': 'eve_148_git("https://www.raptorsupplies.com/l1/abrasives")',
        'eve_148_mro': 'eve_148_mro("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_148_bfc_mro': 'eve_148_bfc_mro("https://www.raptorsupplies.com/c/respirator-accessories/3m")',
        'eve_148_l3_mro': 'eve_148_l3_mro("https://www.raptorsupplies.com/c/downdraft-tables")',
        'eve_148_motherlist_mro': 'eve_148_motherlist_mro("https://www.raptorsupplies.com/p/norton/mandrel-assembly")',

        'eve_149_home_git': 'eve_149_home_git("https://www.raptorsupplies.com/")',
        'eve_149_git': 'eve_149_git("https://www.raptorsupplies.com/l1/abrasives")',
        'eve_149_l3_mro': 'eve_149_l3_mro("https://www.raptorsupplies.com/c/downdraft-tables")',
        'eve_149_mro': 'eve_149_mro("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_149_bfc_mro': 'eve_149_bfc_mro("https://www.raptorsupplies.com/c/respirator-accessories/3m")',
        'eve_149_motherlist_mro': 'eve_149_motherlist_mro("https://www.raptorsupplies.com/p/norton/mandrel-assembly")',

        'eve_150_home_git': 'eve_150_home_git("https://www.raptorsupplies.com/")',
        'eve_150_git': 'eve_150_git("https://www.raptorsupplies.com/l1/abrasives")',
        'eve_150_mro': 'eve_150_mro("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_150_bfc_mro': 'eve_150_bfc_mro("https://www.raptorsupplies.com/c/respirator-accessories/3m")',
        'eve_150_motherlist_mro': 'eve_150_motherlist_mro("https://www.raptorsupplies.com/p/norton/mandrel-assembly")',
        'eve_150_l3_mro': 'eve_150_l3_mro("https://www.raptorsupplies.com/c/downdraft-tables")',

        'eve_151_home_git': 'eve_151_home_git("https://www.raptorsupplies.com/")',
        'eve_151_git': 'eve_151_git("https://www.raptorsupplies.com/l1/abrasives")',
        'eve_151_mro': 'eve_151_mro("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_151_bfc_mro': 'eve_151_bfc_mro("https://www.raptorsupplies.com/c/respirator-accessories/3m")',
        'eve_151_motherlist_mro': 'eve_151_motherlist_mro("https://www.raptorsupplies.com/p/norton/mandrel-assembly")',
        'eve_151_l3_mro': 'eve_151_l3_mro("https://www.raptorsupplies.com/c/downdraft-tables")',

        'eve_109_nonfastener_listtview': 'eve_109_nonfastener_listtview("https://www.raptorsupplies.com/c/test-equipment")',
        'eve_109_nonfastener_gridview': 'eve_109_nonfastener_gridview("https://www.raptorsupplies.com/c/cabinet-accessory")',
        'eve_109_nonfastener_defaultview': 'eve_109_nonfastener_defaultview("https://www.raptorsupplies.com/c/drum-lifters")',
        'eve_109_fastener_listtview': 'eve_109_fastener_listtview("https://www.raptorsupplies.com/c/fasteners/c3/double-loop-and-jack-chain")',
        'eve_109_fastener_gridview': 'eve_109_fastener_gridview("https://www.raptorsupplies.com/c/fasteners/c3/adhesive-anchors")',
        'eve_109_fastener_defaultview': 'eve_109_fastener_defaultview("https://www.raptorsupplies.com/c/fasteners/c3/adhesive-anchor-accessories")',

        'eve_110_nonfastener_listtview': 'eve_110_nonfastener_listtview("https://www.raptorsupplies.com/c/coliwasas")',
        'eve_110_nonfastener_gridview': 'eve_110_nonfastener_gridview("https://www.raptorsupplies.com/c/drum-lifters")',
        'eve_110_nonfastener_defaultview': 'eve_110_nonfastener_defaultview("https://www.raptorsupplies.com/c/drum-accessories")',
        'eve_110_fastener_listtview': 'eve_110_fastener_listtview("https://www.raptorsupplies.com/c/fasteners/c3/double-loop-and-jack-chain")',
        'eve_110_fastener_gridtview': 'eve_110_fastener_gridtview("https://www.raptorsupplies.com/c/fasteners/c3/thread-measuring-gauges")',
        'eve_110_fastener_defaultview': 'eve_110_fastener_defaultview("https://www.raptorsupplies.com/c/fasteners/c3/clamp-assortments")',

        'eve_111_nonfastener_listtview': 'eve_111_nonfastener_listtview("https://www.raptorsupplies.com/c/test-equipment")',
        'eve_111_nonfastener_gridview': 'eve_111_nonfastener_gridview("https://www.raptorsupplies.com/c/sanding-sheet-hand-pad-holders-and-blocks")',
        'eve_111_nonfastener_defaultview': 'eve_111_nonfastener_defaultview("https://www.raptorsupplies.com/c/abrasive-mandrels")',
        'eve_111_fastener_listtview': 'eve_111_fastener_listtview("https://www.raptorsupplies.com/c/fasteners/c3/bolt-caps")',
        'eve_111_fastener_gridtview': 'eve_111_fastener_gridtview("https://www.raptorsupplies.com/c/fasteners/c3/adhesive-anchor-accessories")',
        'eve_111_fastener_defaultview': 'eve_111_fastener_defaultview("https://www.raptorsupplies.com/c/fasteners/c3/cap-nails")',

        'eve_65_fastener_L4': 'eve_65_fastener_L4("https://www.raptorsupplies.com/c/fasteners/c4/grade-18-8-stainless-steel-hex-head-cap-screws")',
        'eve_65_fastener_L5': 'eve_65_fastener_L5("https://www.raptorsupplies.com/c/fasteners/c5/plain-grade-18-8-stainless-steel-hex-head-cap-screws")',
        'eve_65_L2': 'eve_65_L2("https://www.raptorsupplies.com/l2/data-and-communication")',
        'eve_65_L3': 'eve_65_L3("https://www.raptorsupplies.com/c/test-equipment")',
        'eve_65_mother': 'eve_65_mother("https://www.raptorsupplies.com/p/ideal/fiber-optic-cable-testing-instruments")',
        'eve_65_fastener_search': 'eve_65_fastener_search("https://www.raptorsupplies.com/c/fasteners/c3/cap-nails")',

        'eve_299_home': 'eve_299_home("https://www.raptorsupplies.com/")',
        'eve_299_l2': 'eve_299_l2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_299_brand': 'eve_299_brand("https://www.raptorsupplies.com/b/3m")',
        'eve_299_mother': 'eve_299_mother("https://www.raptorsupplies.com/p/norton/backup-pad")',
        'eve_299_grainger': 'eve_299_grainger("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_299_l3': 'eve_299_l3("https://www.raptorsupplies.com/c/abrasive-mandrels")',
        'eve_299_desktop': 'eve_299_desktop("https://www.raptorsupplies.com/pd/norton/66261059422")',
        'eve_299_myaccount': ' eve_299_myaccount("https://www.raptorsupplies.com/customer/account/")',

        'eve_300_home': 'eve_300_home("https://www.raptorsupplies.com/")',
        'eve_300_l2': 'eve_300_l2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_300_brand': 'eve_300_brand("https://www.raptorsupplies.com/b/3m")',
        'eve_300_mother': 'eve_300_mother("https://www.raptorsupplies.com/p/norton/backup-pad")',
        'eve_300_grainger': 'eve_300_grainger("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_300_l3': 'eve_300_l3("https://www.raptorsupplies.com/c/abrasive-mandrels")',
        'eve_300_desktop': 'eve_300_desktop("https://www.raptorsupplies.com/pd/norton/66261059422")',
        'eve_300_myaccount': ' eve_300_myaccount("https://www.raptorsupplies.com/customer/account/")',

        'eve_303_home': 'eve_303_home("https://www.raptorsupplies.com/")',
        'eve_303_l2': 'eve_303_l2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_303_brand': 'eve_303_brand("https://www.raptorsupplies.com/b")',
        'eve_303_mother': 'eve_303_mother("https://www.raptorsupplies.com/p/norton/backup-pad")',
        'eve_303_grainger': 'eve_303_grainger("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_303_l3': 'eve_303_l3("https://www.raptorsupplies.com/c/abrasive-mandrels")',
        'eve_303_desktop': 'eve_303_desktop("https://www.raptorsupplies.com/pd/norton/66261059422")',
        'eve_303_myaccount': ' eve_303_myaccount("https://www.raptorsupplies.com/customer/account/")',

        'eve_306_home': 'eve_306_home("https://www.raptorsupplies.com/")',
        'eve_306_l2': 'eve_306_l2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_306_brand': 'eve_306_brand("https://www.raptorsupplies.com/b/3m")',
        'eve_306_mother': 'eve_306_mother("https://www.raptorsupplies.com/p/norton/backup-pad")',
        'eve_306_grainger': 'eve_306_grainger("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_306_l3': 'eve_306_l3("https://www.raptorsupplies.com/c/abrasive-mandrels")',
        'eve_306_desktop': 'eve_306_desktop("https://www.raptorsupplies.com/pd/norton/66261059422")',

        'eve_64_home': 'eve_64_home("https://www.raptorsupplies.com/")',
        'eve_64_l2': 'eve_64_l2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_64_l3': 'eve_64_l3("https://www.raptorsupplies.com/c/abrasive-mandrels")',
        'eve_64_brand': 'eve_64_brand("https://www.raptorsupplies.com/b/3m")',
        'eve_64_bfc': 'eve_64_bfc("https://www.raptorsupplies.com/c/respirator-accessories/3m")',
        'eve_64_mother': 'eve_64_mother("https://www.raptorsupplies.com/p/norton/backup-pad")',
        'eve_64_product': 'eve_64_product("https://www.raptorsupplies.com/pd/norton/66261059422")',

        'eve_66_fastener_L4': 'eve_66_fastener_L4("https://www.raptorsupplies.com/c/fasteners/c4/grade-18-8-stainless-steel-hex-head-cap-screws")',
        'eve_66_fastener_L5': 'eve_66_fastener_L5("https://www.raptorsupplies.com/c/fasteners/c5/plain-grade-18-8-stainless-steel-hex-head-cap-screws")',
        'eve_66_L2': 'eve_66_L2("https://www.raptorsupplies.com/l2/data-and-communication")',
        'eve_66_L3': 'eve_66_L3("https://www.raptorsupplies.com/c/test-equipment")',
        'eve_66_mother': 'eve_66_mother("https://www.raptorsupplies.com/p/dayton/general-purpose-motor-open-dripproof")',

        'eve_65_fastener_L4': 'eve_65_fastener_L4("https://www.raptorsupplies.com/c/fasteners/c4/grade-18-8-stainless-steel-hex-head-cap-screws")',
        'eve_65_fastener_L5': 'eve_65_fastener_L5("https://www.raptorsupplies.com/c/fasteners/c5/plain-grade-18-8-stainless-steel-hex-head-cap-screws")',
        'eve_65_L2': 'eve_65_L2("https://www.raptorsupplies.com/l2/data-and-communication")',
        'eve_65_L3': 'eve_65_L3("https://www.raptorsupplies.com/c/test-equipment")',
        'eve_65_mother': 'eve_65_mother("https://www.raptorsupplies.com/p/ideal/fiber-optic-cable-testing-instruments")',
        'eve_65_fastener_search': 'eve_65_fastener_search("https://www.raptorsupplies.com/c/fasteners/c3/cap-nails")',

        'eve_67_fastener_L4': 'eve_67_fastener_L4("https://www.raptorsupplies.com/c/fasteners/c4/nylon-hex-head-cap-screws?cat=30157&catKey=49")',
        'eve_67_fastener_L5': 'eve_67_fastener_L5("https://www.raptorsupplies.com/c/fasteners/c5/plain-grade-18-8-stainless-steel-hex-head-cap-screws?cat=30171&catKey=15")',
        'eve_67_L2': 'eve_67_L2("https://www.raptorsupplies.com/l2/data-and-communication")',
        'eve_67_L3': 'eve_67_L3("https://www.raptorsupplies.com/c/test-equipment?cat=31154&catKey=655840")',
        'eve_67_mother': 'eve_67_mother("https://www.raptorsupplies.com/p/ideal/fiber-optic-cable-testing-instruments?cat=31154&catKey=512649")',
        'eve_67_fastener_search': 'eve_67_fastener_search("https://www.raptorsupplies.com/c/fasteners/c3/cap-nails")',

        'eve_68_fastener_L4': 'eve_68_fastener_L4("https://www.raptorsupplies.com/c/fasteners/c4/grade-8-steel-hex-head-cap-screws?cat=30157&catKey=49")',
        'eve_68_fastener_L5': 'eve_68_fastener_L5("https://www.raptorsupplies.com/c/fasteners/c5/plain-grade-18-8-stainless-steel-hex-head-cap-screws?cat=30168&catKey=46356")',
        'eve_68_mother': 'eve_68_mother("https://www.raptorsupplies.com/p/dayton/general-purpose-motor-open-dripproof?cat=25407&catKey=230093")',
        'eve_68_fastener_search': 'eve_68_fastener_search("https://www.raptorsupplies.com/c/fasteners/c3/cap-nails")',

        'eve_113_nonfasteners': 'eve_113_nonfasteners("https://www.raptorsupplies.com/p/tough-guy/counter-duster")',
        'eve_113_fasteners_default': 'eve_113_fasteners_default("https://www.raptorsupplies.com/c/fasteners/p/blue-climaseal-steel-flat-star-concrete-anchor-screws")',
        'eve_113_fasteners_grid': 'eve_113_fasteners_grid("https://www.raptorsupplies.com/c/fasteners/p/blue-ruspert-steel-hex-slotted-concrete-anchor-screws")',

        'eve_114_nonfasteners': 'eve_114_nonfasteners("https://www.raptorsupplies.com/p/tough-guy/bench-counter-brush")',
        'eve_114_fasteners_grid': 'eve_114_fasteners_grid("https://www.raptorsupplies.com/c/fasteners/p/stainless-steel-screen-tube-8-size")',
        'eve_114_fasteners_default': 'eve_114_fasteners_default("https://www.raptorsupplies.com/c/fasteners/p/3-16-tapered-gib-head-machine-key")',

        'eve_115_nonfasteners': 'eve_115_nonfasteners("https://www.raptorsupplies.com/p/remco/bench-brushes-medium")',
        'eve_115_fasteners_grid': 'eve_115_fasteners_grid("https://www.raptorsupplies.com/c/fasteners/p/steel-zinc-plated-rectangle-miscellaneous-key-stocks")',
        'eve_115_fasteners_default': 'eve_115_fasteners_default("https://www.raptorsupplies.com/c/fasteners/p/steel-zinc-plated-square-miscellaneous-key-stocks")',

        'eve_347_fasteners_grid': 'eve_347_fasteners_grid("https://www.raptorsupplies.com/c/fasteners/p/grade-18-8-stainless-steel-plain-oversized-miscellaneous-key-stocks")',
        'eve_347_fasteners_default': 'eve_347_fasteners_default("https://www.raptorsupplies.com/c/fasteners/p/blue-ruspert-steel-hex-slotted-concrete-anchor-screws")',

        'eve_360_product': 'eve_360_product("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_360_category': 'eve_360_category("https://www.raptorsupplies.com/c/abrasive-mandrels")',
        'eve_360_brand': 'eve_360_brand("https://www.raptorsupplies.com/b")',
        'eve_360_l1': 'eve_360_l1("https://www.raptorsupplies.com/l1/abrasives")',
        'eve_360_l2': 'eve_360_l2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_360_bfc': 'eve_360_bfc("https://www.raptorsupplies.com/c/respirator-accessories/3m")',
        'eve_360_mother': 'eve_360_mother("https://www.raptorsupplies.com/p/norton/mandrel-assembly")',

        'eve_361_home': 'eve_361_home("https://www.raptorsupplies.com/")',
        'eve_361_l2': 'eve_361_l2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_361_brand': 'eve_361_brand("https://www.raptorsupplies.com/b/3m")',
        'eve_361_mother': 'eve_361_mother("https://www.raptorsupplies.com/p/norton/backup-pad")',
        'eve_361_grainger': 'eve_361_grainger("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_361_l3': 'eve_361_l3("https://www.raptorsupplies.com/c/abrasive-mandrels")',
        'eve_361_desktop': 'eve_361_desktop("https://www.raptorsupplies.com/pd/norton/66261059422")',
        'eve_361_mobile': 'eve_361_mobile("https://www.raptorsupplies.com/pd/norton/66261059422")',
        'eve_361_myaccount': 'eve_361_myaccount("https://www.raptorsupplies.com/customer/account/")',

        'eve_362_home': 'eve_362_home("https://www.raptorsupplies.com/")',
        'eve_362_l2': 'eve_362_l2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_362_brand': 'eve_362_brand("https://www.raptorsupplies.com/b")',
        'eve_362_mother': 'eve_362_mother("https://www.raptorsupplies.com/p/norton/backup-pad")',
        'eve_362_grainger': 'eve_362_grainger("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_362_l3': 'eve_362_l3("https://www.raptorsupplies.com/c/abrasive-mandrels")',
        'eve_362_desktop': 'eve_362_desktop("https://www.raptorsupplies.com/pd/norton/66261059422")',
        'eve_362_mobile': 'eve_362_mobile("https://www.raptorsupplies.com/pd/norton/66261059422")',

        'eve_15_home': 'eve_15_home("https://www.raptorsupplies.com/")',
        'eve_15_l2': 'eve_15_l2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_15_brand': 'eve_15_brand("https://www.raptorsupplies.com/b/3m")',
        'eve_15_mother': 'eve_15_mother("https://www.raptorsupplies.com/p/norton/mandrel-assembly")',

        'eve_15_l3': 'eve_15_l3("https://www.raptorsupplies.com/c/abrasive-mandrels")',
        'eve_15_pd': 'eve_15_pd("https://www.raptorsupplies.com/pd/norton/66261059422")',


        'eve_6_home': 'eve_6_home("https://www.raptorsupplies.com/s/no-results?q=asdfghjklsdfgh")',
        'eve_6_L2': 'eve_6_L2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_6_brand': 'eve_6_brand("https://www.raptorsupplies.com/customer/account/")',
        'eve_6_mother': 'eve_6_mother("https://www.raptorsupplies.com/b/3m")',
        'eve_6_grainger': 'eve_6_grainger("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_6_L3': 'eve_6_L3("https://www.raptorsupplies.com/c/adhesives")',
        'eve_6_product_desk': 'eve_6_product_desk("https://www.raptorsupplies.com/pd/climax-metal/w-25x")',
       

        'eve_7_home': 'eve_7_home("https://www.raptorsupplies.com/")',
        'eve_7_L2': 'eve_7_L2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_7_brand': 'eve_7_brand("https://www.raptorsupplies.com/b/3m")',
        'eve_7_mother': 'eve_7_mother("https://www.raptorsupplies.com/p/approved-vendor/corner-brace")',
        'eve_7_grainger': 'eve_7_grainger("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_7_L3': 'eve_7_L3("https://www.raptorsupplies.com/c/adhesives")',
        'eve_7_product_desk': 'eve_7_product_desk("https://www.raptorsupplies.com/pd/climax-metal/w-25x")',


        'eve_8_home': 'eve_8_home("https://www.raptorsupplies.com/")',
        'eve_8_L2': 'eve_8_L2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_8_brand': 'eve_8_brand("https://www.raptorsupplies.com/b/3m")',
        'eve_8_mother': 'eve_8_mother("https://www.raptorsupplies.com/p/approved-vendor/corner-brace")',
        'eve_8_grainger': 'eve_8_grainger("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_8_L3': 'eve_8_L3("https://www.raptorsupplies.com/c/adhesives")',
        'eve_8_product_desk': 'eve_8_product_desk("https://www.raptorsupplies.com/pd/climax-metal/w-25x")',


        'eve_5_home': 'eve_5_home("https://www.raptorsupplies.com/")',
        'eve_5_L2': 'eve_5_L2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_5_brand': 'eve_5_brand("https://www.raptorsupplies.com/b/3m")',
        'eve_5_mother': 'eve_5_mother("https://www.raptorsupplies.com/p/approved-vendor/corner-brace")',
        'eve_5_L3': 'eve_5_L3("https://www.raptorsupplies.com/c/adhesives")',
        'eve_5_product_desk': 'eve_5_product_desk("https://www.raptorsupplies.com/pd/climax-metal/w-25x")',

        'eve_73_fasteners': 'eve_73_fasteners("https://www.raptorsupplies.com/c/fasteners/p/1-4-20-coarse-plain-nylon-hex-head-cap-screws")',



        'eve_402_brand': 'eve_402_brand("https://www.raptorsupplies.com/b/char-lynn")',
        'eve_402_l3_default': 'eve_402_l3_default("https://www.raptorsupplies.com/c/microwave-ovens")',
        'eve_402_l4_default': 'eve_402_l4_default("https://www.raptorsupplies.com/c/fasteners/c3/drop-in-anchors")',
        'eve_402_mother_fastner': 'eve_402_mother_fastner("https://www.raptorsupplies.com/c/fasteners/p/640-lbs-capacity-drop-in-anchors")',
        'eve_402_mother_nonfastner': 'eve_402_mother_nonfastner("https://www.raptorsupplies.com/p/cementex-usa/electrical-insulating-roll-blankets")',
        'eve_402_desktop_pd': 'eve_402_desktop_pd("https://www.raptorsupplies.com/pd/vulcan-hart/720431")',

        'eve_12_home': 'eve_12_home("https://www.raptorsupplies.com/")',
        'eve_12_l2': 'eve_12_l2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_12_brand': 'eve_12_brand("https://www.raptorsupplies.com/b/3m")',
        'eve_12_mother': 'eve_12_mother("https://www.raptorsupplies.com/p/ps-doors/ladder-safety-gate-adapter-brackets")',
        'eve_12_grainger': 'eve_12_grainger("https://www.raptorsupplies.com/ww-grainger-dealer")',
        'eve_12_l3': 'eve_12_l3("https://www.raptorsupplies.com/c/brackets")',
        'eve_12_desktop_pd': 'eve_12_desktop_pd("https://www.raptorsupplies.com/pd/dap/18898")',


        'eve_98_brandlist': 'eve_98_brandlist("https://www.raptorsupplies.com/b/d")',
        'eve_98_signin': 'eve_98_signin("https://www.raptorsupplies.com/login")',
        'eve_98_grainger': 'eve_98_grainger("https://www.raptorsupplies.com/ww-grainger-dealer")',

        'eve_99_brandlist': 'eve_99_brandlist("https://www.raptorsupplies.com/b/d")',
        'eve_99_signin': 'eve_99_signin("https://www.raptorsupplies.com/login")',
        'eve_99_grainger': 'eve_99_grainger("https://www.raptorsupplies.com/ww-grainger-dealer")',

        'eve_100_brandlist': 'eve_100_brandlist("https://www.raptorsupplies.com/b/d")',
        'eve_100_signin': 'eve_100_signin("https://www.raptorsupplies.com/login")',
        'eve_100_grainger': 'eve_100_grainger("https://www.raptorsupplies.com/ww-grainger-dealer")',

        'eve_96_homepage': 'eve_96_homepage("https://www.raptorsupplies.com/")',
        'eve_96_product': 'eve_96_product("https://www.raptorsupplies.com/pd/lovejoy/68514411512")',

        'eve_94_l1': 'eve_94_l1("https://www.raptorsupplies.com/l1/abrasives")',
        'eve_94_l2': 'eve_94_l2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_94_l3': 'eve_94_l3("https://www.raptorsupplies.com/c/abrasive-mandrels")',
        'eve_94_mother': 'eve_94_mother("https://www.raptorsupplies.com/p/merit/bore-polisher-extension-mandrel")',

        'eve_90_P1': 'eve_90_P1("https://www.raptorsupplies.com/p1/akro-mils/30080-series-shelf-bin")',
        'eve_90_product': 'eve_90_product("https://www.raptorsupplies.com/pd/merit/08834183163")',
        'eve_90_mother': 'eve_90_mother("https://www.raptorsupplies.com/p/merit/specialty-abrasive-mandrels")',
        'eve_90_Fasteners_L4': 'eve_90_Fasteners_L4("https://www.raptorsupplies.com/c/fasteners/c4/carbon-steel-threaded-rods")',
        'eve_90_BFC': 'eve_90_BFC("https://www.raptorsupplies.com/c/abrasive-mandrels?cat=83&catKey=466441")',
        'eve_90_L3': 'eve_90_L3("https://www.raptorsupplies.com/c/abrasive-mandrels")',
        'eve_90_L2': 'eve_90_L2("https://www.raptorsupplies.com/l2/abrasive-accessories")',
        'eve_90_L1': 'eve_90_L1("https://www.raptorsupplies.com/l1/abrasives")',
        'eve_90_home': 'eve_90_home("https://www.raptorsupplies.com/")',
        'eve_90_brand':'eve_90_brand("https://www.raptorsupplies.com/b/allegro-safety")',

    }

    testing = RawEventsTesting()
    # keys = list(program_dict.keys())
    # start_index = 270
    # for i, key in enumerate(keys[start_index:], start_index):
    #     print(i, ">>>>>>>>>>> Working Template >    >>>>>>>>", key), eval(f"testing.{program_dict[key]}")
    #     time.sleep(5)
    for key in keys_to_run:
        if key in program_dict:
            print(">>>>>>>>>>> Working Template >>>>>>>>>", key)
            eval(f"testing.{program_dict[key]}")

    testing.driver_quit()


# keys_to_run = ["eve_360_l2"]

# keys_to_run = ["eve_72_nonfastener_listtview","eve_72_nonfastener_gridview","eve_72_nonfastener_defaultview"]
# keys_to_run = ["eve_66_L2","eve_66_L3","eve_66_mother"]
keys_to_run = ["eve_360_l2"]
run_program()





