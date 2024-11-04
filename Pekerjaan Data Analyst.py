import re 
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

pointer=0
dataulti = {
    "Pekerjaan":[],
    "Perusahaan":[],
    "Lokasi":[],
    "Gaji":[],
    "Link":[]
    }

driver_path = r"D:\Setelah Kuliah\Belajar\Belajar Data Science\Scraping\edgedriver_win64\msedgedriver.exe"
service = webdriver.EdgeService(driver_path)
options = webdriver.EdgeOptions()

browser = webdriver.Edge(options=options,service=service)
browser.get("https://id.jobstreet.com/id/data-analyst-jobs")

xpathpekerjaan = '//h3[@class="a3yfdf0 _5xlhbl4z _2s7o740 _2s7o743 _2s7o7421 _1708b944 _2s7o74a"]'
listpekerjaan = browser.find_elements(By.XPATH, xpathpekerjaan)

xpathnamapt = '//a[@class="a3yfdf0 a3yfdff  a3yfdf0 a3yfdff cpaqq50 cpaqq51"]'
listnamapt = browser.find_elements(By.XPATH, xpathnamapt)

xpathlokasi = '//div[@class="a3yfdf0"]/span[@class="a3yfdf0 _5xlhbl4z _2s7o740 _2s7o741 _2s7o7421 _1708b944 _2s7o747"]'
listlokasi = browser.find_elements(By.XPATH, xpathlokasi)

xpathgaji = '//article/div[@class="a3yfdf0 _5xlhbl5b _5xlhblhf _5xlhbl6v"]/div[3]'
listgaji = browser.find_elements(By.XPATH, xpathgaji)

xpathlink = '//div[@class="a3yfdf0 _5xlhbl4z _5xlhbl4x"]/a[@href]'
listlink = browser.find_elements(By.XPATH,xpathlink)

for gaji in listgaji:
    try:
        gaji = gaji.find_element(By.XPATH,'./div[@aria-label]')
        gaji = gaji.text
    except:
        gaji = None
    pekerjaan = listpekerjaan[pointer].text
    perusahaan = listnamapt[pointer].text
    lokasi = listlokasi[pointer].text
    link = listlink[pointer].get_attribute('href')
    
    dataulti['Gaji'].append(gaji)
    dataulti['Link'].append(link)
    dataulti['Lokasi'].append(lokasi)
    dataulti['Pekerjaan'].append(pekerjaan)
    dataulti['Perusahaan'].append(perusahaan)
    print(pointer)
    print(pekerjaan)
    pointer+=1
    
pd.DataFrame(dataulti).to_csv('Pekerjaan Data Analyst.csv')
print('\n Done Scrapping')



