import requests
import json
import os

url = "https://webexapis.com/v1/messages"
token = os.environ[WEBEX_TEAMS_ACCESS_TOKEN]
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vYzg2ZjljMDAtNTY5Yi0xMWVjLThjNmUtYjE2MmM5MjUxYmVl"

payload = {
  "roomId": room_id,
  "text": "hi from Postman"
}

data = json.dumps(payload) 
#comvierte de python a json, linea anterior

headers = {
  "Authorization": "Bearer " + token,
  "Content-Type": "application/json"
}
# response para comunicarse con cualquier API 
response = requests.post(url, headers=headers, data=data)

print(response.text)