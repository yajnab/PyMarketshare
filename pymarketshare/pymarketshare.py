#WebScrapping Yahoo Finance Portfolio page in Python for Educational Project
from selenium import webdriver
browser = webdriver.Firefox()  
browser.get('http://www.google.com') 
print (browser.title)
browser.quit()
