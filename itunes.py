import sys
import requests

if len(sys.argv)<1:
    sys.exit()
respose = requests.get("https://itunes.apple.com/search?term=jack+johnson&limit=25")

print(respose.json())