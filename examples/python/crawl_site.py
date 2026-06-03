#!/usr/bin/env python3
import argparse
import time
from collections import deque
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("url")
parser.add_argument("--max-pages", type=int, default=10)
parser.add_argument("--depth", type=int, default=1)
parser.add_argument("--delay", type=float, default=1.0)
args = parser.parse_args()

start_host = urlparse(args.url).netloc
queue = deque([(args.url, 0)])
seen = set()
headers = {"User-Agent": "ResearchStarterBot/1.0"}

while queue and len(seen) < args.max_pages:
    url, depth = queue.popleft()
    if url in seen or urlparse(url).netloc != start_host:
        continue
    seen.add(url)
    print(f"[{len(seen)}] {url}")

    try:
        resp = requests.get(url, headers=headers, timeout=20)
        resp.raise_for_status()
    except Exception as exc:
        print(f"  error: {exc}")
        continue

    if depth >= args.depth:
        continue

    soup = BeautifulSoup(resp.text, "html.parser")
    for a in soup.find_all("a", href=True):
        link = urljoin(url, a["href"].split("#")[0])
        if urlparse(link).netloc == start_host and link not in seen:
            queue.append((link, depth + 1))

    time.sleep(args.delay)
