def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: 
            return False
        while n % 2 == 0:
            n /= 2
        return n==1 
       or '''        return n > 0 and bin(n).count('1') == 1'''
