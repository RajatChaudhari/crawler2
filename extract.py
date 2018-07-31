from bs4 import BeautifulSoup
from selenium import webdriver
import re, datetime
import pandas as pd
import numpy as np

driver = webdriver.Chrome()
driver.get("http://google.co.in")

textbox=driver.find_element_by_id('lst-ib')
textbox.send_keys("Iceland Food , Jobs, slowdown, profit")
driver.find_element_by_name("btnK").click()
news=driver.find_elements_by_class_name("rc")

df=pd.DataFrame(columns=["Date","Link"])
links=[]
dates=[]
for new in news:
    try:
        links.append(new.find_element_by_css_selector('a').get_attribute('href'))
    except:
        links.append("no tag")
    try:
        span=new.find_element_by_css_selector('span.f')
        match = re.match('\w[A-Za-z]* \d[0-9]*, \d[0-9]*', span.text)
        dates.append(match.group())
    except:
        dates.append("no tag")
			
li = pd.Series(links)
dt= pd.Series(dates)
df.Date=dt.values
df.Link=li.values
df.to_csv("Iceland_core.csv",sep=',',encoding='utf-8')
driver.quit()