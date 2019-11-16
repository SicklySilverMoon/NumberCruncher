from decimal import Decimal


def aperys(precision):
    aperys_constant = Decimal(0)
    term = Decimal(0)

    for i in range(1, precision):  # there likely exists a better way to do this but i'm unsure of how to do so
        aperys_constant += term
        term = Decimal(1) / i ** 3  # you better believe Decimal(1) is needed
        i += 1

    return aperys_constant
