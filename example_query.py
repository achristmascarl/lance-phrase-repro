import lancedb
from lancedb.query import PhraseQuery


def main():
    db = lancedb.connect("tmp/working")
    data = [
        {"id": 1, "text": "The United States is a country."},
        {"id": 2, "text": "I like ice cream."},
    ]
    tbl = db.create_table("test", data, exist_ok=True)
    tbl.create_fts_index("text", use_tantivy=False, replace=True, with_position=True)
    result = tbl.search(PhraseQuery("United States", "text", slop=0)).to_polars()
    print(result)


if __name__ == "__main__":
    main()
