
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
 
class Item:
    pass

itens = []

def buscaDados():

    try:

        url = "http://pedidos.embramaco.com.br/export/pedidos/index.php"

        # print("URL=>", url)
        # print("Buscando ", cidade)

        driver.get(url)
        driver.implicitly_wait(5)

        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # driver.implicitly_wait(5)

        print("Page title=>", driver.title)

        element = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[2]/input")
        element.send_keys("abc")
        driver.implicitly_wait(1)

        element = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td[2]/input")
        element.send_keys("123")
        driver.implicitly_wait(1)

        element = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[5]/td[2]/input")
        element.click()
        # driver.implicitly_wait(5)
        time.sleep(5)

        print("1. Page title=>", driver.current_url)


        # url = "http://pedidos.embramaco.com.br/export/pedidos/topo.php?id_cia=2&lang=pt"
        # url = "http://pedidos.embramaco.com.br/export/relatorios/frames_relat.php?id_cia=2"
        url = "http://pedidos.embramaco.com.br/export/relatorios/format_rel.php?id_cia=2&nome_rel=../relatorios/rel_estoque.php&mostra=Relat%C3%B3rio%20de%20Estoque&opcoes=4&lang=pt&ped_aux="
        driver.get(url)
        # driver.implicitly_wait(5)
        time.sleep(5)

        print("2. Page title=>", driver.current_url)

        # driver.find_element_by_name("continuar") #("/html/body/form/table/tbody/tr[2]/td[8]/input")
        # print("1")
        driver.execute_script("document.getElementsByName('continuar')[0].click()")

        # element.click()
        # print("2")
        # driver.implicitly_wait(5)
        time.sleep(5)
        # print("3")
        driver.switch_to.window(driver.window_handles[1])

        time.sleep(30)

        print("3. Page title=>", driver.current_url)

        element = driver.find_element_by_xpath("/html/body/table[2]")
        print(element)

        print("1")
        trs = element.find_elements_by_tag_name("tr")
        print("2")

        cont = 0

        for tr in trs:

            cont = cont + 1
            if cont <= 2:
                continue
            
            # ths = tr.find_elements_by_tag_name("th")
            # for th in ths:
            #     text = th.text.strip()
            #     print(text)

            tds = tr.find_elements_by_tag_name("td")

            if len(tds) != 8:
                continue

            col = 0
            item = Item()
            for td in tds:
                text = td.text.strip()
                col = col+1
                if col == 1:
                    item.codigo = text
                elif col == 2:
                    item.produto = text
                elif col == 3:
                    item.linha = text
                elif col == 4:
                    item.ref = text
                elif col == 5:
                    item.lote = text
                elif col == 6:
                    item.saldoCdi = text
                elif col == 7:
                    item.saldoEmbramaco = text
                elif col == 8:
                    item.programacao = text
            itens.append(item)
            # if cont == 10:
            #     break


        # url = "http://pedidos.embramaco.com.br/export/relatorios/rel_estoque.php"
        #        http://pedidos.embramaco.com.br/export/relatorios/rel_estoque.php&mostra=Relat%C3%B3rio%20de%20Estoque&opcoes=4&lang=pt&ped_aux=
                
        # driver.get(url)
        # time.sleep(25)

        # element = driver.find_element_by_xpath("/html")
        # html_content = element.get_attribute('outerHTML')
        # print(html_content)

        # tds = driver.find_elements_by_tag_name("table")
        # print(tds)

        # el = driver.find_element_by_name("menu")
        # for option in el.find_elements_by_tag_name('option'):
        #     print(option)
            # if option.text in labels:
            #     option.click()

        # select = driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/select[value='../relatorios/rel_estoque.php']")

        # select = driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/select")

        # /html/body/form/table/tbody/tr/td[3]/select

        # /html/body/form/table/tbody/tr/td[3]/select
        # driver.implicitly_wait(1)

        # # my_select.select_by_index(2)
        # select.click()
        # driver.implicitly_wait(1)

        # print("2. Page title=>", driver.current_url)
        
        # element = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[8]/input")
        # print(element)


        # element = driver.find_element_by_xpath("/html/body/section/section/div/div/div/div/div/div[1]/form/div/label[2]")
        # driver.execute_script("arguments[0].click();", element)
        # driver.implicitly_wait(1)

        # _div = driver.find_element_by_xpath("/html/body/section/section/div/div/div/div/div/div[2]/form/div[2]")
        # driver.implicitly_wait(1)
        # _input = _div.find_element_by_css_selector('input')
        # placeholder = _input.get_attribute("placeholder")
        # # print('Placeholder: ', placeholder)

        # # print("Element is visible? " + str(_input.is_displayed()))

        # _input.send_keys(cidade)

        # # print("digitou cidade")

        # driver.implicitly_wait(1)
          
        # botao = driver.find_element_by_xpath("/html/body/section/section/div/div/div/div/div/div[2]/form/div[2]/button")

        # driver.execute_script("arguments[0].click();", botao)

        # # print("clicou")

        # element = WebDriverWait(driver, 10).until(
        #          EC.presence_of_element_located((By.XPATH, "/html/body/section/section/div/div/div/div/div/div[2]/div[2]/ul/li[1]"))
        #             )

        # # print("aguardou")

        # driver.implicitly_wait(1)

        # ul = driver.find_elements_by_xpath("/html/body/section/section/div/div/div/div/div/div[2]/div[2]/ul/li")
        # # ul = driver.find_element_by_xpath("/html/body/section/section/div/div/div/div/div/div[2]/div[2]/ul")
        # # print("ul", ul)
        # for li in ul:
        #     # print("content", li)
        #     strong = li.find_element_by_tag_name('strong')
        #     # print("->", strong.text.strip())
        #     dados = strong.text.strip() + "|"
        #     spans = li.find_elements_by_tag_name('span')
        #     for span in spans:
        #         # print("->", span.text.strip())
        #         dados += span.text.strip() + "|"

        #     # print("================")
        #     save_file(dados, _file)

    except Exception as e:
        print("ERROR:", e)

try:
    driver = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options)
    buscaDados()
    json = json.dumps([ob.__dict__ for ob in itens])
    save_file(json, "/home/ubuntu/python/scrap/embramaco.json")

except Exception as e:
    print("ERROR:", e)
finally:
    driver.close()
    driver.quit()


