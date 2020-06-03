
import os
import sys
import time
import json
from datetime import datetime
from tkinter import messagebox
from tkinter import Tk, Button, Entry, Label, StringVar
from selenium import webdriver as webd
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

# Open the webpage
option = webd.ChromeOptions()
browser = webd.Chrome(executable_path ='C:\Chrome\chromedriver.exe')
browser.get(("https://www.neobux.com/m/l/?vl=5051E0515DBCDC20"))
print("Entered in Headless Mode")
print()
try:
    element = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID, 'dCfd1')))
    print("-----LOGIN PAGE LOADED-----")
except TimeoutException:
    print ("Login Page TIme Out!!")
    messagebox.showwarning("LOGIN","Login Page TIme Out!! \n   OR \nTurn OFf Your VPN")
    browser.quit()
#call login
browser.get_screenshot_as_file("img/br1.png")


"""
Login into Page

"""###################### Download the Capta #####################"""
def input_capt():
    from cv2 import cvtColor, imread, COLOR_BGR2RGB
    from os import system
    from urllib import request
    from tkinter import Tk, Label, Entry, Button, StringVar
    import PIL.Image, PIL.ImageTk

    print("Extracting img tags")
    images = browser.find_elements_by_tag_name('img')   #-----------> Find img tags form the source
    img = images[0].get_attribute('src')            #---------------> Find source of the found img tag

    data = request.urlretrieve(img)
    path = data[0]
    print("Downloading image")
    """ Import Modules"""

    """Config Background"""
    root = Tk()
    root.title("Type In The Captch")
    root.configure(background = "Yellow")

    """ Read image and Display it"""
    img = cvtColor(imread(path), COLOR_BGR2RGB)             #-------------> Read the saved capta using cv2
    photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(img))
    Label (root, image=photo, bg="black").pack()

    """ Add Input and Button"""

    Cap = StringVar(root, "", 'a')
    Label(root, text='Enter the Captca').pack()
    Entry(root, textvariable=Cap).pack()
    Button(root, text='Ok', command=root.destroy).pack()

    root.mainloop()
    system(f'rm {path}')
    return Cap



# Assign the variables
g = open('config.json','r')
data = json.load(g)
if data['username'] == "" or data['password'] == '':
    g.close()
    alert = Tk()
    alert.title('ALERT!!')
    name = StringVar(alert, "", 'a')
    passwd = StringVar(alert, "", 'b')
    Label(alert, text='Enter Usesrname').pack()
    Entry(alert, textvariable=name).pack()
    Label(alert, text='Enter Password').pack()
    Entry(alert, textvariable=passwd).pack()
    Button(alert, text='Ok', command=alert.destroy).pack()
    alert.mainloop()
    print(name.get())
    print(passwd.get())
    with open('config.json', 'w') as g:
        data = {'username':name.get(), 'password':passwd.get()}
        json.dump(data, g)
    userstr = name.get()
    passstr = passwd.get()

else:
    userstr = data['username']
    passstr = data['password']
    print("Usename and Pass Assigned")
    g.close()


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
        capt.send_keys((Cap.get()).upper())
        print("\tCapte Entered Successfully")
except Exception:
    print ("Capta Not Found")
    print(Exception)

"""Click login"""
login = browser.find_element_by_id("botao_login")
login.click()

browser.get_screenshot_as_file("img/br2.png")

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

browser.get_screenshot_as_file("img/br3.png")


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
            browser.get_screenshot_as_file("img/brr4.png")
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

        browser.get_screenshot_as_file("img/brri.png")


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
    messagebox.showinfo("HURRE...!!","All Adds Are Viewed")
    browser.quit();

sys.stdout = orig_stdout  #Restore stdout functionality
f.close()                 #Closing the opend file
