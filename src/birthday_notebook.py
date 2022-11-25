from typing import Any
from src.DB_adapter import DbAdapter
from src.output_adapter import OutputAdapter


class BirthdayNotebook:
    def __init__(self, notes: DbAdapter, output: OutputAdapter):
        self.notes = notes
        self.output = output

    def send_note(self, query) -> str:
        return self.output.send(self.notes.search(query))

    def add(self, df: Any):
        self.notes.add(df)
