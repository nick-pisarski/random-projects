import csv
import sys

from lib.transaction import Transaction
from lib.transaction_list import TransactionList

CATEGORY_FP = "output/analysis_by_category.txt"
TRANSACTION_FP = "output/transactions_by_year.txt"
ACCOUNT_HISTORY_FP = "no_commit/AccountHistory.csv"


def load_transactions_from_file() -> list[Transaction]:
    transactions = []
    with open(ACCOUNT_HISTORY_FP, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions.append(Transaction(row))
    return TransactionList.clean_transaction_desc(transactions)


def main():
    all_transactions = load_transactions_from_file()
    years = [2020, 2021]
    default_stdout = sys.stdout
    with open(CATEGORY_FP, "w+") as f:
        sys.stdout = f
        for year in years:
            transactions = TransactionList.filter_by_year(all_transactions, year)
            print(f"======== Year {year} =========")
            TransactionList.print_category_summary(transactions)
            TransactionList.print_summary(transactions)
            print(f"============================")
            print("")
        sys.stdout = default_stdout
        print(CATEGORY_FP)

    with open(TRANSACTION_FP, "w+") as f:
        sys.stdout = f
        for year in years:
            transactions = TransactionList.filter_by_year(all_transactions, year)
            print(f"======== Year {year} =========")
            TransactionList.print_list(transactions)
            print(f"============================")
            print("")
        sys.stdout = default_stdout
        print(TRANSACTION_FP)

    print("Done!")


if __name__ == "__main__":
    main()
