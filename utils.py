# utils.py
import re

def enhanced_features(number):
    number = re.sub(r'\D', '', number)
    country_code = number[:2] if len(number) >= 2 else number
    length = len(number)
    contains_999 = '999' in number
    repeating_score = sum(1 for i in range(1, len(number)) if number[i] == number[i-1])
    unique_digits = len(set(number))
    suffix = number[-3:] if len(number) > 3 else number
    return f"{country_code} {length} {contains_999} {repeating_score} {unique_digits} {suffix}"
