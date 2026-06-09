weather = []
with open ('D:\Data Science\python\DSA\Hashing Table\weather_data.csv','r') as f :
    for line in f : 
        elements = line.split (',')
        try:
            temperature = int (elements[1])
            weather.append(temperature)
        except:
            print ('exception occure , ignoring the temperature index')
f.close ()

print (weather)     
print(f"average temperature:\n {sum (weather[0:9])/len(weather[0:9])}")  

print (f"The maximum temperature in the list is : {max(weather)}")