import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driverPath = r"D:\Setelah Kuliah\Belajar\Belajar Data Science\Scraping\edgedriver_win64\msedgedriver.exe"
edgeOptions = webdriver.EdgeOptions()
edgeService = webdriver.EdgeService(driverPath)
browser = webdriver.Edge(options=edgeOptions, service=edgeService)

# =============================================================================
# Menuju Website Daftar Film Marvel
# =============================================================================

browser.get("https://kincir.com/movie/cinema/urutan-film-avengers-mulai-dari-mcu-pertama-hingga-fase-keempat-sV7uoEUSYDrdM/")

paragraphs = browser.find_elements(By.XPATH,"//p")
movies = []


for paragraph in paragraphs:
    movie = re.findall(r'\d+\.\s+[^\n]+', paragraph.text)
    try:
        movie = movie[0]
        print(movie)
        movies.append(movie)
    except:
        pass

pd.DataFrame(movies,columns=['Marvel Movies']).to_csv('marvel_movies.csv')
print("\n Scrapping Done")





















