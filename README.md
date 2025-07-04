# lance-phrase-repro
steps:
1. install uv
2. download 20231101.en/train-00017-of-00041.parquet from https://huggingface.co/datasets/wikimedia/wikipedia/blob/main/20231101.en/train-00017-of-00041.parquet
3. place dataset in a `tmp/` directory
4. `uv run ingest.py`
5. `uv run failing_query.py`
6. see that the phrase query fails
7. `uv run example_query.py`
8. see that it works on a small, toy example
