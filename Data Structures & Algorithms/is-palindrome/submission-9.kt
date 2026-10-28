class Solution {
    fun isPalindrome(s: String): Boolean {
        var word = ""

        for (c in s) {
            if (c.isLetterOrDigit()) {
                word += c.lowercase()
            }
        }

        var l = 0
        var r = word.length - 1

        while (l < r) {
            if (word[l] != word[r]) {
                return false
            }
            l++
            r--
        }
        return true
    }
}
