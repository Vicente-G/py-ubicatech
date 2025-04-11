import csv
import io
import json
import os

import pandas as pd

from src.config import TARGET_FOLDER


def remove_last_line(filename):
    with open(filename, "r+", encoding="utf-8") as file:
        file.seek(0, os.SEEK_END)
        file.seek(file.tell() - 1, os.SEEK_SET)
        file.truncate()


def generate_migration_from(json_object, component):
    filename = f"{TARGET_FOLDER}/{component}.csv"
    stringified_json = json.dumps(json_object)
    df = pd.read_json(io.StringIO(stringified_json))
    df.to_csv(
        filename,
        index=False,
        header=False,
        quotechar="'",
        quoting=csv.QUOTE_NONNUMERIC,
    )
    remove_last_line(filename)
