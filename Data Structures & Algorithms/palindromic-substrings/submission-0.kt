class Solution {
    fun countSubstrings(s: String): Int {
        var res = 0

        for (c in 0..s.length) {
            var l = c
            var r = c
            while (l >= 0 && r < s.length && s[l] == s[r]) {
                res++
                l--
                r++
            }

            var left = c
            var right = c + 1
            while (left >= 0 && right < s.length && s[left] == s[right]) {
                res++
                left--
                right++
            }
        }
        return res

    }
}
