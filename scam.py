from time import sleep
from selenium import webdriver
import random

flname = ["tera bap","teri Maa","Teri Behan","Gandoaaaaaaa","loaaru"]
efname = ["teraBap23", "terimaa","lorulallit","lunlun","sattain",]
domainss = ["@madrchod.com","@chutiya.com","@sala.com","@gandu.com","@chakla.com","@randi.com"]
username = ["madrchod","terwwii","dsfsefsdf","dsfsfsd","sdfdsfds","sdfsfd","sdfsfsdfdf","dsgdsfdsfsd"]
password = ["gandoRANDIteriMAA","dsfsefsdf","dsfsfsd","sdfdsfds","sdfsfd","sdfsfsdfdf","dsgdsfdsfsd"]

emaill = "terimalun@harami.com"

url = "https://bdz-task.top/index.php?code=OTI2ODExMDgyNDB8fHBoZy10YXNrLnRvcHx8MzA0"

while(True):
    


    driver = webdriver.Chrome("E:\Python Projects\scam\chromedriver.exe")

    driver.get(url)
    driver.find_element_by_class_name("swal2-confirm").click()
    sleep(1)
    driver.find_element_by_id("fullname").send_keys(random.choice(flname))
    driver.find_element_by_id("username").send_keys(random.choice(username))
    driver.find_element_by_id("email").send_keys(f"{random.choice(efname)}{random.choice(domainss)}")
    driver.find_element_by_id("password").send_keys(random.choice(password))
    driver.find_element_by_id("password_confirmation").send_keys(random.choice(password))
    driver.find_element_by_id("customCheckRegister").click()
    sleep(1)
    driver.find_element_by_class_name("btn-primary").click()
