
import os, sys
import time, json, process
from datetime import datetime
from selenium import webdriver as webd
from tkinter import messagebox
from tkinter import Tk, Button, Entry, Label, StringVar
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Path and File Wirte Setup
#-------------------------

"""Directory name && Parent Directory path"""

path = os.path.join(os.getcwd(), "Records")

"""Accessing the Record sving space"""
try:
    os.mkdir(path)
except OSError:
    print("Welcome Again...!!")


"""Accing file"""
file_name =  os.path.join(path, str(datetime.date(datetime.now())))
f = open(file_name, 'a')
print(f)
orig_stdout = sys.stdout #store orignality
sys.stdout = f           #chnge stdout

"""Adding Time Stamps"""
timestamp = datetime.now().strftime("%H:%M:%S")
print("opened again")
print("########## Accissing neobux on ", str(timestamp), " ##########")
print()


# Assign the variables
g = open('config.json','r')
data = json.load(g)
if data['username'] == "" or data['password'] == '' or data['username'] == None or data['password'] == None:
    g.close()
    get = process.fetch()
    name,passwd = get.info()
    print(name)
    print(passwd)
    with open('config.json', 'w') as g:
        data = {'username':name, 'password':passwd}
        json.dump(data, g)
    userstr = name
    passstr = passwd

else:
    userstr = data['username']
    passstr = data['password']
    print("Usename and Pass Assigned")
    g.close()

if userstr != "" and passstr != '' and userstr != None and passstr != None:
        # Open the webpage
    try:
        browser = webd.Chrome(executable_path ='Chrome\chromedriver.exe')
        browser.get(("https://www.neobux.com/m/l/?vl=5051E0515DBCDC20"))
    except Exception as e:
        print(e)
        process.chromeErr()
        sys.stdout = orig_stdout  #Restore stdout functionality
        f.close()
        window = process.fetch()
        window.closeit(file_name)
        exit(0)
        


    print("Entered in Normal Mode")
    print()
    try:
        element = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID, 'dCfd1')))
        print("-----LOGIN PAGE LOADED-----")
    except TimeoutException:
        print ("Login Page TIme Out!!")
        messagebox.showwarning("LOGIN","Login Page TIme Out!! \n   OR \nTurn OFf Your VPN")
        browser.quit()
    #call login
    browser.get_screenshot_as_file("Records/img/br1.png")


    """
    Login into Page

    """###################### Download the Capta #####################"""
    def input_capt():
        from urllib import request
        print("Extracting img tags")
        images = browser.find_elements_by_tag_name('img')   #-----------> Find img tags form the source
        img = images[0].get_attribute('src')            #---------------> Find source of the found img tag
        data = request.urlretrieve(img)
        path = data[0]
        print("Downloading image")
        get = process.fetch()
        return get.capta(path)


    # Fill login data & Login
    print()
    #-----------------------
    """Input Usename"""
    username = browser.find_element_by_id("Kf1")
    username.send_keys(userstr)
    print("----Username Filled----")

    """Input Password"""
    passw = browser.find_element_by_id("Kf2")
    passw.send_keys(passstr)
    print("----Password Provided----")

    """Find capta (can throw error)"""
    try:
        capt = browser.find_element_by_id("Kf3")
        if(capt):
            capt.click()    #Check if its clicking
            print("Capta Found---*****:")
            Cap = input_capt()
            capt.send_keys((Cap).upper())
            print("\tCapte Entered Successfully")
    except Exception:
        print ("Capta Not Found")
        print(Exception)

    """Click login"""
    login = browser.find_element_by_id("botao_login")
    login.click()

    browser.get_screenshot_as_file("Records/img/br2.png")

    #Go to the Advertisement Viewing Page
    print()
    #------------------------------------
    """Wait for Home page to load"""
    try:
        element = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID, 't_upg_bt')))
        print("Home Page Loaded Successfully")
    except TimeoutException:
        print ("Home Page Time Out!!")       # Wait for Home page to load
        messagebox.showwarning("HOME","Home Page Time Out!!")

        browser.quit()

    """Open Add viewing page"""
    advertise = browser.find_element_by_id("navAds")
    time.sleep(2)
    advertise.click()
    print("----Page directed to Advertisement page")

    browser.get_screenshot_as_file("Records/img/br3.png")


    #Start viewing Advertisement
    print(" ")
    #---------------------------
    """Initial declerations"""
    id = 1
    #Declare regex for star and red_dots
    star_ = "icon_"
    red = "i"

    """Loop to view all Adds"""
    try:
        while(browser.find_element_by_id(star_+str(id))):
            print(id)
            try:
                star = browser.find_element_by_id(star_+str(id))
                star.click();
                print("----Adertisement "+str(id)+" Clicked")
                red_dot = browser.find_element_by_id(red + str(id))
                red_dot.click();
                browser.get_screenshot_as_file("Records/img/brr4.png")
                print("----Red Dot "+str(id)+"Clicked")
            except Exception:
                print("Id " +str(id)+ " Already Vesited")

            '''Wait for new tab to open'''
            try:
                time.sleep(2)
                browser.switch_to.window(browser.window_handles[1])
                element = WebDriverWait(browser, 17).until(EC.presence_of_element_located((By.CLASS_NAME, 'button small2 orange')))
                print("Viewing Advertisement "+id)
            except TimeoutException:
                print ("Viewing Advertisement "+str(id)+" ---->>Couldn't Find the Class element")
            '''Close the opend tab'''

            browser.get_screenshot_as_file("Records/img/brri.png")


            try:
                close_add = browser.find_element_by_class_name("button.small2.orange")
                close_add.click()
                print("0.001$ Added to your account -- closing tab")
            except Exception:
                print("Advertisement already visited  -- closing tab")
                browser.close()
            finally:
                browser.switch_to.window(browser.window_handles[0])

            id = id + 1
            print()
    except Exception:
        print("All Adds Are Viewed")
        sys.stdout = orig_stdout  #Restore stdout functionality
        f.close()                 #Closing the opend file
        browser.quit();
        window = process.fetch()
        window.closeit(file_name)

