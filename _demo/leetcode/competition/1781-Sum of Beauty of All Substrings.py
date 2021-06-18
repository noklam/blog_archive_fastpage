# 1781. Sum of Beauty of All Substrings
# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

from collections import Counter, defaultdict


class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0

        for i in range(len(s)):
            sub_str = s[i:]
            c = Counter(sub_str)
            for j in range(len(sub_str) - 1, 0, -1):
                beauty = c.most_common()[0][1] - c.most_common()[-1][1]
                c[sub_str[j]] -= 1
                if c[sub_str[j]] == 0:
                    del c[sub_str[j]] # Avoid counting 0, delete the key
                total_beauty = beauty + total_beauty
                if beauty == 0:
                    break

        return total_beauty

from collections import defaultdict

class Solution:
    def beautySum(self, s: str) -> int:
        res=0
        n = len(s)        

        for i in range(n-1):
            cnter = [0] * 26 
            cnter[ord(s[i])-ord('a')]+=1
            for j in range(i+1,n,1):
                cnter[ord(s[j])-ord('a')]+=1
                
                min_ = 10000000
                max_ = 0                
                for cnt in cnter:
                    if cnt==0:
                        continue
                    max_ = max(max_,cnt)
                    min_ = min(min_, cnt)
                res+=max_-min_
                
        return res
if __name__ == "__main__":
inp = [
    # "aabcb",
    "rfzobjbnsdmcicbujmytzeygyokslqsierpqrxpfagvbbvdihhtpqdrekxxkezfszykljfqefyvxkwdqldmnpmlvvdxpjeqszaawfilzomtufdltzfeimdpnirjrxfqyexczxaxliqlnpcrhchccnpqczjellcaoofwdogthyzzqbuwxlscyqazsinzrqfcyaczgwnibzmviayqpfjjjdwlzmpecsvuriqolqxmszbjmqwrovsgkggnqxaqjtvwtpzyljflnkxuvkzrknskntdwrvwjvehpkiztbnlgsxdimttdgzppvzzydljsfbaetlpmiutszkxcgetnihosixvjecihsydfkuaurbyxpfpfzibzdlgdsotgztjemxkziedqtnqzxftpqdbpjkdoglyawltujbzodcakofrmbknxl",
]

for ix in inp:
    print(ix, Solution().beautySum(ix))

