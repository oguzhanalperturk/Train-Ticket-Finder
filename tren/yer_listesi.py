from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def reserveSeat(train_no, man_or_woman):

    sec_button_str = "mainTabView:gidisSeferTablosu:" + str(train_no) + ":j_idt117"

    WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.ID, sec_button_str)))

    sec_button = browser.find_element(By.ID, sec_button_str)

    sec_button.click()

    WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.ID, "mainTabView:btnDevam44")))

    devam_button = browser.find_element(By.ID, "mainTabView:btnDevam44")

    devam_button.click()

    WebDriverWait(browser, 100).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ui-wagon-slot-item")))

    all_seats = browser.find_elements(By.CLASS_NAME, "ui-wagon-slot-item")

    flag = 0
    for seat in all_seats:

        if (flag == 1):
            break

        images = seat.find_elements(By.TAG_NAME, "img")
        innerhtml = seat.get_attribute('innerHTML')

        if ("13485128303" not in innerhtml):
            if ("span" in innerhtml):
                if (len(images) == 1):
                    span = seat.find_element(By.TAG_NAME, "span")
                    seatNum = span.get_attribute('innerHTML')

                    WebDriverWait(browser, 100).until(
                        EC.presence_of_element_located((By.TAG_NAME, "input")))
                    checkbox = seat.find_element(By.TAG_NAME, "input")

                    if (int(seatNum) % 3 == 0):

                        checkbox.click()
                        WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.ID, "j_idt547")))

                        if (man_or_woman == "erkek"):
                            select_man = browser.find_element(By.ID, "j_idt547")
                            select_man.click()
                        else:
                            select_woman = browser.find_element(By.ID, "j_idt548")
                            select_woman.click()
                        flag = 1
                        break


                    elif (int(seatNum) % 2 == 1):

                        sideSeat = int(seatNum) + 1
                        for i in all_seats:
                            innerhtml_i = i.get_attribute('innerHTML')
                            images_i = i.find_elements(By.TAG_NAME, "img")

                            if ("13485128303" not in innerhtml_i):
                                if ("span" in innerhtml_i):
                                    checkseat = i.find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
                                    if (checkseat == str(sideSeat)):
                                        if man_or_woman in i.get_attribute('innerHTML') or len(images_i) == 1:
                                            checkbox.click()
                                            WebDriverWait(browser, 100).until(
                                                EC.element_to_be_clickable((By.ID, "j_idt547")))

                                            if (man_or_woman == "erkek"):
                                                select_man = browser.find_element(By.ID, "j_idt547")
                                                select_man.click()
                                            else:
                                                select_woman = browser.find_element(By.ID, "j_idt548")
                                                select_woman.click()
                                            flag = 1
                                            break

                    elif (int(seatNum) % 2 == 0):
                        sideSeat = int(seatNum) + -1
                        for i in all_seats:
                            innerhtml_i2 = i.get_attribute('innerHTML')
                            images_i2 = i.find_elements(By.TAG_NAME, "img")

                            if ("13485128303" not in innerhtml_i2):
                                if ("span" in innerhtml_i2):
                                    checkseat = i.find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
                                    if (checkseat == str(sideSeat)):
                                        if man_or_woman in i.get_attribute('innerHTML') or len(images_i2) == 1:
                                            checkbox.click()
                                            WebDriverWait(browser, 100).until(
                                                EC.element_to_be_clickable((By.ID, "j_idt547")))

                                            if (man_or_woman == "erkek"):
                                                select_man = browser.find_element(By.ID, "j_idt547")
                                                select_man.click()
                                            else:
                                                select_woman = browser.find_element(By.ID, "j_idt548")
                                                select_woman.click()
                                            flag = 1
                                            break







browser = webdriver.Chrome(executable_path=r"C:\Users\Oguzhan\Desktop\tren\chromedriver_win32\chromedriver.exe")
browser.get("https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf")


reserveSeat(1,"erkek")













while True:
    time.sleep(100)


time.sleep(1000)



