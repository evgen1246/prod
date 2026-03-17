from pathlib import Path

import pandas as pd


def read_transactions_from_csv(path_file: Path) -> list:
    path_file = Path(path_file)

    if not path_file.exists():
        raise FileNotFoundError(f"Файл не найден: {path_file}")

    df = pd.read_csv(path_file)
    operation = df.to_dict(orient="records")
    return operation


def read_transactions_from_excel(path_file: Path) -> list:
    path_file = Path(path_file)

    if not path_file.exists():
        raise FileNotFoundError(f"Файл не найден: {path_file}")
    df = pd.read_excel(path_file)
    operation = df.to_dict(orient="records")
    return operation
