def sum_of_digits(digit_string: str) -> int:
    if not (digit_string).isdigit():
        raise ValueError("input string must be digit string")
    elif len(digit_string) > 1:
        summ = int(digit_string[-1]) + sum_of_digits(digit_string[:-1])
        return summ
    else:
        return int(digit_string)

print(sum_of_digits('065'))