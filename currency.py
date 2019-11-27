import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

filename = 'write_data.txt'

olddata = []
with open(filename,'r') as f: 
    lines = f.readlines() # 读取文本中所有内容，并保存在一个列表中，列表中每一个元素对应一行数据
    olddata = lines[-1].rstrip().split(',')
    oldtime = time.mktime(time.strptime(olddata[1], "%Y-%m-%d %H:%M:%S"))

html = urlopen("http://www.boc.cn/sourcedb/whpj/index.html").read().decode('utf-8')
soup = BeautifulSoup(html,"html.parser")
result = soup.find("td",text="日元")
myArray = []
for child in result.parent.children:
    if child.string != u"\n":
        myArray.append(child.string)
##获取myArray
price = myArray[3]
dt = myArray[6] +' '+ myArray[7]
##获取当前price和dt
##timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
newtime = time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S"))
newdata = [price,dt]



if oldtime < newtime:
    sdata = '\n'+price+','+dt
    with open(filename,'a') as f: # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        f.write(sdata)
    print('Last:',olddata)
    print('Now:',newdata)
    gap = int(newdata[0].replace('.', '')) - int(olddata[0].replace('.', ''))
    if gap > 0:
        print('Princing UP',gap/10000)
    elif gap < 0:
        print('Princing DOWN',gap/10000)
    else:
        print('NO CHANGE')

else:
    print('Price checked, no update!')
    print(newdata)











