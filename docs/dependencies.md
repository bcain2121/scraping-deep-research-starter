# Dependencies

This bundle is intentionally lightweight. The skills themselves are markdown instructions; the example scraping/search scripts use Python.

## Required

- **Git** — to clone the repo.
- **Python 3.10+** — Python 3.11+ preferred.
- **pip** and **venv** — for installing Python packages in a virtual environment.
- Internet access.

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install -y git python3 python3-pip python3-venv
```

On macOS with Homebrew:

```bash
brew install git python
```

## Python packages

Installed from `examples/python/requirements.txt`:

- `requests` — HTTP requests.
- `beautifulsoup4` — HTML parsing and link extraction.
- `trafilatura` — clean main-text extraction from web pages.
- `python-dotenv` — loads `.env` files.
- `tavily-python` — Tavily Search API client.

Install:

```bash
cd examples/python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## API keys

### Tavily

Needed only for `tavily_search.py` and `research_pipeline.py`.

Get a free key at https://tavily.com, then:

```bash
cd examples/python
cp .env.example .env
# edit .env and add:
TAVILY_API_KEY=tvly-your-key-here
```

## Optional

- **Playwright** — only needed if you want browser automation for JS-heavy pages, clicking, forms, or screenshots.

```bash
pip install playwright
python -m playwright install chromium
```

- **Agent Skills-compatible harness** — Pi, Claude Code-style skills, or any tool that can load `skills/*/SKILL.md` directories.

## Quick dependency check

```bash
git --version
python3 --version
python3 -m pip --version
```
