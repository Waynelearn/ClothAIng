from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

import shutil

def search_insta(hashtag):

    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", "Manjaro Linux")

    driver = webdriver.Firefox(profile)
    driver.get("https://instagram.com/explore/tags/"+hashtag)

    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'img')))

    img_list = driver.find_elements(By.TAG_NAME, "img")

    for i, img in enumerate(img_list):
        image_url = img.get_attribute("src")
        r = requests.get(image_url, stream = True)
        filename = f'instaPoster/pictures/original/image_{i}.jpeg'
        if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
                
            print('Image sucessfully Downloaded: ',filename)
        
        else:
            print('Image Couldn\'t be retreived')

if __name__=="__main__":
    search_insta("ootd")