# import re
#
# print(bool(re.match(
#     r'^'
#     r'(?!.*(.).\1.*(.).\2)'
#     r'(?!.*(.)(.)\3\4)'
#     r'[1-9]\d{5}'
#     r'$', input()
# )))

# regex_integer_in_range = r"_________"    # Do not delete 'r'.
# regex_alternating_repetitive_digit_pair = r"_________"    # Do not delete 'r'.
#
#
# import re
# P = input()
#
# print (bool(re.match(regex_integer_in_range, P))
# and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# import re
# postcode = input()
#
# # make sure it is between 100000 and 999999
# is_valid_1 = re.match(r"^[1-9][0-9]{5}$", postcode) != None
#
# # make sure it has no more than one alternating digit pair
# is_valid_2 = len(re.findall(r"(?=(([0-9])[0-9]\2))", postcode)) <= 1
#
# print(is_valid_1 and is_valid_2)

# import re
#
# P = input()
#
# regex_integer_in_range = r'^[1-9][\d]{5}$'  # Do not delete 'r'.
# regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'  # Do not delete 'r'.
#
# print (bool(re.match(regex_integer_in_range, P))
#        and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)