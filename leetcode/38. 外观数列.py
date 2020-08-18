class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return '1'
        prev = self.countAndSay(n - 1) + '*'
        result = ''
        count = 1
        for item in range(len(prev) - 1):
            if prev[item] == prev[item + 1]:
                count += 1
            else:
                result += str(count) + prev[item]
                count = 1
        return result


if __name__ == "__main__":
    print(Solution().countAndSay(6))
