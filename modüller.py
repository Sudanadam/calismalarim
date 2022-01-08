import requests
suc_URL = "https://data.police.uk/api/crimes-no-location"
payload = {
    "category" : "all-crime",
    "force" : "city-of-london",
    "date" : "2021-01"
}
response = requests.get(suc_URL, params=payload)
print(response.json())
 