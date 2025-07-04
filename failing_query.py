import lancedb
from lancedb.query import PhraseQuery


def main():
    db = lancedb.connect("tmp/repro")
    tbl = db.open_table("test")

    # Non-phrase FTS query works
    fts_results = tbl.search("united states", "text").to_polars()
    print(fts_results)
    fts_results["text"].to_list()
    matches = 0

    # At least some of the results should have an exact phrase match
    for i, row in enumerate(fts_results["text"]):
        if str(row).find("United States") >= 0:
            matches += 1
    print(f"Found {matches} exact matches in non-phrase FTS results.")

    # Doesn't work, no results
    phrase_results = tbl.search(
        PhraseQuery("United States", "text", slop=0)
    ).to_polars()
    print(phrase_results)

    # Even with slop=1, no results
    phrase_results = tbl.search(
        PhraseQuery("United States", "text", slop=1)
    ).to_polars()
    print(phrase_results)


if __name__ == "__main__":
    main()
