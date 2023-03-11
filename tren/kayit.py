"""
url = "https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf"
response = requests.get(url)
html_code = response.content


soup = BeautifulSoup(html_code, 'html.parser')
print(soup.prettify())


-----------------------------------

browser = webdriver.Chrome(executable_path=r"C:\Users\Oguzhan\Desktop\tren\chromedriver_win32\chromedriver.exe")
browser.get("https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf")
time.sleep(2)

nereden = browser.find_element("name",'nereden')
nereden.send_keys("Eskişehir")

nereye = browser.find_element("name",'nereye')
nereye.send_keys("Ankara Gar")

araButton = browser.find_element("name","btnSeferSorgula")
araButton.click()

time.sleep(1)
"""
