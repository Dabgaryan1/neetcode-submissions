class Solution {
    fun characterReplacement(s: String, k: Int): Int {
        val chars = hashMapOf<Char, Int>()
        var best = 0

        var l = 0
        var r = 0

        while (r < s.length) {
            chars[s[r]] = chars.getOrDefault(s[r], 0) + 1

            while ((r - l + 1) - (chars.values.maxOrNull() ?: 0) > k) {
                chars[s[l]] = chars.getOrDefault(s[l], 0) - 1
                l++
            }

            best = maxOf(best, r - l + 1)
            r++
        }

        return best
    }
}