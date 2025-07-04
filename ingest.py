import lancedb
import polars as pl

DATA_FILE = "tmp/wikimedia.wikipedia.20231101.en/train-00017-of-00041.parquet"


def main():
    db = lancedb.connect("tmp/repro")
    raw_data = pl.read_parquet(DATA_FILE)
    data = raw_data.select(
        id=pl.col("id"),
        text=pl.col("text"),
    )
    tbl = db.create_table("test", data, exist_ok=True)
    tbl.create_fts_index("text", use_tantivy=False, replace=True, with_position=True)
    print(tbl.search().to_polars())


if __name__ == "__main__":
    main()
