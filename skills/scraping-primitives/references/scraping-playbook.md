# Scraping playbook

## 1. Decide whether scraping is appropriate

Before scraping, check whether the site offers:

- an official API
- RSS feeds
- sitemap XML
- downloadable CSV/PDF resources
- a terms-compliant data export

Use those first when available.

## 2. Discovery patterns

Start with lightweight discovery:

- homepage links
- `/robots.txt`
- `/sitemap.xml`
- category or index pages
- search-result pages if permitted

## 3. Single-page scrape

For most research tasks, scrape one URL at a time and extract:

- title
- main text
- outbound links
- publication/update date if visible
- source URL

## 4. Bounded crawl

When crawling, set hard limits:

- max pages
- max depth
- same-domain-only
- include/exclude URL filters
- delay between requests

## 5. Structured extraction

Convert raw page text into records such as:

```json
{
  "claim": "The stated factual claim",
  "evidence": "Exact supporting quote or summary",
  "source_url": "https://...",
  "confidence": "high|medium|low"
}
```

## 6. Verification

For important claims, require at least two sources or one primary/official source.

Track:

- confirmed findings
- contradictions
- outdated pages
- missing evidence
- follow-up questions
