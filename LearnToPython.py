def convert_to_decimal(number, base):
    decimal_number = 0
    multiplier = 1

    while number > 0:
        digit = number % 10
        decimal_number += digit * multiplier
        multiplier *= base
        number //= 10

    return decimal_number


def convert_from_decimal(number, base):
    result = ""

    while number > 0:
        digit = number % base
        result = str(digit) + result
        number //= base

    return result


number = int(input("Enter the number: "))
current_base = int(input("Enter the current base: "))
target_base = int(input("Enter the target base: "))

decimal_number = convert_to_decimal(number, current_base)
result = convert_from_decimal(decimal_number, target_base)

print("Result:", result)