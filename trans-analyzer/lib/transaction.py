from datetime import datetime


class Transaction:
    """A Transaction"""

    def __init__(self, transaction: dict) -> None:
        self.account_number = transaction["Account Number"]
        self.balance = self._convert_to_decimal(transaction["Balance"])
        self.check = transaction["Check"]
        self.credit = self._convert_to_decimal(transaction["Credit"])
        self.debit = self._convert_to_decimal(transaction["Debit"])
        self.description = transaction["Description"]
        self.post_date = datetime.strptime(transaction["Post Date"], "%m/%d/%Y")
        self.status = transaction["Status"]
        self.category = "Other"

    def _convert_to_decimal(self, val: str) -> float:
        if val != "" and val is not None:
            return float(val)
        return 0.0

    def __str__(self):
        post_date = self.post_date.strftime("%m/%d/%Y")
        amt = self.credit - self.debit
        prf = "+" if amt > 0 else "-"
        return f"{post_date}| {prf}{abs(amt):9.2f} |{self.category.upper():14}|{self.description}"

    def __repr__(self):

        return self.__str__()
