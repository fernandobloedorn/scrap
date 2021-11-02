import os
from selenium import webdriver
import json

from selenium.webdriver.chrome.webdriver import WebDriver
from utils import save_file
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from services.product_service import saveOrUpdate
from services.connection_service import getConnection
from models.product import Product
import util.float_util as floatUtil
import util.date_util as dateUtil

import time
from dotenv import load_dotenv

def getStocks(driver: WebDriver):

   products = []

   try:

      url = "http://pedidos.embramaco.com.br/export/pedidos/index.php"

      driver.get(url)
      driver.implicitly_wait(5)
      
      print("Page title=>", driver.title)

      element = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td[2]/input")
      element.send_keys(os.environ['EMBRAMACO_USER'])
      driver.implicitly_wait(1)

      element = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td[2]/input")
      element.send_keys(os.environ['EMBRAMACO_PASSWORD'])
      driver.implicitly_wait(1)

      element = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[5]/td[2]/input")
      element.click()
      
      time.sleep(5)

      print("1. Page title=>", driver.current_url)

      url = "http://pedidos.embramaco.com.br/export/relatorios/format_rel.php?id_cia=2&nome_rel=../relatorios/rel_estoque.php&mostra=Relat%C3%B3rio%20de%20Estoque&opcoes=4&lang=pt&ped_aux="
      driver.get(url)

      time.sleep(5)

      print("2. Page title=>", driver.current_url)
      
      driver.execute_script("document.getElementsByName('continuar')[0].click()")
      
      time.sleep(5)
      
      driver.switch_to.window(driver.window_handles[1])

      time.sleep(30)

      print("3. Page title=>", driver.current_url)

      element = driver.find_element(By.XPATH, "/html/body/table[2]")
      
      print(element)
      
      trs = element.find_elements(By.TAG_NAME, 'tr')
      
      print("Encontradas " + str(trs.__len__()) + ' trs...')
      
      cont = 0

      for tr in trs:
         
         if cont % 10 == 0:
            print("Processadas " + str(cont) + ' linhas...')
         
         cont = cont + 1
         if cont <= 2:
            continue

         if cont >= 30:
             break;
         
         tds = tr.find_elements(By.TAG_NAME, 'td')
         
         if len(tds) != 8:
            continue
         
         col = 0
         product = Product()
         
         for td in tds:
            text = td.text.strip()
            col = col + 1
            if col == 1:
               product.code = text
            elif col == 2:
               product.name = text
            elif col == 3:
               product.line = text
            elif col == 4:
               product.reference = text
            elif col == 5:
               product.lot = text
            elif col == 6:
               product.inventory_cdi = floatUtil.parse(text)
            elif col == 7:
               product.inventory_embramaco = floatUtil.parse(text)
            elif col == 8:
               print("Data:", text)
               product.programation = dateUtil.dateToString(dateUtil.parse(text))
         
         # print(text)

         print(product.code, product.name, "Data", product.programation)

         products.append(product)

         # print("Adiciou ", item.produto)
         
         
   except Exception as e:
      print("ERROR:", e)

   return products


load_dotenv()

driver = None

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--remote-debugging-port=9222") 

try:
   service = Service(os.environ['CHROME_DRIVER_PATH'])
   driver = webdriver.Chrome(service=service, options=chrome_options)
   products = getStocks(driver)
   # jsonData = json.dumps([ob.__dict__ for ob in itens])
   # save_file(jsonData, "estoque_embramaco2.json")
   saveOrUpdate(products)

except Exception as e:
   print("ERROR:", e)
finally:
   if driver is not None:
      driver.close()
      driver.quit()