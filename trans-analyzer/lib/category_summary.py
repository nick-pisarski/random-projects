from dataclasses import dataclass


@dataclass
class CategorySummary:
    debit: float
    credit: float
    transaction_count: int = 1
