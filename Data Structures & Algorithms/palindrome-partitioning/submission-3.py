class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def palindrome(s):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(i, cur):
            if i >= len(s):
                if palindrome(cur[-1]):
                    res.append(cur.copy())
                return
            if not cur or palindrome(cur[-1]):
                cur.append(s[i])
                dfs(i + 1, cur)
                cur.pop()
            
            if cur:
                old = cur[-1]
                cur[-1] += s[i]
                dfs(i + 1, cur)
                cur[-1] = old
        
        dfs(0, [])
        return res