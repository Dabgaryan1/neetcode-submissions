class Solution {
    fun maxProfit(prices: IntArray): Int {
        var best = 0
        var min = prices[0]

        for (p in 0 until prices.size) {
            min = minOf(min, prices[p])
            best = maxOf(best, prices[p] - min)
        }
        return best
    }
}
