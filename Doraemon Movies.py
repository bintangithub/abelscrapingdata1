from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driverPath = r"D:\Setelah Kuliah\Belajar\Belajar Data Science\Scraping\edgedriver_win64\msedgedriver.exe"
edgeOptions = webdriver.EdgeOptions()
edgeService = webdriver.EdgeService(driverPath)
browser = webdriver.Edge(options=edgeOptions, service=edgeService)

# =============================================================================
# Mengakses Website
# =============================================================================

browser.get("https://doraemon.fandom.com/wiki/Doraemon_Wiki")

# //center/div/div[1]/div[1]/a

allMovies = browser.find_element(By.XPATH,"//center/div")
matches = allMovies.find_elements(By.XPATH,"div")
movies = []

for line in matches:
    # mengakses per line dari tabel movies doraemon
    # kemudian mengakses movie yang ada di dalamnya
    movieMatches = line.find_elements(By.XPATH,"div")
    for movieMatch in movieMatches:
        movie = movieMatch.find_element(By.XPATH,"a")
        movies.append(movie.get_attribute("title"))


# mencari tahun terbit di banyak negara
# search dahulu pada setiap nama film

searchMovieNameXPATH = '//header/div/div[3]/a[1]'
inputSearchMovieXPATH = '//form/input[@class="SearchInput-module_input__LhjJF search-input"]'
outputSearchMovieCSS = '//a[@data-testid="search-modal-result"]'
dateXPATH = '//div[@class="pi-item pi-data pi-item-spacing pi-border-color" and @data-source="Release date"]/div'
releaseDate = []
for movie in movies:
    element = browser.find_element(By.XPATH, searchMovieNameXPATH)
    element.click()
    browser.implicitly_wait(9)
    element = browser.find_element(By.XPATH, inputSearchMovieXPATH)
    element.send_keys(movie)
    element = browser.find_element(By.XPATH, outputSearchMovieCSS)
    element.click()
    element = browser.find_element(By.XPATH, dateXPATH)
    releaseDate.append(element.text)
    print(element.text)


pd.DataFrame({'Movie':movies,'Date':releaseDate}).to_csv('doraemon_movies.csv')
print("\n Scrapping Done")



