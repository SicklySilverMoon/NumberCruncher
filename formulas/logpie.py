from decimal import Decimal
from formulas.pi import *
from formulas.euler import *


def logpie():
    result = Decimal(euler()).log10() / Decimal(pi().log10())

    return result
