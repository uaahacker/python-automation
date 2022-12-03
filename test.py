from time import sleep
from selenium import webdriver

username = "bc220415808"
password = "VUlms22fall@2"

url = "https://vulms.vu.edu.pk/"

driver = webdriver.Chrome("C:\chromedriver.exe")

driver.get(url)

driver.find_element_by_name("txtStudentID").send_keys(username)
driver.find_element_by_name("txtPassword").send_keys(password)

driver.find_element_by_name("ibtnLogin").click()

driver.find_element_by_id("MainContent_gvCourseList_imgInstructor_0").click()
sleep(3)
driver.find_element_by_id("m_accordion_2_item_1_head").click()
driver.find_element_by_link_text("Topic-001. Introduction to Computer Science").click()

sleep(10)
driver.find_element_by_id("tabHeader90993").click()
sleep(4)

driver.find_element_by_id("tabHeader184421").click()

driver.find_element_by_id("lnkTakeQuiz184421").click()

sleep(5)
driver.find_element_by_id("btnStartQuiz").click()

driver.find_element_by_name("btnReTakeQuiz").click()
driver.find_element_by_id("radioBtn1").click()

driver.find_element_by_name("btnSave").click()



