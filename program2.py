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

        for numeral in reversed(s):
            value = roman_numerals[numeral]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value

        return result







        pass