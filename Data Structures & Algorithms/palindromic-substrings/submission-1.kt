class Solution {
    fun countSubstrings(s: String): Int {
        var count = 0
        
        for (i in 0..s.length) {
            var l = i
            var r = i

            while (l >= 0 && r < s.length) {
                if (s[l] == s[r]) {
                    count++
                }
                else {
                    break
                }
                l--
                r++
            }

            var l2 = i
            var r2 = i+1

            while (l2 >= 0 && r2 < s.length) {
                if (s[l2] == s[r2]) {
                    count++
                }
                else {
                    break
                }
                l2--
                r2++
            }
        }
        return count
    }
}
