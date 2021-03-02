# the main python file
import requests
import config



url = config.RESPONSE_URL
payload="{\"query\":\"{ \\n    viewer { \\n        name\\n    }\\n}\",\"variables\":{}}"

headers = {
  'Authorization': config.ACCESS_TOKEN,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response)
print(response.text)
