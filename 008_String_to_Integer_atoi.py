class Solution(object):
    def myAtoi(self, input):
        """
        :type str: str
        :rtype: int
        """
        if len(input) == 0:
            return 0
            
        while input[0] == " ":
            input = input[1:]
        accu = 0           
        neg = 1

        if input[0] == "-":
            neg = -1
            input = input[1:]
        elif input[0] == "+":
            neg = 1
            input = input[1:]

        while len(input) > 0:
            num = 0
 
            isNum = False
            for i in range(0,10):
                if input[0] == str(i):
                    isNum = True
                    num = i
            print isNum        
            if not isNum:
                break     
            
            accu = accu * 10 + num

            input = input[1:]
            
        return max(min(neg * accu, pow(2,31)-1), -1 * pow(2,31))
