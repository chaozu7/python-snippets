
import re


url = input("URL: ").strip()

#1
#username = re.sub(r"^(https|http)://(www\.)?twitter\.com/", "", url)
#print(f"Username: {username}")


#2
#username = url.replace("https://twitter.com", "")
#username = url.removeprefix("https://twitter.com")
#print(f"Username: {username}")


#3

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))