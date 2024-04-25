class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_value = 0

    for numeral in reversed(roman):
        value = roman_numerals[numeral]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result

# Test the function
print(roman_to_int("III"))    # Output: 3
print(roman_to_int("IV"))     # Output: 4
print(roman_to_int("IX"))     # Output: 9
print(roman_to_int("LVIII"))  # Output: 58
print(roman_to_int("MCMXCIV"))# Output: 1994





        pass