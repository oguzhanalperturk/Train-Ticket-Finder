from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# ana ekrana geldiğinde bir süre sonra boş bırakıyor kutucukları, default doldurmayı bırakıyor.


def checkAvailability(start_time, end_time, dataList, selectedList):
    startTimeObj = datetime.strptime(start_time, '%H:%M')
    endTimeObj = datetime.strptime(end_time, '%H:%M')

    for data in dataList:
        if(data[0] >= startTimeObj and data[1] <= endTimeObj and data[3] != "Engelli" and int(data[3]) > 0):
            selectedList.append(data)

def reserveSeat(train_no, man_or_woman):

    sec_button_str = "mainTabView:gidisSeferTablosu:" + str(train_no) + ":j_idt117"

    WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.ID, sec_button_str)))

    sec_button = browser.find_element(By.ID, sec_button_str)

    sec_button.click()

    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, "mainTabView:btnDevam44")))

    WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.ID, "mainTabView:btnDevam44")))

    devam_button = browser.find_element(By.ID, "mainTabView:btnDevam44")

    devam_button.click()

    WebDriverWait(browser, 100).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ui-wagon-slot-item")))

    all_seats = browser.find_elements(By.CLASS_NAME, "ui-wagon-slot-item")

    seat_found_flag = 0
    flag = 0
    for seat in all_seats:

        if (flag == 1):
            break

        images = seat.find_elements(By.TAG_NAME, "img")
        innerhtml = seat.get_attribute('innerHTML')

        if (("13485128303" not in innerhtml) and ("13029825502" not in innerhtml)):
            if ("span" in innerhtml):
                if (len(images) == 1):
                    span = seat.find_element(By.TAG_NAME, "span")
                    seatNum = span.get_attribute('innerHTML')

                    WebDriverWait(browser, 100).until(
                        EC.presence_of_element_located((By.TAG_NAME, "input")))
                    checkbox = seat.find_element(By.TAG_NAME, "input")

                    letters = ["a","b","c","d"]

                    if any(x in seatNum for x in letters):

                        if "a" in seatNum:
                            sideSeat = seatNum[:-1]
                            sideSeat = sideSeat + "b"
                            for i in all_seats:
                                innerhtml_a = i.get_attribute('innerHTML')
                                images_a = i.find_elements(By.TAG_NAME, "img")

                                if (("13485128303" not in innerhtml_a) and ("13029825502" not in innerhtml_a)):
                                    if ("span" in innerhtml_a):
                                        checkseat = i.find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
                                        if (checkseat == str(sideSeat)):
                                            if man_or_woman in i.get_attribute('innerHTML') or len(images_a) == 1:
                                                checkbox.click()
                                                WebDriverWait(browser, 100).until(
                                                    EC.element_to_be_clickable((By.ID, "j_idt547")))
                                                seat_found_flag = 1

                                                if (man_or_woman == "erkek"):
                                                    select_man = browser.find_element(By.ID, "j_idt547")
                                                    select_man.click()
                                                else:
                                                    select_woman = browser.find_element(By.ID, "j_idt548")
                                                    select_woman.click()
                                                flag = 1
                                                break



                        elif "b" in seatNum:
                            sideSeat = seatNum[:-1]
                            sideSeat = sideSeat + "a"

                            for i in all_seats:
                                innerhtml_b = i.get_attribute('innerHTML')
                                images_b = i.find_elements(By.TAG_NAME, "img")

                                if (("13485128303" not in innerhtml_b) and ("13029825502" not in innerhtml_b)):
                                    if ("span" in innerhtml_b):
                                        checkseat = i.find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
                                        if (checkseat == str(sideSeat)):
                                            if man_or_woman in i.get_attribute('innerHTML') or len(images_b) == 1:
                                                checkbox.click()
                                                WebDriverWait(browser, 100).until(
                                                    EC.element_to_be_clickable((By.ID, "j_idt547")))
                                                seat_found_flag = 1

                                                if (man_or_woman == "erkek"):
                                                    select_man = browser.find_element(By.ID, "j_idt547")
                                                    select_man.click()
                                                else:
                                                    select_woman = browser.find_element(By.ID, "j_idt548")
                                                    select_woman.click()
                                                flag = 1
                                                break

                        elif "c" in seatNum:
                            sideSeat = seatNum[:-1]
                            sideSeat = sideSeat + "d"

                            for i in all_seats:
                                innerhtml_c = i.get_attribute('innerHTML')
                                images_c = i.find_elements(By.TAG_NAME, "img")

                                if (("13485128303" not in innerhtml_c) and ("13029825502" not in innerhtml_c)):
                                    if ("span" in innerhtml_c):
                                        checkseat = i.find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
                                        if (checkseat == str(sideSeat)):
                                            if man_or_woman in i.get_attribute('innerHTML') or len(images_c) == 1:
                                                checkbox.click()
                                                WebDriverWait(browser, 100).until(
                                                    EC.element_to_be_clickable((By.ID, "j_idt547")))
                                                seat_found_flag = 1

                                                if (man_or_woman == "erkek"):
                                                    select_man = browser.find_element(By.ID, "j_idt547")
                                                    select_man.click()
                                                else:
                                                    select_woman = browser.find_element(By.ID, "j_idt548")
                                                    select_woman.click()
                                                flag = 1
                                                break

                        elif "d" in seatNum:
                            sideSeat = seatNum[:-1]
                            sideSeat = sideSeat + "c"

                            for i in all_seats:
                                innerhtml_d = i.get_attribute('innerHTML')
                                images_d = i.find_elements(By.TAG_NAME, "img")

                                if (("13485128303" not in innerhtml_d) and ("13029825502" not in innerhtml_d)):
                                    if ("span" in innerhtml_d):
                                        checkseat = i.find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
                                        if (checkseat == str(sideSeat)):
                                            if man_or_woman in i.get_attribute('innerHTML') or len(images_d) == 1:
                                                checkbox.click()
                                                WebDriverWait(browser, 100).until(
                                                    EC.element_to_be_clickable((By.ID, "j_idt547")))
                                                seat_found_flag = 1

                                                if (man_or_woman == "erkek"):
                                                    select_man = browser.find_element(By.ID, "j_idt547")
                                                    select_man.click()
                                                else:
                                                    select_woman = browser.find_element(By.ID, "j_idt548")
                                                    select_woman.click()
                                                flag = 1
                                                break



                    else:
                        if (int(seatNum) % 3 == 0):

                            checkbox.click()
                            WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.ID, "j_idt547")))
                            seat_found_flag = 1

                            if (man_or_woman == "erkek"):
                                select_man = browser.find_element(By.ID, "j_idt547")
                                select_man.click()
                            else:
                                select_woman = browser.find_element(By.ID, "j_idt548")
                                select_woman.click()

                            break


                        elif (int(seatNum) % 2 == 1):

                            sideSeat = int(seatNum) + 1
                            for i in all_seats:
                                innerhtml_i = i.get_attribute('innerHTML')
                                images_i = i.find_elements(By.TAG_NAME, "img")

                                if (("13485128303" not in innerhtml_i) and ("13029825502" not in innerhtml_i)):
                                    if ("span" in innerhtml_i):
                                        checkseat = i.find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
                                        if (checkseat == str(sideSeat)):
                                            if man_or_woman in i.get_attribute('innerHTML') or len(images_i) == 1:
                                                checkbox.click()
                                                WebDriverWait(browser, 100).until(
                                                    EC.element_to_be_clickable((By.ID, "j_idt547")))
                                                seat_found_flag = 1

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

                                if (("13485128303" not in innerhtml_i2) and ("13029825502" not in innerhtml_i2)):
                                    if ("span" in innerhtml_i2):
                                        checkseat = i.find_element(By.TAG_NAME, "span").get_attribute('innerHTML')
                                        if (checkseat == str(sideSeat)):
                                            if man_or_woman in i.get_attribute('innerHTML') or len(images_i2) == 1:
                                                checkbox.click()
                                                WebDriverWait(browser, 100).until(
                                                    EC.element_to_be_clickable((By.ID, "j_idt547")))
                                                seat_found_flag = 1

                                                if (man_or_woman == "erkek"):
                                                    select_man = browser.find_element(By.ID, "j_idt547")
                                                    select_man.click()
                                                else:
                                                    select_woman = browser.find_element(By.ID, "j_idt548")
                                                    select_woman.click()
                                                flag = 1
                                                break
        if(seat_found_flag == 1):
            break

    if(seat_found_flag == 0):
        browser.get("https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf")
        WebDriverWait(browser, 100).until(
            EC.element_to_be_clickable((By.NAME, "btnSeferSorgula")))
        araButton = browser.find_element("name", "btnSeferSorgula")
        araButton.click()

    return seat_found_flag



browser = webdriver.Chrome(executable_path=r"C:\Users\Oguzhan\Desktop\tren\chromedriver_win32\chromedriver.exe")
browser.get("https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf")

WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.NAME, "mainTabView:btnSonrakiGunGidis")))
WebDriverWait(browser, 100).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ui-selectonemenu-label")))
WebDriverWait(browser, 100).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "seferSorguTableBuyuk")))


loopCount = 1
seat_found_f = 0
while True:

    seatInfo = browser.find_elements(By.CLASS_NAME, "ui-selectonemenu-label")
    dept_time = browser.find_elements(By.CLASS_NAME, "seferSorguTableBuyuk")


    alldata = []


    index = 0
    train_no = 0
    for seat in seatInfo:
        if(index+2 > len(dept_time) ):
            break
        temp = []
        temp.append(datetime.strptime(dept_time[index].text, '%H:%M'))
        index+=1
        temp.append(datetime.strptime(dept_time[index].text, '%H:%M'))
        index += 1
        temp.append(dept_time[index].text)
        index += 1
        seatnum = seat.text.split(" ")
        if(len(seatnum) > 3):
            seatnum = seatnum[-2].strip()
            if seatnum != "Engelli":
                seatnum = int(seatnum.replace("(", "").strip())

            temp.append(seatnum)
            temp.append(train_no)
            train_no += 1
        alldata.append(temp)


    availableList = []
    start_time = "10:00"
    end_time = "17:59"
    checkAvailability(start_time, end_time, alldata, availableList)

    print("----- CHECK " + str(loopCount) + " ----------")
    print("")

    if(len(availableList) > 0):
        count = 1
        for available in availableList:
            print(str(count) + "-) " + str(available[0].time()) + " - "  + str(available[1].time()) + " :  " + str(int(available[3])) + " seats available")
            count += 1
            seat_found_f = reserveSeat(int(available[4]), "erkek")

            if(seat_found_f == 1):
                while True:
                    pass
    else:
        print("There is not any available seats in that interval : " + start_time + " - " + end_time)

    print("")
    print("-------------------------------------------")
    print("")
    loopCount += 1

    time.sleep(1)
    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.NAME, "mainTabView:btnSonrakiGunGidis")))
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.NAME, "mainTabView:btnSonrakiGunGidis")))
    time.sleep(1)
    nextPageButton = browser.find_element("name", "mainTabView:btnSonrakiGunGidis")
    nextPageButton.click()
    time.sleep(15)
    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.NAME, "mainTabView:btnOncekiGunGidis")))
    WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.NAME, "mainTabView:btnOncekiGunGidis")))
    previousPageButton = browser.find_element("name", "mainTabView:btnOncekiGunGidis")
    previousPageButton.click()
    time.sleep(15)

time.sleep(5)
browser.close()





