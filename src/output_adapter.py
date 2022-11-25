import abc


class OutputAdapter:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def send(self, data: list) -> str:
        """Present output"""
        pass


class EmailOutputAdapter(OutputAdapter):
    def send(self, data: list) -> str:
        outp = []
        for item in data:
            date_of_birth = item.get("date_of_birth")
            email = item.get("email")
            outp.append("Sending greeting to: {}".format(item.get("first_name")))
            outp.append("Who has date of birth: {}".format(date_of_birth))
            outp.append("by email: {}".format(email))
        return ". ".join(outp)


class SMSOutputAdapter(OutputAdapter):
    def send(self, data: list) -> str:
        outp = []
        for item in data:
            date_of_birth = item.get("date_of_birth")
            number = item.get("phone_number")
            outp.append("Sending greeting to: {}".format(item.get("first_name")))
            outp.append("Who has date of birth: {}".format(date_of_birth))
            outp.append("by sms: {}".format(number))
        return ". ".join(outp)


class TelegramOutputAdapter(OutputAdapter):
    def send(self, data: list) -> str:
        outp = []
        for item in data:
            date_of_birth = item.get("date_of_birth")
            tel = item.get("telegram")
            outp.append("Sending greeting to: {}".format(item.get("first_name")))
            outp.append("Who has date of birth: {}".format(date_of_birth))
            outp.append("by telegram: {}".format(tel))
        return ". ".join(outp)
