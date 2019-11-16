from decimal import Decimal


def golden_ratio():
    golden_constant = Decimal((1 + Decimal(5).sqrt()) / 2)

    return golden_constant
