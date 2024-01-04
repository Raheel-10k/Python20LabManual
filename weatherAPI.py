import requests
import json

api_key = '918e5c9c6f36588656bd2b19701a3044'

base_url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=4fd6cc6793bbdf879edd556a2b138547"

city=str(input("Enter city to search: "))

dict_para={'q':city, 'api':api_key}
response=requests.get(url=base_url, params=dict_para)

data=response.json()    #extraction of data

#print(data)    #USED to find where to extrapolate the data from.
print("Temperature: ",data['list'][0]['main']['temp'])
print("Pressure: ",data['list'][0]['main']['pressure'])
print("humidity: ",data['list'][0]['main']['humidity'])