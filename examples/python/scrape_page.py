#!/usr/bin/env python3
import sys
import requests
import trafilatura
from bs4 import BeautifulSoup

url = sys.argv[1] if len(sys.argv) > 1 else None
if not url:
    print("Usage: python scrape_page.py <url>")
    sys.exit(1)

headers = {"User-Agent": "ResearchStarterBot/1.0 (+https://github.com/bcain2121/scraping-deep-research-starter)"}
resp = requests.get(url, headers=headers, timeout=20)
resp.raise_for_status()

text = trafilatura.extract(resp.text, url=url)
if not text:
    soup = BeautifulSoup(resp.text, "html.parser")
    text = soup.get_text("\n", strip=True)

print(text)
