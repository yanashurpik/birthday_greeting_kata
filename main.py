import argparse
import pathlib
from typing import Optional

from src.data_providers import DataProvider
from src.DB_adapter import Notes_TDB_Adapter
from src.birthday_notebook import BirthdayNotebook
from tinydb import TinyDB
import pandas as pd
from src.output_adapter import (
    EmailOutputAdapter,
    TelegramOutputAdapter,
    SMSOutputAdapter,
    OutputAdapter,
)

TDB_JSON: str = "tdb.json"
path = pathlib.Path(__file__).resolve()


def main(data_provider: DataProvider) -> None:
    output_adapter: Optional[OutputAdapter] = None
    if data_provider.value == "email":
        output_adapter = EmailOutputAdapter()
        csv_with_user_data = "input_email.csv"
        search_value = "2022-08-12"
    elif data_provider.value == "telegram":
        output_adapter = TelegramOutputAdapter()
        csv_with_user_data = "input_telegram.csv"
        search_value = "1981-12-07"
    elif data_provider.value == "sms":
        output_adapter = SMSOutputAdapter()
        csv_with_user_data = "input_sms.csv"
        search_value = "1943-10-26"
    else:
        raise Exception(f"There is no such provider {output_adapter}")

    dict_from_csv: dict = pd.read_csv(csv_with_user_data).to_dict("records")

    tdb: TinyDB = TinyDB(TDB_JSON)
    for item in dict_from_csv:
        tdb.insert(item)

    db_adapter = Notes_TDB_Adapter(TDB_JSON)

    notebook = BirthdayNotebook(notes=db_adapter, output=output_adapter)

    print(notebook.send_note(search_value))

    tdb.truncate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_provider", type=DataProvider, choices=list(DataProvider))
    args = parser.parse_args()
    main(args.data_provider)
