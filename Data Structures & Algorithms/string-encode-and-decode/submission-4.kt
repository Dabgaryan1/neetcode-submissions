class Solution {

    fun encode(strs: List<String>): String {
        var res = ""

        for (s in strs) {
            res += s.length
            res += '#'
            res += s
        }

        return res
    }

    fun decode(str: String): List<String> {
        var res = mutableListOf<String>()
        var i = 0

        while (i < str.length) {
            var count = ""

            while (str[i] != '#') {
                count += str[i]
                i++
            }

            i++ // Skip '#'

            var word = ""
            var j = 0

            while (j < count.toInt()) {
                word += str[i] // Use i instead of j
                i++            // Move through encoded string
                j++            // Count characters read
            }

            res.add(word)
        }

        return res
    }
}