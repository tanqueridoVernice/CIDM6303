import requests
"""
Documentation at 
https://documenter.getpostman.com/view/10808728/SzS8rjbc
"""

# 1. get the API data from the web server
# This API server does not require an API key
# 2. Convert the data into a useful python objects: usually a list or dictionaries
url = "https://api.covid19api.com/summary"

response = requests.get(url)
# Convert the json object to a dictionary
result = response.json()


countries = result["Countries"]
total_deaths = 0
cases = 0

for country in countries:
    total_deaths += country["TotalDeaths"]
for country in countries:
    cases += country["TotalConfirmed"]
mortality = total_deaths/cases
print(f"Total Deaths: {total_deaths:,}")
print(f"Total Confirmed Cases: {cases:,}")
print(f"Mortality Rate: {mortality:.3f}")
