# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 17:19:02 2020

@author: Khaid Hoilett
"""

import time
import csv
import threading
import concurrent.futures
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import final


# Personal Customer Information
class Orders(object):
   
    def __init__(self):    
        self.name= ''
        self.email=''
        self.tel=''
        self.address=''
        self.postalcode=''
        self.city=''
        self.province=''
        self.country=''
        self.cctype=''
        self.ccnumber=''
        self.expiarymonth=''
        self.expiaryyear=''
        self.cvv=''
        self.item_type = ''
        self.item = ''
        self.FinalSize = ''
        self.Colour = ''
        self.Profile = ''
        self.Proxy = ''
        inst=final.GUI()
        self.Selektor= inst.Selektor
        self.count = 0
         
# Function that checkouts out items based on user input
    def Copper(self,item_type,item,Size,Colour,Profile):
       
# Assigns all profile information to respective variables    
        print(self.Profile)       
        
        infolist = []
        
        infolist=tuple(self.Profile.split(','))
        
        (self.name, self.email, self.tel, self.address, self.postalcode, self.city,  self.province, self.country, self.cctype, self.ccnumber, self.expiarymonth, self.expiaryyear, self.cvv) = infolist

# Making Chromedriver undetectable  and changing User Agent
       
        user_agent='Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
        chrome_options= Options()
        #chrome_options.add_argument('--proxy-server=%s' % self.Proxy)
        chrome_options.add_extension('C:\\Users\\Administrator\\Desktop\\extension_1_1_0_0.crx')
        chrome_options.add_argument("--disable-blink-features")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        
       
# Setting Path of chromedriver    
        chrome_path = ("C:\\Users\\Khaid Hoilett\\Desktop\\chromedriver.exe")
        driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)
       # driver.set_window_rect(x,y,w,h)
       
       
# This part of the code navigates to the Supreme shop all page            
        driver.get("https://www.supremenewyork.com/shop/all")    
        wait = WebDriverWait(driver,10)
       
# Saves the time that the selection and checkout process starts    
        begin_time=datetime.now()
# Waits for item type element to load and selects it from the main menu    
        i=2
       
        while True:
               
            i=i+1
            self.element3 = wait.until (EC.element_to_be_clickable((By.XPATH,'//*[@id="nav-categories"]/li[' + str(i) + ']/a')))
            Item_Type_Position = driver.find_element_by_xpath('//*[@id="nav-categories"]/li[' + str(i) + ']/a').text
           
            if  str(item_type.lower()) in str(Item_Type_Position.lower()):
                driver.find_element_by_xpath('//*[@id="nav-categories"]/li[' + str(i) + ']/a').click()
                break  
       
        while True:
            guide=0

           
# Waits for the item + colour combo the user selected to load and selects it
               
           
            self.element3 = wait.until (EC.element_to_be_clickable((By.XPATH,'//*[@id="container"]/li[1]/div/div[1]')))
               
            try:
                   
                Item_Position = driver.find_elements_by_class_name('name-link')

                count = len(Item_Position)

                for j in range (count):

                    k=Item_Position[j].text
                    colour_link=Item_Position[j+1].text

       
                           
                    if str(item.lower()) in str(k.lower()) and str(Colour.lower()) in str(colour_link.lower()) :
                        print (Item_Position[j])
                        Item_Position[j].click()
                        print('item selected')
                        guide = guide +1
                       
                        break
           
 
            except:
                    print('Item Not Dropped Yet')
                    driver.refresh()
                    pass
               
            if  guide > 0:
               
                break

# Waits for the drop down size menu to load and selects the correct size if applicable
       
        l=0
        Size_Selector=''
       
   
        try:
            self.elementx = wait.until (EC.element_to_be_clickable((By.XPATH,'//*[@id="s"]')))
           
            while True:
           
                l=l+1
           
                Size_Selector=driver.find_element_by_xpath('//*[@id="s"]/option['+str(l)+']').text
           
                if Size.lower() in Size_Selector.lower():
               
                    driver.find_element_by_xpath('//*[@id="s"]/option['+str(l)+']').click()
                   
                    break
   
       
        except:
            print('No Size Selection Required')
            pass
       
   
   
        self.element1 = wait.until (EC.element_to_be_clickable((By.XPATH,'//*[@id="add-remove-buttons"]/input')))
       
        driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
           
        self.element2 = wait.until (EC.element_to_be_clickable((By.XPATH,'//*[@id="cart"]/a[2]')))
   
   
        driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
   
   
   
   
# Drop down selection for country
        m= 0
        while True:
       
            m=m+1
   
            Country_Selector=driver.find_element_by_xpath('//*[@id="order_billing_country"]/option['+str(m)+']').text
       
            if Country_Selector == self.country:
         
                driver.find_element_by_xpath('//*[@id="order_billing_country"]/option['+str(m)+']').click()
           
                break
   
# Drop down selection for Province
        p=0
        while True:
       
            p=p+1
       
            Province_Selector=driver.find_element_by_xpath('//*[@id="order_billing_state"]/option['+str(p)+']').text
       
            if Province_Selector == self.province:
         
                driver.find_element_by_xpath('//*[@id="order_billing_state"]/option['+str(p)+']').click()
           
                break
   
   
# Drop down selection for CC month
        q=0
        while True:
       
            q=q+1
       
            cc_selector=driver.find_element_by_xpath('//*[@id="credit_card_month"]/option['+str(q)+']').text
       
            if cc_selector == self.expiarymonth:
         
                driver.find_element_by_xpath('//*[@id="credit_card_month"]/option['+str(q)+']').click()
           
                break
   
        driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(self.name)
        driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(self.email)
        driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(self.tel)
        driver.find_element_by_xpath('//*[@id="bo"]').send_keys(self.address)
        driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(self.postalcode)
        driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(self.city)
        Creditcard_field=driver.find_element_by_xpath('//*[@id="rnsnckrn"]')
        ActionChains(driver).move_to_element(Creditcard_field).click().key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(self.ccnumber).perform()
        driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()
        driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(self.cvv)
        driver.find_element_by_xpath('//*[@id="pay"]/input').click()  
       
        end_time= datetime.now()
        print(end_time - begin_time)
        time.sleep(9)    


def main (self): 
    
   SonnytheSupremeBot=Orders()
#  SonnytheSupremeBot.Ordertaker()
   SonnytheSupremeBot.Selektor=self.Selektor
   SonnytheSupremeBot.Count=len(self.Selektor)
   print(SonnytheSupremeBot.Selektor)
   Threads = []
   
  # self.Count=len(self.Selektor)
  # print(self.Count)

   
# A process is created for every item and joined to be ran simultaneously on multiple processors (multiprocessing)
        
        
   for i in range (0,SonnytheSupremeBot.Count-1,6):

       SonnytheSupremeBot.item_type= SonnytheSupremeBot.Selektor[i]
       SonnytheSupremeBot.item=SonnytheSupremeBot.Selektor[i+1]
       SonnytheSupremeBot.Size=SonnytheSupremeBot.Selektor[i+2]
       SonnytheSupremeBot.Colour=SonnytheSupremeBot.Selektor[i+3]
       SonnytheSupremeBot.Profile=SonnytheSupremeBot.Selektor[i+4]

       
   T=threading.Thread(target=SonnytheSupremeBot.Copper,args=(SonnytheSupremeBot.item_type,SonnytheSupremeBot.item,SonnytheSupremeBot.Size,SonnytheSupremeBot.Colour,SonnytheSupremeBot.Profile))
       
       
   T.start()
   Threads.append(T)           
   
   print(Threads)
       
   for Thread in Threads:
           
       Thread.join()
    
       
   
# A list with the users chosen items & item specs are stored from their prompted input
if __name__=="__main__":
       
    main()
