import abc
from datetime import datetime
from tinydb import TinyDB, Query


CORRECT_DATE_FORMAT = "%Y-%m-%d"


def check_date_format(date_format: str, value: str):
    try:
        datetime.strptime(value, date_format)
    except ValueError:
        raise ValueError(
            f"This is the incorrect date string format. It should be {date_format}"
        )


def check_date_is_today(value: str):
    if value != str(datetime.today().date()):
        raise ValueError(
            f"This is the incorrect date. It is not today {datetime.today().date()}"
        )


class DbAdapter:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search(self, query: str) -> list:
        """Search the database"""
        pass

    @abc.abstractmethod
    def add(self, df: dict) -> list:
        """Add an item to the database"""
        pass


class Notes_TDB_Adapter(DbAdapter):
    def __init__(self, path):
        self.tdb = TinyDB(path)
        self.today_date: str

    @property
    def today_date(self) -> str:
        return self._today_date

    @today_date.setter
    def today_date(self, value: str) -> None:
        check_date_format(date_format=CORRECT_DATE_FORMAT, value=value)
        check_date_is_today(value=value)
        self._today_date = value

    def search(self, today_date: str) -> list:
        self.today_date = today_date
        Note = Query()
        return self.tdb.search(Note.date_of_birth == self.today_date)

    def add(self, df: dict):
        self.tdb.insert(df)
