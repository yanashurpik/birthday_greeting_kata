import os
from datetime import datetime
from typing import Optional
from tinydb import TinyDB
import pandas as pd
from behave import *
import pathlib

from src.DB_adapter import Notes_TDB_Adapter
from src.output_adapter import (
    EmailOutputAdapter,
    SMSOutputAdapter,
    TelegramOutputAdapter, OutputAdapter,
)

TDB_JSON: str = "tdb.json"
use_step_matcher("re")
path = pathlib.Path(__file__).parent.parent.resolve()


def create_database_with_test_data(output_provider: str):
    output_adapter: Optional[OutputAdapter] = None
    if output_provider == "email":
        output_adapter = EmailOutputAdapter()
        csv_with_user_data = os.path.join(path, "input_email.csv")
    elif output_provider == "telegram":
        output_adapter = TelegramOutputAdapter()
        csv_with_user_data = os.path.join(path, "input_telegram.csv")
    elif output_provider == "sms":
        output_adapter = SMSOutputAdapter()
        csv_with_user_data = os.path.join(path, "input_sms.csv")
    else:
        raise Exception(f"There is no such provider {output_adapter}")

    dict_from_csv: dict = pd.read_csv(csv_with_user_data).to_dict("records")

    tdb: TinyDB = TinyDB(TDB_JSON)
    for item in dict_from_csv:
        tdb.insert(item)

    db_adapter = Notes_TDB_Adapter(TDB_JSON)
    return db_adapter, output_adapter, tdb


def check_date_is_today(value: str):
    try:
        value == str(datetime.today().date())
    except ValueError:
        raise ValueError(
            f"This is the incorrect date. It is not today {datetime.today().date()}"
        )

