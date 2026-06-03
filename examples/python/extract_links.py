#!/usr/bin/env python3
import sys
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

url = sys.argv[1] if len(sys.argv) > 1 else None
if not url:
    print("Usage: python extract_links.py <url>")
    sys.exit(1)

headers = {"User-Agent": "ResearchStarterBot/1.0"}
html = requests.get(url, headers=headers, timeout=20).text
soup = BeautifulSoup(html, "html.parser")

seen = set()
for a in soup.find_all("a", href=True):
    link = urljoin(url, a["href"])
    if link not in seen:
        seen.add(link)
        print(link)
