class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping={')', '(', '}', '{', '[', ']' }
        for char in s:
            top= stack.pop() if stack else '#'
            if mapping[char]!=top:
                return False
            else:
                stack.append


        pass
    



  

