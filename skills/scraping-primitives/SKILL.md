---
name: scraping-primitives
description: Practical web scraping skill for reading pages, extracting links, bounded crawling, and preparing structured extraction. Use when the user provides URLs or asks to scrape, crawl, map, or extract information from websites.
---

# Scraping Primitives

Use this skill for safe, bounded scraping tasks.

## Setup

```bash
cd examples/python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Commands

### Scrape one page

```bash
python scrape_page.py https://example.com
```

### Extract links

```bash
python extract_links.py https://example.com
```

### Bounded crawl

```bash
python crawl_site.py https://example.com --max-pages 10 --depth 1 --delay 1
```

## Rules

- Respect robots.txt and terms.
- Keep crawl limits small by default.
- Use a clear User-Agent.
- Cache or save results when running repeated research.
- Do not scrape private, sensitive, gated, or disallowed content.
- Prefer official APIs if available.

## Extraction pattern

For every important fact, capture:

- claim
- evidence/quote
- source URL
- page title/date if available
- confidence level

See `references/scraping-playbook.md`.
