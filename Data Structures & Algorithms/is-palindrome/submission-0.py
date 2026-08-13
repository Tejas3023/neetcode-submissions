class Solution:
    def isPalindrome(self, s: str) -> bool:
        front,back = 0,len(s)-1
        while front<back:
            while front<back and not self.alphaNum(s[front]):
                front+=1
            while back>front and not self.alphaNum(s[back]):
                back-=1
            if s[front].lower()!=s[back].lower():
                return False
            front,back = front+1, back-1
        return True 
    
    def alphaNum(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))