class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        map1 = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in map1.values():
                stk.append(char)
            elif char in map1.keys():
                if stk == [] or map1[char] != stk.pop():
                    return False
            else:
                return False

        return stk == []

    pass



  

