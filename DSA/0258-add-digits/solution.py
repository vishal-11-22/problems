class Solution:
    def addDigits(self, num: int) -> int:
        def add_num(num):
            tot=0
            while(num):
                tot+=num%10
                num=num//10
            return tot
                
        while num>=10:
            num=add_num(num)
        return num