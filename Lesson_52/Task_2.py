def is_palindrome(looking_str: str, index: int = 0) -> bool:
    mid = len (looking_str) // 2
    if mid > 1:
        return looking_str[0] == looking_str[-1] and (is_palindrome(looking_str[1:-1]))
    else:
        return looking_str[0] == looking_str[-1]


print(is_palindrome('saas'))


