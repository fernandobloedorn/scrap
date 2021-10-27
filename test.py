
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json, requests
from utils import strip_accents
from utils import retrieve_date_time
from utils import save_file
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--remote-debugging-port=9222") 
chrome_options.add_argument("start-maximized"); 
chrome_options.add_argument("disable-infobars");
chrome_options.add_argument("--disable-extensions");
chrome_options.add_argument("--disable-gpu"); 
 
def buscaDados():

    try:

        url = "http://pedidos.embramaco.com.br/export/pedidos/index.php"

        # print("URL=>", url)
        # print("Buscando ", cidade)

        driver.get(url)
        driver.implicitly_wait(5)
        print("Page title=>", driver.title)


    except Exception as e:
        print("ERROR:", e)

try:
    driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
    buscaDados()

except Exception as e:
    print("ERROR:", e)
finally:
    driver.close()
    driver.quit()


