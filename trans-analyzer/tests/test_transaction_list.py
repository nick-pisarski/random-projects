import unittest

from lib.transaction import Transaction
from lib.transaction_list import TransactionList


def get_transaction(
    post_date: str = "1/1/1999",
    credit: float = 0.0,
    debit: float = 0.1,
    desc: str = "default desc",
) -> Transaction:
    trans_dict = {
        "Account Number": "123456789",
        "Balance": "1297.47",
        "Check": "",
        "Credit": str(credit),
        "Debit": str(debit),
        "Description": desc,
        "Post Date": post_date,
        "Status": "Posted",
    }
    return Transaction(trans_dict)


class TestTransactionList(unittest.TestCase):
    def test_filter_by_date(self):
        transactions = [
            get_transaction(post_date="1/12/1999"),
            get_transaction(post_date="1/12/2000"),
        ]
        expected = [
            get_transaction(post_date="1/12/2000"),
        ]

        result = TransactionList.filter_by_year(transactions, 2000)

        self.assertEqual(len(result), len(expected))
        self.assertEqual(result[0].post_date.year, expected[0].post_date.year)

    def test_sum_debits(self):
        transactions = [get_transaction(debit=1.1) for _ in range(0, 10)]
        expected = 11.0

        result = TransactionList.sum_debits(transactions)

        self.assertAlmostEqual(result, expected, 1)

    def test_sum_credits(self):
        transactions = [get_transaction(credit=1.1) for _ in range(0, 10)]
        expected = 11.0

        result = TransactionList.sum_credits(transactions)

        self.assertAlmostEqual(result, expected, 1)
