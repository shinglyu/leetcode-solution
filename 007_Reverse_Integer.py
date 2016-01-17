class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
            
        try:
            neg = x / abs(x)
        except ZeroDivisionError:
            neg = 1
            
        x = abs(x)
        #i = 0
        output = 0
        while x > 0:
            
            output = output * 10 + (x % 10)
            
            x /= 10
        MAXINT=pow(2,31) #32 bit
        if output > MAXINT:
            return 0
        
        return neg * output      
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def count_digits(num, accu):
            if pow(10, accu) > abs(num):
                return accu 
            else:
                return count_digits(num, accu + 1)
                
        output_digits = []
  
            
        try:
            neg = x / abs(x)
        except ZeroDivisionError:
            neg = 1
            
        x = abs(x)
        for i in range(count_digits(x,1)-1, -1, -1): # digits -1 to 0
            output_digits.append(x / pow(10,i) % 10)
        
        output = 0
        for digit in enumerate(output_digits):
            output += pow(10,digit[0]) * digit[1]
        MAXINT=pow(2,31) #32 bit
        if output > MAXINT:
            return 0
        
        return neg * output
"""      
