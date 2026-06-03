---
name: deep-research-workflow
description: Repeatable deep research workflow for planning, source gathering, verification, synthesis, and bibliography creation. Use when a user asks to research, investigate, compare, or produce a source-backed report.
---

# Deep Research Workflow

Use this skill when the task needs more than a quick search.

## Depth levels

| Depth | Typical use |
|---|---|
| Quick | 3-5 sources, overview answer |
| Standard | 8-10 sources, balanced summary |
| Deep | 12-20 sources, report with verification |

Default to **deep** if the user asks for “deep research”; otherwise pick the smallest depth that satisfies the request.

## Workflow

1. **Normalize** — define question, audience, geography/timeframe, output.
2. **Plan** — create subquestions and source targets.
3. **Discover** — use Tavily/search to find candidate sources.
4. **Gather** — scrape official pages, expert sources, data pages, and opposing views.
5. **Extract** — capture source-backed claims with URLs.
6. **Verify** — cross-check important claims against independent or primary sources.
7. **Synthesize** — write summary, findings, uncertainty, and bibliography.
8. **Bounded follow-up** — do 1-2 extra passes only for major gaps.

## Output template

```markdown
# Research Report: <topic>

## Executive Summary

## Key Findings

## Evidence and Analysis

## Contradictions / Uncertainty

## Open Questions

## Bibliography
```

See `references/deep-research-workflow.md` for details.
