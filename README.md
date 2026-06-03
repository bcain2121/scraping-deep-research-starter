# Scraping + Deep Research Starter

A lightweight public starter kit for web scraping, Tavily search, and repeatable deep-research workflows.

This repo bundles practical patterns for:

- discovering URLs on a site
- scraping clean page text
- extracting links and structured facts
- using Tavily for AI-friendly web search
- running a repeatable deep-research workflow: plan → gather → verify → synthesize

> No API keys or private credentials are included. Copy `.env.example` to `.env` and add your own keys.

## Quick start

```bash
git clone https://github.com/bcain2121/scraping-deep-research-starter.git
cd scraping-deep-research-starter/examples/python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

If you want Tavily search, add your Tavily key to `.env`:

```bash
TAVILY_API_KEY=tvly-your-key-here
```

## Get a free Tavily API key

1. Go to https://tavily.com
2. Click **Get Started** or **Sign Up**.
3. Create a free account.
4. Open the dashboard.
5. Go to API Keys.
6. Copy your key.
7. Put it in `examples/python/.env` as `TAVILY_API_KEY=...`.

See [`docs/tavily-free-key.md`](docs/tavily-free-key.md) for details.

## Example commands

### Search the web with Tavily

```bash
cd examples/python
python tavily_search.py "best practices for website scraping politely"
```

### Scrape a single page

```bash
python scrape_page.py https://example.com
```

### Extract links from a page

```bash
python extract_links.py https://example.com
```

### Crawl a small site section

```bash
python crawl_site.py https://example.com --max-pages 10 --depth 1
```

### Run a simple research pipeline

```bash
python research_pipeline.py "San Diego ADU permit requirements 2026"
```

## Deep research workflow

A good deep-research workflow is not just scraping more pages. It is a bounded loop:

1. **Normalize the question** — define scope, audience, and expected output.
2. **Plan the investigation** — list subquestions and source types.
3. **Gather sources** — use search, scraping, crawling, and official docs.
4. **Extract claims** — turn pages into source-backed facts.
5. **Verify** — cross-check important claims against independent sources.
6. **Find gaps/contradictions** — explicitly track uncertainty.
7. **Synthesize** — write a short answer, then a full report with bibliography.
8. **Bounded follow-up** — do 1–2 extra passes only where gaps remain.

See [`docs/deep-research-workflow.md`](docs/deep-research-workflow.md).

## Responsible scraping notes

- Respect robots.txt and site terms.
- Use rate limits and small crawl sizes.
- Identify yourself when appropriate.
- Prefer official APIs when available.
- Do not scrape private, gated, or sensitive data without permission.
- Cache results to avoid hammering sites.

## Repo structure

```text
.
├── README.md
├── docs/
│   ├── deep-research-workflow.md
│   ├── scraping-playbook.md
│   └── tavily-free-key.md
└── examples/python/
    ├── .env.example
    ├── requirements.txt
    ├── tavily_search.py
    ├── scrape_page.py
    ├── extract_links.py
    ├── crawl_site.py
    └── research_pipeline.py
```
