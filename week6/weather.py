#3 gun arka arkaya 20 derecenin altinda oldu mu olmadi mi 

weather = []

weather.append([1, 19.0])
weather.append([2, 23.5])
weather.append([3, 25.6])
weather.append([4, 20.1])
weather.append([5, 19.1])
weather.append([6, 18.6])
weather.append([7, 25.6])

criteria = 21.0

def goodweather(mylist, criteria):
    amount = 0 
    for i in range(len(mylist)):
        for degree in mylist:
            if degree[1] < criteria and amount < 3:
                amount = 0
            else:
                amount += 1
    if amount >= 3:
        return True
    return False

print(goodweather(weather, criteria))


'''
criteria  = 25.0

def goodweather(mylist, criteria): #3 gun ust uste kriterini olcmez
    amount = 0 
    for degree in mylist:
        if degree[1] > criteria:
            amount += 1
    if amount >= 3:
        return True
    else:
        return False

print(goodweather(weather, criteria))
'''


'''
criteria = 25.0

def is_weather_good(mylist, criteria):
    for i in range(len(mylist)):
        if (mylist[i-1][1] > criteria) and (mylist[i][1] > criteria) and (mylist[i+1][1] > criteria):
            return True
    return False

print(is_weather_good(weather, criteria))
'''




