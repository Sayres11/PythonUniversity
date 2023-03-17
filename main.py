import webbrowser
import requests

pageurl = 'https://github.com'
timestamps = ['20150101', '20140101', '20130101']

for timestamp in timestamps:
    url = "https://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + timestamp
    response = requests.get(url)
    d = response.json()
    page = d["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page)
