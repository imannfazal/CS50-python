import sys
import requests
import json

if len(sys.argv)<1:
    sys.exit()
respose = requests.get("https://itunes.apple.com/search?term=weezer&limit=10")

o = respose.json()
for track in o["results"]:
    print(track["trackCensoredName"])