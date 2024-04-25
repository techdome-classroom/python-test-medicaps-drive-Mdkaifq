class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        map1 = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in map1.values():
                stk.append(i)
            elif i in map1.keys():
                if stk == [] or map1[i] != stk.pop():
                    return False
            else:
                return False

        return stk == []

    pass



  

