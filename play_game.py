from selenium import webdriver
import selenium.webdriver.common.keys as Keys
import time
import threading
from dinosaur import dinosaur
from capture import capture_feed
from network import ai_player
 
driver = webdriver.Chrome('/Users/owner/Desktop/all/tools/chromedriver')

# internet connection must be off
driver.get('http://www.google.com/')
time.sleep(2)

# main page to send key commands to
page = driver.find_element_by_class_name('offline')

# start game
page.send_keys(u'\ue00d')

# instance of dinosaur
dino = dinosaur.Dino(driver=driver)

# captures the dinosaur video feed

# controls the dinosaur
frame = 0
while True:
   ai_player.predict(page, frame) 
   frame += 1
