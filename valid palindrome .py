    def isPalindrome(self, s: str) -> bool:
       
        n=''
        for i in s.lower():
            if i.isalpha() or i.isnumeric():
                n+=i
        if n== n[::-1]:
            return True
        return False
        
