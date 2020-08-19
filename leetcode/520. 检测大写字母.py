class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count=0
        for item in range(len(word)):
            if word[item].isupper():
                count+=1
        if count==1 and word[0].isupper():
            return True
        elif count==len(word):
            return True
        else:
            return False
