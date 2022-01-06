import functools
from typing import OrderedDict

from lib.category_summary import CategorySummary
from lib.search_term import get_descriptions
from lib.transaction import Transaction


class TransactionList:
    @staticmethod
    def filter_by_year(transactions: list[Transaction], year: int) -> list[Transaction]:
        transactions_copy = transactions.copy()
        return list(filter(lambda t: t.post_date.year == year, transactions_copy))

    @staticmethod
    def clean_transaction_desc(transactions: list[Transaction]) -> list[Transaction]:
        trans_copy = transactions.copy()

        for transaction in trans_copy:
            for search_term in get_descriptions():
                if search_term.term in transaction.description.upper():
                    if search_term.replacement is not None:
                        transaction.description = search_term.replacement
                    else:
                        transaction.description = search_term.term
                    transaction.category = search_term.category
                    break
            if transaction.category == "Other" and transaction.credit > 0:
                transaction.category = "Misc Income"

        trans_copy.sort(key=lambda t: t.category)

        return trans_copy

    @staticmethod
    def sum_debits(transactions: list[Transaction]) -> float:
        return functools.reduce(lambda a, b: a + b, [t.debit for t in transactions])

    @staticmethod
    def sum_credits(transactions: list[Transaction]) -> float:
        return functools.reduce(lambda a, b: a + b, [t.credit for t in transactions])

    @staticmethod
    def group_by_desc(
        transactions: list[Transaction],
    ) -> OrderedDict:
        groups = {}

        for trans in transactions:
            if trans.category not in groups:
                groups.update(
                    {trans.category: CategorySummary(trans.debit, trans.credit, 1)}
                )
            else:
                summary = groups[trans.category]
                summary.debit = trans.debit + summary.debit
                summary.credit = trans.credit + summary.credit
                summary.transaction_count = summary.transaction_count + 1

        return OrderedDict(
            sorted(groups.items(), key=lambda t: t[1].credit - t[1].debit)
        )

    @staticmethod
    def print_list(transactions: list[Transaction]) -> None:
        for transaction in transactions:
            print(transaction)

    @staticmethod
    def print_category_summary(transactions: list[Transaction]) -> None:
        grouped = TransactionList.group_by_desc(transactions)
        print("----- Category Summary -----")
        for category, summary in grouped.items():
            profit = round(summary.credit - summary.debit)
            print(f"{category:12}    {profit:12,.2f}")
        print("----------------------------")

    @staticmethod
    def print_summary(transactions: list[Transaction]) -> None:
        sum_debits = TransactionList.sum_debits(transactions)
        sum_credits = TransactionList.sum_credits(transactions)
        profits = sum_credits - sum_debits
        prefix = "+" if profits > 0 else "-"
        # print(f"Transactions: {len(transactions)}")
        print(f"Credits:       +{sum_credits:12,.2f}")
        print(f"Debits:        -{sum_debits:12,.2f}")
        print(f"               -------------")
        print(f"               {prefix}{profits:12,.2f}")
