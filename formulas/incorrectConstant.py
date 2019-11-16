from decimal import Decimal


def incorrect():  # This constant is caused doing the steps for pi in a wrong order which results in a very different number
    incorrect_constant = Decimal(0)
    term = Decimal(1)
    current_iteration = Decimal(0)

    C = Decimal(426880)*Decimal(10005).sqrt()
    M = Decimal(1)  # names from https://en.wikipedia.org/wiki/Chudnovsky_algorithm
    L = Decimal(13591409)
    X = Decimal(1)  # and yes i understand they're terrible variable names but it makes it easier to follow the page
    K = Decimal(6)

    while incorrect_constant + term != incorrect_constant:
        incorrect_constant += term
        L += 5451401
        X *= -262537412640768000
        K += 12
        M *= (K ** 3 - 16 * K) / (current_iteration + 1) ** 3

        term = Decimal((M * L) / X)

    incorrect_constant = C * incorrect_constant ** (-1)

    return incorrect_constant
