from decimal import Decimal


def pi():
    pi = Decimal(0)
    term = Decimal(1)
    current_iteration = Decimal(0)

    C = Decimal(426880) * Decimal(10005).sqrt()
    M = Decimal(1)  # names from https://en.wikipedia.org/wiki/Chudnovsky_algorithm
    L = Decimal(13591409)
    X = Decimal(1)  # and yes i understand they're terrible variable names but it makes it easier to follow the page
    K = Decimal(6)

    while pi + term != pi:
        term = (M * L) / X

        pi += term

        L += 545140134
        X *= -262537412640768000
        M *= (K ** 3 - 16 * K) / (current_iteration + 1) ** 3
        K += 12

        current_iteration += 1

    pi = C / pi

    return pi
