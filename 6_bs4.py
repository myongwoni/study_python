import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attrs)
# print(soup.a["href"])

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# rank01 = soup.find("li", attrs={"class":"rank01"})
# print(rank01.a.get_text())
# print(rank01.next_sibling)
# print(rank01.next_sibling.next_sibling)

# rank02 = rank01.find_next_sibling("li")
# print(rank02.a.get_text())
# rank03 = rank02.find_next_sibling("li")
# print(rank03.a.get_text())
# rank02 = rank03.find_previous_sibling("li")
# print(rank02.a.get_text())

# print(rank01.find_next_siblings("li"))

webtoon = soup.find("a", text="불편한 관계-54화")
print(webtoon)