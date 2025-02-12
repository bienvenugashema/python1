import requests

# Base URL with placeholders
base_url = "https://static1.squarespace.com/static1/54e8ba93e4b07c3f655b452e/a/56c2a04520c64707756f4267/{}/"

# Range of numbers to test (modify as needed)
start = 1493764600000  # Adjust starting number
end = 1493764700000  # Adjust ending number
step = 100  # Step size to increment

for i in range(start, end, step):
    url = base_url.format(i)  # Insert number into URL
    response = requests.get(url)

    if response.status_code == 200:
        print(f"✅ Valid URL: {url}")
    else:
        print(f"❌ Invalid URL: {url} (Status: {response.status_code})")
