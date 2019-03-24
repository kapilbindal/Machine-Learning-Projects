from selenium import webdriver

driver = webdriver.Chrome('C:/Users/KAPIL/Downloads/chromedriver.exe')
driver.get("https://web.whatsapp.com/")

name = input("Enter the name of the reciever : ")
msg = input("Enter the message to be delivered : ")
count = int(input("Enter the count: "))

input("Enter anything after scanning th QRCode")

user = driver.find_element_by_xpath('//span[@title  = "{}"]'.format(name))
user.click()

msgBox = driver.find_element_by_class_name("_2S1VP")
for i in range(count):
    msgBox.send_keys(msg)
    button = driver.find_element_by_class_name("_35EW6")
    button.click()

