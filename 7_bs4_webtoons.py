import requests
from bs4 import BeautifulSoup

# url = "https://comic.naver.com/webtoon/weekday"
url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# cartoons = soup.find_all("a", attrs={"class":"title"})
# for cartoon in cartoons:
#     print(cartoon.get_text())

# cartoons = soup.find_all("td", attrs={"class":"title"})
# print(cartoons[0].a.get_text())
# print("https://comic.naver.com" + cartoons[0].a["href"])

# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

total = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text() 
    print(rate)
    total += float(rate)
    print(total)

average = total / len(cartoons)
print(total)
print(len(cartoons))
print(average)