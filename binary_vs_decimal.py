from typing import Callable

def decimal_to_binary(num: int, result = '') -> str:
    if num == 0:
        if result == '':
            return '0b0'
        return '0b' + result[::-1]
    modulo = num % 2
    result += str(modulo)
    num = num // 2
    return decimal_to_binary(num, result)

def binary_to_decimal(num_str: str) -> int:
    num = num_str[2:]
    number_of_powers = len(num)
    num_dec = 0
    for i in range(number_of_powers):
        num_dec += int(num[-(i+1)]) * 2 ** i
    return num_dec
