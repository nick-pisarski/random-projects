import json
from dataclasses import dataclass
from pathlib import Path

SEARCH_TERMS_FP = f"{Path(__file__).parents[1]}/no_commit/search_terms.json"


@dataclass
class SearchTerm:
    term: str
    replacement: str | None
    category: str = "Other"


def get_descriptions() -> list[SearchTerm]:
    search_terms = []
    with open(SEARCH_TERMS_FP) as f:
        data = json.load(f)
        for term in data:
            search_terms.append(
                SearchTerm(term["term"], term["replacement"], term["category"])
            )
    return search_terms


if __name__ == "__main__":
    desc = get_descriptions()
    for d in get_descriptions():
        print(d)
