from imports import *

print("1: Euler's constant (e)")
print("2: The golden ratio (φ)")
print("3: Apéry's constant (ζ(3))")
print("4: pi (π)")
print("5: incorrect pi calculation (!π)")
print("6: log base π of e")
formula = int(input("Enter the formula you want to calculate: "))

digits = int(input("Enter number of digits of the constant to calculate: "))
getcontext().prec = digits + 50  # +50 for accuracy which gets cut off later

Switcher = {
    1: euler(),
    2: golden_ratio(),
    3: aperys(getcontext().prec),
    4: pi(),
    5: incorrect(),
    6: logpie()
}

result = Switcher[formula]

result = Decimal(
    str(result)[:digits + 2])  # +2 to preserve digits as the decimal point and number before the decimal count

print(result)
