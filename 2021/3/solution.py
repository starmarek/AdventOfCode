import collections
import os

with open(os.path.dirname(__file__) + "/data") as data_file:
    data = [line.rstrip() for line in data_file]

len_of_digits = len(data[0])


def get_most_common_bits_in_each_position():
    most_common_bits = ""
    for current_bit_position in range(len_of_digits):
        most_common_bits += get_most_common_bit_in_position(current_bit_position)
    return most_common_bits


def reduce_digits_by_critera(criteria, digits):
    for current_position in range(len_of_digits):
        bit = get_most_common_bit_in_position(current_position, criteria)
        if criteria != 1:
            bit = flip_binary(bit)
        digits = remove_digits_by_bit(bit, current_position, digits)
        if len(digits) == 1:
            break
    return digits


def get_most_common_bit_in_position(position, criteria=1):
    current_position_bits_counted = collections.Counter(
        entry[position] for entry in data
    )
    if current_position_bits_counted["1"] == current_position_bits_counted["0"]:
        return criteria
    return max(current_position_bits_counted, key=current_position_bits_counted.get)


def flip_binary(binary):
    return "".join("1" if x == "0" else "0" for x in binary)


def remove_digits_by_bit(selector_bit, position, digits):
    return [digit for digit in digits if digit[position] == str(selector_bit)]


most_common_bits = get_most_common_bits_in_each_position()
least_common_bits = flip_binary(most_common_bits)

most_common_bits_int = int(most_common_bits, 2)
least_common_bits_int = int(least_common_bits, 2)

print(most_common_bits_int * least_common_bits_int)  # 1


bit_criteria = 1
a = reduce_digits_by_critera(bit_criteria, data.copy())
bit_criteria = 0
b = reduce_digits_by_critera(bit_criteria, data.copy())

a = int(a.pop(), 2)
b = int(b.pop(), 2)

print(a * b)
