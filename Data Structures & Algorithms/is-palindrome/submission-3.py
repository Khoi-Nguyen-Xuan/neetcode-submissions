class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s)
        size = len(clean_s)

        for i in range(int(size/2)):
            if clean_s[i].lower() != clean_s[size-1-i].lower():
                return False
        
        return True 
        