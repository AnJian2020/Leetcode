from typing import List

class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum(guess[i]==answer[i] for i in range(len(guess)))

if __name__=="__main__":
    guess = [1,2,3]
    answer = [1,2,3]
    print(Solution().game(guess,answer))

