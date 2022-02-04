from selenium import webdriver
import pandas as pd

url = 'https://www.youtube.com/c/EnglishClass101/videos?view=0&sort=p&flow=grid'

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.get(url)

videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
item_list = []
for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    uploaded_date = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
    #print(title,views,uploaded_date)
    items = {
        'title':title,
        'view':views,
        'uploaded_date':uploaded_date
    }
    item_list.append(items)

data = pd.DataFrame(item_list)
print(data)