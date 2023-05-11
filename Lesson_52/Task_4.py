def reverse(input_str: str) -> str:
    if len(input_str) > 1:
        rev_str = input_str[-1]+reverse(input_str[:-1])
        return rev_str
    else:
        return input_str

print(reverse('low'))