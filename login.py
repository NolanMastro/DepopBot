import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def login(username, email, password):
    
    service = webdriver.ChromeService(executable_path = 'chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.depop.com/login/?withPassword=true")
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "username__input"))#Email field
        )
        element.send_keys(email)

        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password__input"))#Password field
        )
        element.send_keys(password)

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div.styles_loginOptionsContainer__JBHSf > div.styles_emailLoginOptionsContainer__UeY0k > form > button"))#Log in button
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div > div.sc-jTIIxJ.fFJNST > div.sc-fwdjwH.lgELAG > button.sc-hjcAab.bpwLYJ.sc-gshygS.fFJfAu"))#Accept cookies
        )
        element.click()

        
        
          
    except:
        print("Timed out on login page.")
        #add reset function that resets back to homepage.









if __name__ == "__main__":
    if len(sys.argv) == 4:
        login(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Invalid number of arguments. Expected 3 arguments (username, email, password).")
