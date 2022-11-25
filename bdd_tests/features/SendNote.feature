Feature: send birthday greeting


Scenario Outline: Send  birthday greeting
   Given  db_adapter and output_adapter with <output_provider> are created
   When I send note via <output_provider> that has <date_of_birth>
   Then friends with <date_of_birth> have a <greeting_note>

 Examples: Test data
   | output_provider  | date_of_birth | greeting_note|
   | sms               | 1918-12-28   | Sending greeting to: Lisa. Who has date of birth: 1918-12-28. by sms: +1-816-682-0064x7511|
   | email             | 1920-08-22   | Sending greeting to: Angela. Who has date of birth: 1920-08-22. by email: isabellaali@example.org|
   | telegram          | 1954-01-04   | Sending greeting to: Brandi. Who has date of birth: 2022-08-12. by telegram: what-arrive-quite|
