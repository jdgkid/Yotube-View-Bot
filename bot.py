import time;
from selenium import webdriver;

#time to refresh page like tf
Timer = 3 #(3seconds)

#youtube link
link = 'YOUTUBE_LINK_HERE'

#number of views
views = 10

driver = webdriver.Chrome()
driver.get(link)

for i in range(views)
time.sleep(Timer)