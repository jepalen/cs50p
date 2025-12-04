import re

url = input("URL: ").strip()

# username = replace(url, "https://twitter.com/", "")
# username = removeprefix(url, "https://twitter.com/")
# username = re.sub(r"^(https?://)?(www\.)?//twitter\.com/", "", url)

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url,re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
else:
    print("Invalid URL")
