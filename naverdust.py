from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
#pprint(html.text)

soup = bs(html.text,'html.parser')
#pprint(soup)

data1 = soup.find('div',{'class':'detail_box'})  #영역 추출
#pprint(data1)

data2 = data1.findAll('dd')      #data1내에 dd태그를 가진 코드 모두 추출
#pprint(data2[0])

find_dust = data2[0].find('span',{'class':'num'}).text  #0번째 인덱스 텍스트 값만 추출
print(find_dust)                              