# Search Quality & Relevance Evaluation

A small portfolio study of how well web search results satisfy technical queries. The dataset captures 30 result positions across 10 queries and includes the searcher intent, displayed title, URL, evidence, and rating for each accessible result.

## Findings

| Measure | Result |
| --- | ---: |
| Queries | 10 |
| Captured positions | 30 |
| Rated / unverified | 27 / 3 |
| Fully meets (3) | 19 |
| Mostly meets (2) | 5 |
| Partly meets (1) | 3 |
| Does not meet (0) | 0 |
| Mean relevance among rated results | 2.59 / 3 |
| Fully meets at position 1 | 9 / 10 |
| Duplicate positions | 6 |

- **Windows Python download.** All three positions lead to the same Windows release listing through different URLs. Each page meets the individual intent, while the result set provides only one distinct destination. [Python for Windows](https://www.python.org/downloads/windows/)
- **Node.js download.** The official download page directly serves the task. The source repository also helps, but requires a click through to the installers. [Download page](https://nodejs.org/en/download/) · [Project repository](https://github.com/nodejs/node#download)
- **Undoing a Git commit.** The first result discusses amending and unstaging. The Git book section that directly explains how reset can move the branch while retaining changes was outside the three captured results. [Undoing Things](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things) · [Reset Demystified](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified)

## Collection and rating

The results were collected on November 17, 2026 with the OpenAI web search tool. Each query was submitted separately, and the first three returned listings were preserved in the order supplied by the tool. These positions represent that response order. They are not verified Google rankings. Search location and personalization were uncontrolled.

The assistant inferred one intent per query, attempted to open every landing page, then scored each retrievable result using the rubric below. The Git download redirects were checked using their available destination and listing evidence. Unretrievable pages were retained as unverified with blank scores and excluded from rating averages. Duplicate destinations were tagged and retained at their captured positions. The overall mean is therefore position-weighted and includes duplicate positions. The sample focuses on developer queries and contains one set of assistant ratings without independent review.

## Rubric

| Rating | Decision rule |
| --- | --- |
| 3 — Fully meets | The result directly satisfies the specified intent and important constraints such as an exact platform or official source. |
| 2 — Mostly meets | The result substantially helps and provides a clear path, with an extra step or a gap in scope. |
| 1 — Partly meets | The result addresses the topic but leaves essential work to the searcher. |
| 0 — Does not meet | The result fails the intent or conflicts with an essential constraint. |
| Unverified | The landing page could not be inspected well enough to assign a defensible rating. |

## Reproduce the summary

Open `ratings.csv` in a spreadsheet to filter by query, position, rating, or verification status. Run `python analyze.py` from this folder to validate the dataset and regenerate the metrics using the Python standard library.

### Worked example — Q3, Node.js official download

Searcher intent: obtain an official Node.js installer or binary. The assistant rechecked the three landing pages against the rubric and retained these ratings.

| Position | Result | Rating | Evidence |
| --- | --- | ---: | --- |
| 1 | [Node.js download page](https://nodejs.org/en/download/) | 3 | Offers installers and binaries by release and platform, with an archive link for users without JavaScript. |
| 2 | [About Node.js](https://nodejs.org/en/about) | 2 | The official overview has a Download link in its navigation, so the installer is one step away. |
| 3 | [Node.js GitHub repository](https://github.com/nodejs/node#download) | 2 | The project's Download section points to official binaries and installers on the Node.js website. |
