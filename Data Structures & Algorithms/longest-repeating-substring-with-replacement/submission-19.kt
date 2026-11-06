class Solution {
    fun characterReplacement(s: String, k: Int): Int {
        var i = 0
        var best = 0
        val freq = mutableMapOf<Char, Int>()

        for (j in 0 until s.length) {
            freq[s[j]] = freq.getOrDefault(s[j], 0) + 1
            var most = freq.values.maxOrNull() ?: 0

            while ((j - i + 1) - most > k) {
                freq[s[i]] = freq[s[i]]!! - 1
                i++
                most = freq.values.maxOrNull() ?: 0
            }

            best = maxOf(best, j - i + 1)
        }

        return best
    }
}