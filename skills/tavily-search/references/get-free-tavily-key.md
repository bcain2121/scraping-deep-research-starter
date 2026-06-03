# How to get a free Tavily API key

Tavily is an AI-focused search API that is useful for research agents and search-augmented workflows.

## Steps

1. Visit https://tavily.com
2. Click **Get Started**, **Sign Up**, or similar.
3. Create an account.
4. Open the Tavily dashboard.
5. Find **API Keys**.
6. Create or copy your API key.
7. In this repo, copy the env example:

```bash
cd examples/python
cp .env.example .env
```

8. Add your key:

```bash
TAVILY_API_KEY=tvly-your-key-here
```

9. Test it:

```bash
python tavily_search.py "latest web scraping best practices"
```

## Safety

Do not commit `.env` or any real key to GitHub. This repo includes `.gitignore` rules to keep local secrets out of commits.
