import requests
from bs4 import BeautifulSoup   #导入bs4

url = 'http://www.bjsubway.com/station/zjgls/'
html = requests.get(url).content  # 获取首页的html
soup = BeautifulSoup(html, 'lxml')  # 得到soup对象

stationDistance = {}
citys = []
city_setcions = []
num = len(soup.select('.line_place > div > table > tbody > tr > th'))
for i in range(1,num):
    station_raw = soup.select('.line_place > div > table > tbody > tr > th')[i]
    station = str(station_raw).replace('<th>','').replace('</th>','')
    if(len(station)==0):
        continue
    distance_raw = soup.select('.line_place > div > table > tbody > tr > td:nth-child(2)')[i]
    distance = int(str(distance_raw).replace('<td>','').replace('</td>',''))

    if(station.__contains__('――')):
        a = station.split('――')
    elif(station.__contains__('——')):
        a = station.split('——')
    station_A = a[0]
    station_B = a[1]
    if not citys.__contains__(station_A):
        citys.append(station_A)
    if not citys.__contains__(station_B):
        citys.append(station_B)

    if stationDistance.get(station).__bool__() is False:
        stationDistance[station] = distance

    if not city_setcions.__contains__(station):
        city_setcions.append(station)

print('_______________________RESULT:')
print(stationDistance)
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print(citys)
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print(city_setcions)








