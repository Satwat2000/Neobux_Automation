from cv2 import cvtColor, imread, COLOR_BGR2RGB
from os import system
from urllib import request

class Read_Capta:
    
    def __init__(self, browser):
        self.browser = browser                          #-----------> FInding Path of Download
        
    def read(self):
        from cv2 import cvtColor, imread, COLOR_BGR2RGB
        from os import system
        from urllib import request
        from tkinter import Tk, Label, Entry, Button, StringVar
        import PIL.Image, PIL.ImageTk
    
        print("Extracting img tags")
        images = self.browser.find_elements_by_tag_name('img')   #-----------> Find img tags form the source
        img = images[0].get_attribute('src')            #---------------> Find source of the found img tag
    
        data = request.urlretrieve(img)
        path = data[0]
        print("Downloading image")