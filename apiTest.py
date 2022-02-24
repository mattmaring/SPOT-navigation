'''
Spot mongo database API test.  Gets locations, currently -> {"document":{"_id":1,"name":"Davis"}}
'''
AUTH = ""
url = "https://data.mongodb-api.com/app/data-fpnfy/endpoint/data/beta/action/findOne"

import requests
import json

payload = json.dumps({
    "collection": "location",
    "database": "spot",
    "dataSource": "SpotData",
    "projection": {
        "_id": 1,
        "name": 1
    }
})
headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': AUTH
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
