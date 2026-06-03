---
name: web-research-router
description: Unified routing skill for web research. Use when a user asks to search the web, scrape a URL, crawl a site, extract structured data, or run deeper research; chooses Tavily, scraping scripts, browser automation, or deep-research workflow as appropriate.
---

# Web Research Router

Use this skill to choose the right research path.

## Decision tree

| User need | Best path |
|---|---|
| General search, finding URLs, current info | Tavily search |
| Read one specific URL | Single-page scrape |
| List pages/links on a site | Link extraction or site map |
| Crawl a site section | Bounded crawler |
| Extract fields from pages | Scrape then structured extraction |
| Click forms/buttons, login flows, screenshots | Browser automation such as Playwright |
| Compare sources, investigate a topic, produce report | Deep research workflow |

## Operating rules

1. Prefer search for discovery, scraping for known URLs, and deep research for multi-source answers.
2. Keep crawls bounded with max pages, depth, same-domain limits, and delays.
3. Cite source URLs in final answers.
4. Track uncertainty, contradictions, and dates.
5. Do not scrape private, gated, sensitive, or disallowed content.

## Example local commands

From this repo:

```bash
cd examples/python
python tavily_search.py "query"
python scrape_page.py https://example.com
python extract_links.py https://example.com
python crawl_site.py https://example.com --max-pages 10 --depth 1
python research_pipeline.py "research question"
```

See `references/routing.md` for more detail.
