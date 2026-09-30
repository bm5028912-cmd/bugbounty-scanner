import requests
url = input("JS URL: ")
js = requests.get(url, timeout=10).text
print(js[:1000])
if "slice" in js:
    print("\n[!] Found slice - check manually")
