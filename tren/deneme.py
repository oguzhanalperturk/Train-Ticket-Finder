seatNum = "9c"

all_seats = []
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

    elif "c" in seatNum:
        sideSeat = seatNum[:-1]
        sideSeat = sideSeat + "d"

    elif "d" in seatNum:
        sideSeat = seatNum[:-1]
        sideSeat = sideSeat + "c"

















