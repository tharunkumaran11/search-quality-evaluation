"""Validate the captured result set and report relevance metrics."""
import csv
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean


def main():
    with Path(__file__).with_name("ratings.csv").open(encoding="utf-8-sig", newline="") as file:
        rows = list(csv.DictReader(file))
    queries = defaultdict(list)
    scores = []
    for row in rows:
        queries[row["query_id"]].append(row)
        rank = int(row["position"])
        if not row["rationale"] or not row["url"].startswith("https://"):
            raise ValueError("Each position requires a URL and review rationale.")
        if row["status"] == "rated" and row["rating"] in {"0", "1", "2", "3"}:
            scores.append(int(row["rating"]))
        elif row["status"] != "unverified" or row["rating"]:
            raise ValueError("An unverified result must have a blank rating.")
        duplicate = row["duplicate_of_position"]
        if duplicate and not 1 <= int(duplicate) < rank:
            raise ValueError("A duplicate must reference an earlier position.")
    if len(queries) != 10 or any(sorted(int(r["position"]) for r in q) != [1, 2, 3]
                                for q in queries.values()):
        raise ValueError("Expected 10 queries with positions 1, 2, and 3 each.")
    top = [r for r in rows if r["position"] == "1"]
    rated_top = [r for r in top if r["status"] == "rated"]
    duplicates = sum(bool(r["duplicate_of_position"]) for r in rows)
    print(f"Queries: {len(queries)} | Captured positions: {len(rows)}")
    print(f"Rated: {len(scores)} | Unverified: {len(rows) - len(scores)} | Duplicate positions: {duplicates}")
    print(f"Rating distribution: {dict(sorted(Counter(scores).items()))}")
    print(f"Mean relevance among rated results: {mean(scores):.2f}/3")
    print(f"Fully meets at position 1: {sum(r['rating'] == '3' for r in rated_top)}/{len(rated_top)} rated")


if __name__ == "__main__":
    main()
