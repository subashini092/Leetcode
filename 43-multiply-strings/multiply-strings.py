class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        Val_1 = 0
        Val_2 = 0
        for i in num1:
            Val_1 = Val_1*10 + (ord(i) - 48)
        for j in num2:
            Val_2 = Val_2*10 + (ord(j) - 48)
        return str(Val_1*Val_2)
        
        
        