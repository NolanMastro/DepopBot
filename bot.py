import sys
import time
import shutil
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



username = sys.argv[1]
email = sys.argv[2]
password = sys.argv[3]

service = webdriver.ChromeService(executable_path = 'chromedriver.exe')
driver = webdriver.Chrome(service=service)

def login(username, email, password):
    
    
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

        time.sleep(1)

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div > div.sc-jTIIxJ.fFJNST > div.sc-fwdjwH.lgELAG > button.sc-hjcAab.bpwLYJ.sc-gshygS.fFJfAu"))#Accept cookies
        )
        element.click()
        time.sleep(3)

        print(f'Logged into {username}')

        
          
    except:
        print("Timed out on login page.")
        #add reset function that resets back to homepage.
    


def relist(driver):

    driver.get(f"https://www.depop.com/{username}/") 
    element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#main > div > div:nth-child(5) > div:nth-child(1) > div.styles_activeHeading__XHXh2 > span > p._text_bevez_41._shared_bevez_6._normal_bevez_51"))#Listing count
        )
    
    listing_count = ""
    for char in element.text.strip():
        if char.isdigit():
            listing_count+=char
    listing_count = int(listing_count)

    for i in range(1, listing_count+1):
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"#main > div > div:nth-child(5) > div:nth-child(1) > div.styles_container__yRMOx.styles_productListContainer__zwk_n > ol > li:nth-child({i}) > div > div > div.styles_productImageContainer__withoutHoverOverlay__oJusn.styles_baseProductImageContainer__4kInl > a > div.styles_overlay__rSQ3Y"))#Listing picture
        )

        element.click()

        image_count = 1

        while True:
            try:
                with open(f'{image_count}.png', 'wb') as file:
                    element = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, f'#main > div.styles__Layout-sc-b6f63023-2.IBnCu > div.styles__Desktop-sc-ae87dc0d-1.ijyefD > div:nth-child({image_count}) > img'))#Listing photos
                    )
                    url = element.get_attribute('src')
                    response = requests.get(url, stream=True)
                    print(f"{image_count}: "+response)
                    shutil.copyfileobj(response.raw, file)
                    print(f'Saved {url} successfuly.')
                del response
                image_count +=1
            except:
                break
        
        print('Done saving listing photos.')

                

                


#main > div.styles__Layout-sc-b6f63023-2.IBnCu > div.styles__Desktop-sc-ae87dc0d-1.ijyefD > div:nth-child(1) > img
#main > div.styles__Layout-sc-b6f63023-2.IBnCu > div.styles__Desktop-sc-ae87dc0d-1.ijyefD > div:nth-child(2) > img
    








if __name__ == "__main__":
    if len(sys.argv) == 4:
        login(username,email, password)
        relist(driver)
    else:
        print("Invalid number of arguments. Expected 3 arguments (username, email, password).")
