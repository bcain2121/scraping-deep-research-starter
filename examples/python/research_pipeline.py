#!/usr/bin/env python3
"""Simple research pipeline: Tavily discovery -> scrape top URLs -> source notes."""
import os
import sys
import requests
import trafilatura
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()
query = " ".join(sys.argv[1:]).strip()
if not query:
    print("Usage: python research_pipeline.py '<research question>'")
    sys.exit(1)

api_key = os.getenv("TAVILY_API_KEY")
if not api_key:
    print("Missing TAVILY_API_KEY. Copy .env.example to .env and add your key.")
    sys.exit(1)

client = TavilyClient(api_key=api_key)
results = client.search(query=query, search_depth="advanced", max_results=5).get("results", [])

print(f"# Research notes: {query}\n")
for result in results:
    url = result.get("url")
    title = result.get("title", url)
    print(f"## {title}\n{url}\n")
    try:
        html = requests.get(url, timeout=20, headers={"User-Agent": "ResearchStarterBot/1.0"}).text
        text = trafilatura.extract(html, url=url) or result.get("content", "")
        print((text or "")[:1200].strip())
    except Exception as exc:
        print(f"Could not scrape: {exc}")
    print("\n---\n")
