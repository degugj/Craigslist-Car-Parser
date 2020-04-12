import carClass
import urllib
import SMS
import time
from bs4 import BeautifulSoup
import requests

# ----- FOR TESTING -----
# kbb url: https://www.kbb.com/honda/accord/2012/ex-sedan-4d/?vehicleid=366069&intent=buy-used&options=4615315%7ctrue%7c6514393%7cfalse%7c6514395%7cfalse%7c6514399%7cfalse%7c6514403%7cfalse%7c6514407%7ctrue%7c6514411%7cfalse%7c6514414%7cfalse%7c6869232%7cfalse&category=sedan&mileage=96226&pricetype=private-party&condition=very-good
# Honda Accord 201* EX; odo 90k; V6; Private Party Value = $9,701
# -----------------------

# Keep all same params, change price thres depending on year

# url to craislist page (enter any preliminary filters to craigslist)
url = 'https://boston.craigslist.org/search/cto?hasPic=1&search_distance=25&postal=01880&auto_make_model=honda+accord&max_auto_miles=95000&auto_cylinders=4&auto_title_status=1&auto_bodytype=8'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all('li', class_= 'result-row')

#print(posts) #to double check that I got a ResultSet
#print(len(posts)) #to double check I got 120 (elements/page)
print(" ----- Parsing Craigslist ----- ")
urlArr = []
isAlreadySent = 0
#while(1):
for i in range(len(posts)):
        isAlreadySent = 0
        postPrice = posts[i].a.text.strip()      #first post's price, .strip removes whitespace
        postDatetime = posts[i].find('time', class_='result-date')['datetime']      #datetime of listing
        postLink = posts[i].find('a', class_='result-title hdrlnk')['href']         #link to listing
        postTitle = posts[i].find('a', class_='result-title hdrlnk').text        #title of listing

        #for j in urlArr:
        #    if (j == postLink):
        #        isAlreadySent = 1
        #if(isAlreadySent == 0):
        SMS.send('\n'+postTitle + ' (List Price: ' + postPrice + ')\n' + postDatetime + '\n' + postLink)
        urlArr.append(postLink)
        time.sleep(5)
#print("Still Running")
#for i in range(0,len(posts)):
#    print(posts[i].a.text);

