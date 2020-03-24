#!/usr/bin/env python3

# Import the modules 
import time
from selenium import webdriver as webd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.common.exceptions import TimeoutException

# Assign the variables
userstr = 'uzumaki420'
passstr = 'ska@734006'

# Open the webpage
browser = webd.Chrome(executable_path = 'C:\Chrome\chromedriver')
browser.get(("https://www.neobux.com/m/l/?vl=A8A244545EBEC902"))
try:
    element = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID, 'dCfd1')))
except TimeoutException:
    print ("Login Page TIme Out!!")
    browser.quit()

# Fill login data & Login
#-----------------------
"""Input Usename"""
username = browser.find_element_by_id("Kf1") 
username.send_keys(userstr)

"""Input Password"""
passw = browser.find_element_by_id("Kf2")    
passw.send_keys(passstr)

"""Find capta (can throw error)"""
try:
    capt = browser.find_element_by_id("Kf6")
    if(capt):
        capt.click()#Check if its clicking 
        time.sleep(10)
except Exception:
    print ("Capta not found !!")
    
"""Click login"""    
login = browser.find_element_by_id("botao_login")
login.click()


#Go to the Advertisement Viewing Page 
#------------------------------------
"""Wait for Home page to load"""
try:
    element = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID, 't_upg_bt')))
except TimeoutException:
    print ("Home Page Time Out!!")       # Wait for Home page to load
    browser.quit()

"""Open Add viewing page"""
advertise = browser.find_element_by_id("navAds")
advertise.click()

#Start viewing Advertisement
#---------------------------
"""Initial declerations"""
id = 14
#Declare regex for star and red_dots
star_ = "icon_"
red = "i"

"""Loop to view all Adds"""
try:
    while(browser.find_element_by_id(star_+str(id))):
        star = browser.find_element_by_id(star_+str(id))
        star.click();
        print("Adertisement "+id+" Clicked")
        red_dot = browser.find_element_by_id(red+str(id))
        red_dot.click();
        print("Red Dot "+str(id)+"Clicked")
        
        '''Wait for new tab to open'''
        try:
            time.sleep(2)
            browser.switch_to.window(browser.window_handles[1])
            element = WebDriverWait(browser, 17).until(EC.presence_of_element_located((By.CLASS_NAME, 'button small2 orange')))
            print("close")
        except TimeoutException:
            print ("Loading took too much time!")
        '''Close the opend tab'''
        try:
            close_add = browser.find_element_by_class_name("button.small2.orange")
            close_add.click()
            print("Tab closed")
        except Exception:
            print("Add "+ str(id) +" Already Visited")
            browser.close()
        finally:
            browser.switch_to.window(browser.window_handles[0])
            
        id = id + 1
        print(id)  
except Exception:
    print("All Adds Are Viewed")
    
        
