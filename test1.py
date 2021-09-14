from bs4 import BeautifulSoup
import re
import xlwt

with open('test3.html','r',encoding='utf-8') as f :
    soup = BeautifulSoup(f.read(),'html.parser')

lilist = ['疫情地区','新增','现有','累计','治愈','死亡'] ##需要记录的数据

data = soup.findAll('tr',{'class':'VirusTable_1-1-315_3m6Ybq'})

workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('国内疫情各地区数据')
for num in range(6):
    worksheet.write(0,num,lilist[num])
for i in range(len(data)):
    i_str = str(data[i])
    i_area = re.findall('<span>(.*?)</span>',i_str)[0] #单个地区str
    worksheet.write(i+1,0,i_area) #在excel中写入地区
    i_num = re.findall('>(.*?)</td>',i_str)
    for u in range(1,6):
        worksheet.write(i+1,-u+6,i_num[-u]) #写入各类数据

workbook.save('国内疫情.csv')
