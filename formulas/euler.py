from decimal import Decimal


def euler():
    eulers_constant = Decimal(0)
    term = Decimal(1)
    current_iteration = Decimal(0)

    while eulers_constant + term != eulers_constant:  # you don't have to loop up to the amount of precision, you only have to go until it hits the set precision limit
        eulers_constant += term
        term /= current_iteration + 1
        current_iteration += 1

    return eulers_constant
