# использует образец JSON, выводит группы, занятия и количество занятий 
import json
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

