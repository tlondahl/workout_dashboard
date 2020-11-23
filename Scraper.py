from bs4 import BeautifulSoup
import pandas as pd
import requests
url = 'https://torokhtiy.com/blogs/warm-body-cold-mind/how-to-determine-your-pr'
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')

'/html/body/div[3]/main/div/article/div[1]/div[1]/div[1]/div[2]/p[17]'
'/html/body/div[3]/main/div/article/div[1]/div[1]/div[1]/div[2]/p[18]'
'/html/body/div[3]/main/div/article/div[1]/div[1]/div[1]/div[2]/p[28]'
'/html/body/div[3]/main/div/article/div[1]/div[1]/div[1]/div[2]/p[21]'

lift = []
percentage_min = []
percentage_max = []

for i, x in enumerate(range(17, 28)):
    if x == 21:
        continue
    text = soup.find_all('p')[x].text
    lift.append(text.split('-')[0])
    percentage_min.append(int((text.split('-')[1]))/100)
    percentage_max.append(int((text.split('-')[2]).split()[0]) / 100)

df = pd.DataFrame(list(zip(lift, percentage_min, percentage_max)), columns=['lift', 'percentage_min', 'percentage_max'])

df.to_csv('lifting_benchmarks.csv')