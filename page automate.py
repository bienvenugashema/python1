import requests

base_url = "https://69b83c91a6284ab923aa2d45a228325f.ctf.hacker101.com/page/edit/"
start = 1   # Starting page number
end = 100   # Change this to the range you want to test

for i in range(start, end + 1):
    url = f"{base_url}{i}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"✅ Valid page found: {url}")
    else:
        print(f"❌ Invalid page: {url} (Status: {response.status_code})")
