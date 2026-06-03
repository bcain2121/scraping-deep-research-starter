#!/usr/bin/env python3
import os
import sys
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

query = " ".join(sys.argv[1:]).strip()
if not query:
    print("Usage: python tavily_search.py '<query>'")
    sys.exit(1)

api_key = os.getenv("TAVILY_API_KEY")
if not api_key:
    print("Missing TAVILY_API_KEY. Copy .env.example to .env and add your key.")
    sys.exit(1)

client = TavilyClient(api_key=api_key)
response = client.search(query=query, search_depth="advanced", max_results=5)

for i, result in enumerate(response.get("results", []), 1):
    print(f"\n{i}. {result.get('title')}")
    print(result.get("url"))
    print(result.get("content", "")[:600])
