from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# open firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# start
driver.get(r'https://data.ers.usda.gov/reports.aspx?ID=17829')

driver.find_element(By.XPATH, r'//*[@id="MainContentPlaceHolder_reportingServicesWrapper1_tbl_menu"]/tbody/tr/td[2]/div/div/p').click()
states = driver.find_elements(By.XPATH, r'//*[@id="MainContentPlaceHolder_reportingServicesWrapper1_tbl_menu"]/tbody/tr/td[2]/div/div/div/ul/li')

driver.find_element(By.XPATH, r'/html/body/form/div[4]/div/main/div/div/div/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr/td[4]/div/div/p').click()
education = driver.find_elements(By.XPATH, r'/html/body/form/div[4]/div/main/div/div/div/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr/td[4]/div/div/div/ul/li')

body = driver.find_element(By.TAG_NAME, 'body')
body.click()

for i in range(1, len(states)+1, 1):
    wait = WebDriverWait(driver, 30)
    # driver.find_element(By.XPATH, r'//*[@id="MainContentPlaceHolder_reportingServicesWrapper1_tbl_menu"]/tbody/tr/td[2]/div/div/p').click()
    dropdown1 = driver.find_element(By.XPATH, r'//*[@id="MainContentPlaceHolder_reportingServicesWrapper1_tbl_menu"]/tbody/tr/td[2]/div/div/p')
    driver.execute_script("arguments[0].scrollIntoView();", dropdown1)
    driver.execute_script("arguments[0].click();", dropdown1)

    # driver.find_element(By.XPATH, r'//*[@id="MainContentPlaceHolder_reportingServicesWrapper1_tbl_menu"]/tbody/tr/td[2]/div/div/div/ul/li['+str(2)+']').click()
    element1 = driver.find_element(By.XPATH, r'//*[@id="MainContentPlaceHolder_reportingServicesWrapper1_tbl_menu"]/tbody/tr/td[2]/div/div/div/ul/li['+str(i)+']')
    driver.execute_script("arguments[0].scrollIntoView();", element1)
    driver.execute_script("arguments[0].click();", element1)

    time.sleep(3)

    # driver.find_element(By.XPATH, r'//*[@id="MainContentPlaceHolder_reportingServicesWrapper1_ReportSubmitButton"]').click()
    submit1 = driver.find_element(By.XPATH, r'//*[@id="MainContentPlaceHolder_reportingServicesWrapper1_ReportSubmitButton"]')
    driver.execute_script("arguments[0].scrollIntoView();", submit1)
    driver.execute_script("arguments[0].click();", submit1)

    for j in range(1, len(education)+1, 1):
        wait = WebDriverWait(driver, 30)
        # driver.find_element(By.XPATH, r'/html/body/form/div[4]/div/main/div/div/div/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr/td[4]/div/div/p').click()
        dropdown = driver.find_element(By.XPATH, r'/html/body/form/div[4]/div/main/div/div/div/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr/td[4]/div/div/p')
        driver.execute_script("arguments[0].scrollIntoView();", dropdown)
        driver.execute_script("arguments[0].click();", dropdown)

        # driver.find_element(By.XPATH, r'/html/body/form/div[4]/div/main/div/div/div/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr/td[4]/div/div/div/ul/li['+str(j)+']').click()
        element = driver.find_element(By.XPATH, r'/html/body/form/div[4]/div/main/div/div/div/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr/td[4]/div/div/div/ul/li['+str(j)+']')
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.execute_script("arguments[0].click();", element)

        time.sleep(3)

        # driver.find_element(By.XPATH, r'//*[@id="MainContentPlaceHolder_reportingServicesWrapper1_ReportSubmitButton"]').click()
        submit = driver.find_element(By.XPATH, r'//*[@id="MainContentPlaceHolder_reportingServicesWrapper1_ReportSubmitButton"]')
        driver.execute_script("arguments[0].scrollIntoView();", submit)
        driver.execute_script("arguments[0].click();", submit)

        time.sleep(10)

        dropdown_locator = (By.XPATH, '//a[@title="Export drop down menu"]')
        wait = WebDriverWait(driver, 10)
        dropdown_element = wait.until(EC.element_to_be_clickable(dropdown_locator))
        driver.execute_script("arguments[0].scrollIntoView();", dropdown_element)
        dropdown_element.click()
        excel_button_locator = (By.XPATH, r'/html/body/form/div[4]/div/main/div/div/div/table/tbody/tr[2]/td/div/span/div/table/tbody/tr[3]/td/div/div/div[4]/table/tbody/tr/td/div[2]/div[1]/a')
        excel_button_element = wait.until(EC.element_to_be_clickable(excel_button_locator))
        driver.execute_script("arguments[0].click();", excel_button_element)

#takes like 30 min
driver.quit()

