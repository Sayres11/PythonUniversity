import webbrowser
import requests

# przyklad działania:
# pageurl – pobrana strona, date-data w formacie rok miesiac dzien np. 20230126
# zapytanie do api:
# http://archive.org/wayback/available?url=example.com&timestamp=20060101
pageurl = 'https:github.com'
# pageurl = input("podaj adres strony")
# date = input("podaj date")
date = 20150101
url = "https://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(date)
response = requests.get(url)
d = response.json()
print(type(d))
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)
