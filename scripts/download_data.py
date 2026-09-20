"""Download the RAG knowledge-base dataset (SQuAD 2.0 or MS MARCO).

See docs/modules/01_rag_system.md, task 1.

Usage: python scripts/download_data.py
"""

from pathlib import Path

RAW_DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

SQUAD_V2_TRAIN_URL = "https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json"
SQUAD_V2_DEV_URL = "https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v2.0.json"


def download_squad(target_dir: Path = RAW_DATA_DIR) -> None:
    """Download SQuAD 2.0 train/dev JSON into `target_dir`.

    TODO:
        - Use `requests` (or `urllib`) to fetch SQUAD_V2_TRAIN_URL / _DEV_URL
        - Save as target_dir / "squad_train.json" and "squad_dev.json"
        - Skip re-downloading if the file already exists
    """
    raise NotImplementedError("TODO: implement download_squad (Module 1)")


if __name__ == "__main__":
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    download_squad()
