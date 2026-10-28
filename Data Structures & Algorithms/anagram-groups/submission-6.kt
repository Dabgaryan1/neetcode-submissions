class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val res = hashMapOf<List<Int>, MutableList<String>>()
        for (s in strs) {
            val count = IntArray(26)
            for (c in s) {
                count[c - 'a']++
            }

            res.getOrPut(count.toList()) { mutableListOf() }.add(s)
        }
        return res.values.toList()
    }
}
