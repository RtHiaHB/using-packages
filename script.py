import pprint
import requests
from matplotlib import pyplot as plt
from datetime import datetime


pp = pprint.PrettyPrinter(indent=2)
API_URL = 'https://api.weather.gov/gridpoints/RAH/75,57/forecast'
r = requests.get(API_URL)
response = r.json()

# pp.pprint(response)

forecast_list = response['properties']['periods']
# pp.pprint(forecast_list)
today = datetime.now().strftime("%Y-%m-%d")
# print(today)

to_graph={} #The empty dictionary to store our shaped data
count = 1 # AA global iterator to track each day past current datetime

for day in forecast_list:
    current_date = day['startTime'][0:13]
    count += 1

    to_graph[current_date] = day['windSpeed'].split()[0]

# print(to_graph)
plt.xlabel('DateTime')
plt.ylabel('Wind Speed (mph)')
plt.scatter(to_graph.keys(), to_graph.values())
plt.xticks(rotation = 45)
plt.show()
