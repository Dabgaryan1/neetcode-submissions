class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        var best = 0
        var l = 0

        var chars = mutableSetOf<Char>()

        for (r in 0 until s.length) {
            while (s[r] in chars) {
                chars.remove(s[l])
                l++
            }
            best = maxOf(best, r-l+1)
            chars.add(s[r])
        }
        return best
    }
}
