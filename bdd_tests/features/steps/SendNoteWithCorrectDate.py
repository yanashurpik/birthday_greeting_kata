import os
from freezegun import freeze_time
import pytest
from behave import *
import pathlib
from bdd_tests.functions import create_database_with_test_data
from src.birthday_notebook import BirthdayNotebook

TDB_JSON: str = "tdb.json"
use_step_matcher("re")
path = pathlib.Path(__file__).parent.parent.resolve()


greeting: list = []


@given("db_adapter and output_adapter with (?P<output_provider>.+) are created")
def step_impl(context, output_provider: str, ):
    """
    :param output_provider:
    :type context: behave.runner.Context
    """
    db_adapter, output_adapter, context.tdb = create_database_with_test_data(output_provider)
    context.notebook = BirthdayNotebook(notes=db_adapter, output=output_adapter)


@pytest.mark.freeze_time
@when("I send note via (?P<output_provider>.+) that has (?P<date_of_birth>.+)")
def step_impl(context, output_provider: str, date_of_birth: str):
    """
    :param date_of_birth: str
    :type context: behave.runner.Context
    :type output_provider: str
    """
    with freeze_time(date_of_birth):
        context.greet = context.notebook.send_note(date_of_birth)


@then("friends with (?P<date_of_birth>.+) have a (?P<greeting_note>.+)")
def step_impl(context, date_of_birth: str, greeting_note: str):
    """
    :param greeting_note:
    :type context: behave.runner.Context
    :type date_of_birth: str
    """
    assert context.greet == greeting_note
    context.tdb.truncate()
