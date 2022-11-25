import argparse

from dataclasses import dataclass
from birthday_greetings.yana.src.data_providers import DataProvider

from faker import Faker
from faker.providers import date_time, internet, person, phone_number

fake = Faker()
fake.add_provider(internet)
fake.add_provider(person)
fake.add_provider(date_time)
fake.add_provider(phone_number)


@dataclass
class PersonDataInterface:
    data_provider: DataProvider
    first_name: str
    last_name: str
    date_of_birth: str
    file_name: str
    columns: str
    provider_property: str


PersonData: dict[DataProvider, list[PersonDataInterface]] = {
    DataProvider.EMAIL: [
        PersonDataInterface(
            data_provider=DataProvider.EMAIL,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            date_of_birth=fake.date_of_birth(),
            provider_property=fake.email(),
            file_name="input_email.csv",
            columns="last_name,first_name,date_of_birth,email\n",
        )
        for i in range(1000)
    ],
    DataProvider.SMS: [
        PersonDataInterface(
            data_provider=DataProvider.SMS,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            date_of_birth=fake.date_of_birth(),
            provider_property=fake.phone_number(),
            file_name="input_sms.csv",
            columns="last_name,first_name,date_of_birth,phone_number\n",
        )
        for i in range(1000)
    ],
    DataProvider.TELEGRAM: [
        PersonDataInterface(
            data_provider=DataProvider.TELEGRAM,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            date_of_birth=fake.date_of_birth(),
            provider_property=fake.slug(),
            file_name="input_telegram.csv",
            columns="last_name,first_name,date_of_birth,telegram\n",
        )
        for i in range(1000)
    ],
}


def generate_fake_person_data(provider: DataProvider) -> None:
    for person in PersonData[provider]:
        print(person)
        with open(person.file_name, "a") as f:
            if PersonData[provider].index(person) == 0:
                f.write(person.columns)

            f.write(
                f"{person.last_name},{person.first_name},{person.date_of_birth},"
                f"{person.provider_property}\n"
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_source", type=DataProvider, choices=list(DataProvider))
    args = parser.parse_args()
    generate_fake_person_data(args.data_source)
