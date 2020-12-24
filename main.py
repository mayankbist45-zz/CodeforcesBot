from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

PATH = "/home/blackhawk/tools/webdriver/chrome/chromedriver"

chrome_options = webdriver.ChromeOptions()
# uncomment line below to hide the class tab
# chrome_options.headless = True
driver = webdriver.Chrome(PATH, options=chrome_options)


def select(id, val):
    select = Select(driver.find_element_by_id(id))
    select.select_by_value(val)


driver.get("https://codeforces.com/contest/1463/status")

select('frameProblemIndex', 'A')
select('verdictName', 'OK')
select('programTypeForInvoker', 'cpp.g++14')
driver.find_element_by_xpath('//input[@value="Apply"]').click()
driver.find_element_by_xpath('//input[@value="BY_ARRIVED_DESC"]').click()

getLimit = 9
ct = 1010

for page in range(getLimit, 0, -1):
    driver.get("https://codeforces.com/contest/1463/status/page/" + str(page) + "?order=BY_JUDGED_DESC")

    val = driver.find_elements_by_xpath('//a[@title="Source"]')
    if page != 1:
        for ele in val:
            ct += 1
            print(ele.get_attribute('href'))
            temp = webdriver.Chrome(PATH, options=chrome_options)
            temp.get(ele.get_attribute('href'))
            code = temp.find_element_by_id("program-source-text").text

            name = 'codes/file' + str(ct) + '.cpp'
            f = open(name, "a")
            f.write("//" + ele.get_attribute('submissionid') + '\n')
            f.write(code)
            f.close()
            temp.close()
    # print(ct)
    # print(val)
driver.close()
