from decimal import Decimal
from pi import *
from euler import *


def logpie():
    result = Decimal(euler()).log10() / Decimal(pi().log10())

    return result
