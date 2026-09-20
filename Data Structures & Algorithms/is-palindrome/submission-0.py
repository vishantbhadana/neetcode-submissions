class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1  # .is_al_num() tells us if that character is alphanumeric or not
        while i<j:
            if not s[i].isalnum():
                i+=1
                continue

            if not s[j].isalnum():
                j-=1
                continue
            
            if s[i].lower()!=s[j].lower():
                return False
            
            i+=1
            j-=1
        
        return True

                


