import os
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 



# options.add_Arguments("--disable-notifications")


current_dir = os.getcwd()
path = current_dir + '/chromedriver'
URL1 = 'https://www.facebook.com/letsgojp/?eid=ARCaqBTaDv5o1Hmo7YXT7oRuHeQmK8hfA20fG0SESMVa8gRoeNNQ7sE9HCqO_MOPWqPdIuQqYlbWPodF&fref=tag'
browser = webdriver.Chrome(executable_path=path) #填入chromedriver的路徑
browser.get(URL1)



# browser.find_element_by_css_selector('[name="email"]').send_keys('a0923850407@gmail.com') # 填入帳號
# browser.find_element_by_css_selector('#pass').send_keys('') # 填入密碼
# browser.find_element_by_css_selector('[type="submit"]').click() # 點選登入按鈕



for i in range(3):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)

# 在滑鼠不移動情況下，selenium打開的視窗裡，可以顯示幾篇動態牆文章？
soup = bs(browser.page_source, 'lxml')
# len(soup.select('.userContentWrapper'))

userContentWrapper = soup.select('div._1dwg._1w_m._q7o')
name = []
userContent = [] 
timestamp = [] 
link = []
for i in userContentWrapper:
    
    if i.select_one('.fwb.fcg'):
        name.append(i.select_one('.fwb.fcg').text)
    else:
        name.append('找不到Name')
    
    if i.select_one('div > p:nth-child(1)'):
        userContent.append(i.select_one('div > p:nth-child(1)').text)
    else:
        userContent.append('找不到userContent')
    
    if i.select_one('.timestampContent'):
        timestamp.append(i.select_one('.timestampContent').text)
    else:
        timestamp.append('找不到timestampContent')
        
    if i.select_one('._6m3._--6 a[href]'):
        link.append(i.select_one('._6m3._--6 a[href]').get('href'))
    else:
        link.append('找不到link')

browser.quit()            

df = pd.DataFrame({'link': link})
df = pd.DataFrame({'name':name,'content':userContent, 'time':timestamp, 'link': link})
df = df.drop_duplicates()
df