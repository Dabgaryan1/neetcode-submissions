import kotlin.math.ceil

class Solution {
    fun minEatingSpeed(piles: IntArray, h: Int): Int {
        var sol = Int.MAX_VALUE

        var l = 1
        var r = piles.max()

        while (l <= r) {
            val m = (l + r).floorDiv(2)
            var count = 0L

            for (i in 0 until piles.size) {
                count += ceil(piles[i].toDouble() / m).toInt()
            }

            if (count > h) {
                l = m + 1
            }
            else {
                sol = minOf(sol, m)
                r = m - 1
            }
        }
        return sol
    }
}
