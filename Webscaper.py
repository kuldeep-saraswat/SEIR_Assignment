import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Please enter a URL")
    sys.exit()
website= sys.argv[1]
page= requests.get(website,timeout=10)
data= BeautifulSoup(page.text,"html.parser")

print("Title:")
if data.title:
    print(data.title.string)
else:
    print("No title found")

print("\nBody Text:")
if data.body:
    print(data.body.get_text())
else:
    print("No body found")

print("\nLinks found:")
links = data.find_all("a")
for item in links:
    link = item.get("href")
    if link:
        print(link)