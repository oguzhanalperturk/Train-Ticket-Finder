from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



browser = webdriver.Chrome(executable_path=r"C:\Users\Oguzhan\Desktop\tren\chromedriver_win32\chromedriver.exe")
browser.get("https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf")

time.sleep(15)

train_no = 1
man_or_woman = "erkek"

sec_button_str = "mainTabView:gidisSeferTablosu:" + str(train_no) + ":j_idt117"

sec_button = browser.find_element(By.ID,sec_button_str)
sec_button.click()

time.sleep(15)

devam_button = browser.find_element(By.ID,"mainTabView:btnDevam44")

devam_button.click()

time.sleep(10)

all_seats = browser.find_elements(By.CLASS_NAME,"ui-wagon-slot-item")

seats_in_order = []
temp = []
count = 0
for seat in all_seats:
    images = seat.find_elements(By.TAG_NAME,"img")
    innerhtml = seat.get_attribute('innerHTML')

    if("13485128303" not in innerhtml):
        if("span" in innerhtml):
            temp.append(seat)
            count += 1
            if(count == 3):
                seats_in_order.append(temp)
                temp = []
                count = 0





for i in seats_in_order:
    print(i)
print(len(seats_in_order))






while True:
    time.sleep(100)


time.sleep(1000)



