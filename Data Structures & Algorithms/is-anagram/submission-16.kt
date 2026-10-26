class Solution {
    fun isAnagram(s: String, t: String): Boolean {

        if (s.length != t.length) {
            return false
        }

        val smap = hashMapOf<Char, Int>()
        val tmap = hashMapOf<Char, Int>()

        for (c in s) {
            smap[c] = smap.getOrDefault(c,0) + 1
        }

        for (c in t) {
            tmap[c] = tmap.getOrDefault(c,0) + 1
        }

        return smap == tmap
    }
}
