class Solution {
    fun maxProfit(prices: IntArray): Int {
        var best = 0

        var i = 0
        var j = 1

        while (i < prices.size) {
            if (j < prices.size && prices[i] >= prices[j]) {
                i++
                j++
                continue
            }
            while (j < prices.size && prices[j] > prices[i]) {
                best = maxOf(best, prices[j]-prices[i])
                j++
            }
            i = j
            j++
        }
        return best
    }
}
