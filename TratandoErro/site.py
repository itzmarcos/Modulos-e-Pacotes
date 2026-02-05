import requests

def site_online(url):
    try:
        r = requests.get(url, timeout=5)
        return r.status_code == 200
    except requests.RequestException:
        return False
    
if site_online("https://google.com"):
    print("Site online")
else:
    print("Site fora do ar")

