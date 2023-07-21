import requests

url = "https://api.similarweb.com/v1/similar-rank/https:/youtube.com/rank?api_key=fd710f9d69ba4ec98ca748579a7e4ccd"
response = requests.get(url)
print(response.text)


