---
name: tavily-search
description: Tavily web search skill for quick AI-friendly searches, source discovery, and current fact lookup. Use when the user asks to search, find sources, look up current information, or gather URLs before scraping.
---

# Tavily Search

Tavily is useful for search/discovery before scraping or research synthesis.

## Setup

1. Get a free key: see `references/get-free-tavily-key.md`.
2. Install dependencies:

```bash
cd examples/python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

3. Add your key to `.env`:

```bash
TAVILY_API_KEY=tvly-your-key-here
```

## Usage

```bash
cd examples/python
python tavily_search.py "your search query"
```

## When to use

- general web search
- finding current info
- source discovery before scraping
- finding official pages

## When not to use

- reading one known URL: use scraping-primitives
- clicking/interacting with pages: use browser automation
- long report generation: use deep-research-workflow
