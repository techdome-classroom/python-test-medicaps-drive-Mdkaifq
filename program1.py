class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values():
                stk.append(char)
            elif char in mapping.keys():
                if stk == [] or mapping[char] != stk.pop():
                    return False
            else:
                return False

        return stk == []

    pass



  

