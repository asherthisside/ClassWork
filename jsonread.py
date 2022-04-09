import json


countrylist = []
with open('countries.json') as f:
    data = json.load(f)
    # print(data)
    for i in data:
        # if i['Country'] == 'India':
        #     # print(i['Country'])
        #     print(i)
    #    print(i['Country'])
        countrylist.append(i['Country'])

countrylist.sort()
# print(countrylist)
for c in countrylist:
    print(c)

students = {
    "Shoaib" : {
        "name" : "Shoaib", 
        "Class" : 12, 
        "Attendace" : True, 
        "Favgames" : ['Battlefield2042', 'Football'],
    },
    "Akash" : {
        "name" : "Akash", 
        "Class" : 11, 
        "Attendace" : False, 
        "Favgames" : ['Cricket', 'COD'],
    },
    "Shruti" : {
        "name" : "Shruti", 
        "Class" : 8, 
        "Attendace" : True, 
        "Favgames" : ['Cricket', 'COD'],
    }
}

studentJSON = json.dumps(students)
fp = open('students.json', 'w')
fp.write(studentJSON)