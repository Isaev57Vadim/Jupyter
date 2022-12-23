import requests
import xmltodict

url = "http://www.cbr.ru/scripts/xml_metall.asp?date_req1=01/07/2001&date_req2=13/07/2001"
response = requests.get(url)
data = xmltodict.parse(response.content)
print(data)

my_array = []
for item in data['Metall']['Record']:
    my_set = [item['@Date'], item['@Code'], item['Buy'], item['Sell']];
    my_array.append(my_set)
    print(my_set)

# - print(my_array)
