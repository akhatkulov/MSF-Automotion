import requests

url = "http://<metasploit_ip>:55553/api/v1/login"
data = {"username": "msf", "password": "toor"}
response = requests.post(url, json=data)
print(response.json())
