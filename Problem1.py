import pandas as pd

def hammimgDist(name,city):
    count = 0
    for i in range(len(name)):
        if (name[i] != city[i]):
            count+=1
    return count

def minDist(name,citylist,cityID):
    mindist = 9999999
    mincity = ""
    for city in citylist:
        if(len(city) == len(name)):
            dist = hammimgDist(name,city)
            if(dist < mindist):
                mindist = dist
                
                mincity = city
    return mincity

df1 = pd.read_csv("/Users/nikhildattatraya.c/Downloads/SaleskenProblemSolving-master/Correct_cities.csv")

CountryCity = {}
CityID = {}
for index, row in df1.iterrows():
    if row['country'] in CountryCity:
        CountryCity[row['country']].append(row['name'])
    else:
        CountryCity[row['country']] = []
        CountryCity[row['country']].append(row['name'])
    if not row['name'] in CityID:
        CityID[row['name']] = row['id']

df2 = pd.read_csv("/Users/nikhildattatraya.c/Downloads/SaleskenProblemSolving-master/Misspelt_cities.csv")

for index, row in df2.iterrows():
    id = minDist(row['misspelt_name'],CountryCity[row['country']],CityID)
    if(row['country'] == "India"):
        print(row['misspelt_name']+" , "+id+" , "+str(CityID[id]))
