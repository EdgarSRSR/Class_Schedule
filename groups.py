import requests
#data={"id":'value',"actName":"value1","time":"value3","date":"value4","address":"value5","group":"value6"}
x = requests.get('http://localhost:8080/')
print(x.headers)
#print(x.text)
#print(x.json)
#print(x.cookies)
#resp = requests.post("http://localhost:8080/",data)
#print(resp.json)
#x = requests.get('http://localhost:8080/','activities')
#print(x.text)

#var req = new XMLHttpRequest();
#req.open('GET', 'http://localhost:8080/', false); 
#req.send(null);
#if (req.status == 200)
#  dump(req.responseText);
#session = requests.Session()
#response = session.get('http://localhost:8080/')
#print(session.cookies.get_dict())
#[{"id":1580020796345,"actName":"футбол","time":"13:00","date":"28.01.2020","address":"стадион","group":"а"},{"id":1580020833306,"actName":"английский","time":"12:00","date":"08.03.2020","address":"корпус 2","group":"а"},{"id":1580020871848,"actName":"программирование","time":"11:00","date":"25.01.2020","address":"корпус 2","group":"б"},{"id":1580020925084,"actName":"история","time":"10:00","date":"01.30.2020","address":"главный корпус","group":"б"}]
'''import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://localhost:8080"
html = urllib.request.urlopen(url, context=ctx).read()
page = BeautifulSoup(html, 'html.parser')
print(page)'''
# использует образец JSON, выводит группы, занятия и количество занятий 
'''import json
data = '[{"id":1580020796345,"className":"футбол","time":"13:00","date":"28.01.2020","address":"стадион","group":"а"},{"id":1580020833306,"className":"английский","time":"12:00","date":"08.03.2020","address":"корпус 2","group":"а"},{"id":1580020871848,"className":"программирование","time":"11:00","date":"25.01.2020","address":"корпус 2","group":"б"},{"id":1580020925084,"className":"история","time":"10:00","date":"01.30.2020","address":"главный корпус","group":"б"}]'

# превращает строку в список
data2 =data[1:]
data2 = data2[:-1]
value = data2.replace('},','};')
jsonlist = value.split(';')
print (jsonlist)
grouplist = []

#создает список с группами
for e in jsonlist:
    print(e)
    info = json.loads(e)
    if info['group'] not in grouplist:
        grouplist.append(info['group'])

# выводит группы, занятия и количество занятий
for e in grouplist:
    act = 0;
    activities = []
    for j in jsonlist:
        if json.loads(j)['group'] == e:
            act+=1;
            activities.append(json.loads(j)['className'])
    print("Группа: " + e + " количество занятий " + str(act) + " Имя Задании: "+ str(activities[:]))


'''

