import time
from datetime import datetime
import json
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import http
import getpass

 ##side > div.uwk68 > div > label > div > div._13NKt.copyable-text.selectable-text
class WhatsAppElements:
    search = (By.CSS_SELECTOR, "#side > div.uwk68 > div > label > div > div._13NKt.copyable-text.selectable-text")
 
class WhatsApp:
    init_time = datetime.now()
    browser =  None
    timeout = 100  # The timeout is set for about ten seconds
    def __init__(self, wait, screenshot=None, session=None):
        options = webdriver.ChromeOptions() 
        options.add_argument('--profile-directory=Default')
        options.add_argument('--user-data-dir=C:/Temp/ChromeProfile')
        self.browser = webdriver.Chrome(executable_path=r'C:\Users\lenovo\Downloads\chromedriver_win32\chromedriver.exe', chrome_options=options)
        self.browser.get("https://web.whatsapp.com/") #to open the WhatsApp web
        self.browser.maximize_window()
        # you need to scan the QR code in here (to eliminate this step, I will publish another blog
        WebDriverWait(self.browser,3600).until( 
        EC.presence_of_element_located(WhatsAppElements.search)) #wait till search element appears
    
    def goto_main(self):
        try:
            self.browser.refresh()
            Alert(self.browser).accept()
        except Exception as e:
            print(e)
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
            WhatsAppElements.search))
 
    def unread_usernames(self):
        self.goto_main()
        initial = 50
        usernames = []
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        for k in soup.find_all("div", class_="_3Bc7H _20c87"):
            if k.find("div", class_="_3uIPm WYyr1"):
                username = k.find_all("div", class_="_2nY6U vq6sj _3C4Vf")
                if username:
                    for unread in username:
                        name = unread.find("div", class_="zoWT4")
                        msg = unread.find("div", class_="_37FrU")
                        usernames.append(name.text)
        initial += 1
        usernames = list(usernames)
        return usernames

    def get_last_message_for(self, name):
        messages = list()
        search = self.browser.find_element(*WhatsAppElements.search)
        search.send_keys(name+Keys.ENTER)
        time.sleep(3)
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        for i in soup.find_all("div", class_="message-in"):
            message = i.find("span", class_="selectable-text")
            if message:
                messages.append(message.text)
        messages = list(filter(None, messages))
        self.send_reply(name,messages[-1])
        return messages

    def send_reply(self,name, message):
        if message.lower() in ('hi', 'hello', 'hey'):
            msg = """Hi \n Please Provide Your customer id and service id."""
        else:
            msg = self.get_customer_id(message)
        wait = WebDriverWait(self.browser, 100)
        user = self.browser.find_element_by_xpath("//span[@title='{}']".format(name))
        user.click()
        text_box = self.browser.find_element_by_xpath("//footer/div/div/span/div/div/div/div/div[@title='{}']".format('Type a message'))
        #text_box = self.browser.find_element_by_class_name('_2vbn4')
        text_box.send_keys(msg)
        time.sleep(5)
        send_button = self.browser.find_element_by_xpath("//span[@data-icon='send']")
        send_button.click()
        time.sleep(5)
        return msg
    
    def get_customer_id(self, message):
        url = ''
        token = ''
        response = ''

        with open("config.json") as json_data_file:
            data_api = json.load(json_data_file)
        for k, v in data_api['api_custumer'].items():
            if k == 'url':
                url = v
            elif k == 'token':
                token = v
        CustomerID = None
        serviceid = [str(i) for i in message.split() if i.isdigit()]
        uri = url + token
        response = requests.get(uri)
        res_dict = response.json()
        if res_dict != None:
            customerid = res_dict['CustomerId']
            if customerid  in message:
                if len(serviceid) > 0:
                    response = self.get_service_data(serviceid)
                    msg = response
                elif customerid  in message and "YES" in message.upper():
                    msg = """Hello Manager will connect you after in few time."""
                else:
                    msg = """Hello Please Provide service id with customer id on same message. \n If you want connectwith manager please reply "YES and CustomerID". """
            
            else:
                msg = """Hello Your Customer id is not Valid please provide valid ID. """
        return msg

    def get_service_data(self, serviceid):
        url = ''
        token = ''
        response = ''

        with open("config.json") as json_data_file:
            data_api = json.load(json_data_file)
        for k, v in data_api['api_cred'].items():
            if k == 'url':
                url = v
            elif k == 'token':
                token = v
        CallId = None
        servicestatus = None
        for res in serviceid:
            uri = url + token + '/' + res
            response = requests.get(uri)
            res_dict = response.json()
            if res_dict != None:
                Status = res_dict['StatusCode']
                servicestatus = Status
                CallId = res_dict['CallId']
        if servicestatus == None:
            result = 'Hello Your service id not found.'
        else:
            result = 'Hi \n Your service order status is {} and Call Id is {}.'.format(servicestatus, CallId)
        return result
