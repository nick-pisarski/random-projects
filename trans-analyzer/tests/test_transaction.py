import unittest
from datetime import datetime

from lib.transaction import Transaction


def get_transaction_dict() -> dict:
    return {
        "Account Number": "123456789",
        "Balance": "1297.47",
        "Check": "",
        "Credit": "245.96",
        "Debit": "",
        "Description": "some_description",
        "Post Date": "9/8/2017",
        "Status": "Posted",
    }


class TestTransaction(unittest.TestCase):
    def setUp(self) -> None:
        self.transaction = Transaction(get_transaction_dict())

    def test_parses_date(self):
        expected = datetime(2017, 9, 8)

        self.assertEqual(type(self.transaction.post_date), type(expected))
        self.assertEqual(self.transaction.post_date.year, expected.year)
        self.assertEqual(self.transaction.post_date.month, expected.month)
        self.assertEqual(self.transaction.post_date.day, expected.day)

    def test_parses_balance(self):
        expected = float(1297.47)

        self.assertEqual(type(self.transaction.balance), type(expected))
        self.assertEqual(self.transaction.balance, expected)

    def test_parses_credit(self):
        expected = float(245.96)

        self.assertEqual(type(self.transaction.credit), type(expected))
        self.assertEqual(self.transaction.credit, expected)

    def test_parses_debit(self):
        expected = float(0)

        self.assertEqual(type(self.transaction.debit), type(expected))
        self.assertEqual(self.transaction.debit, expected)
