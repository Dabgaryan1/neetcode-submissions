class Solution {
    fun maxArea(heights: IntArray): Int {
        var best = 0
        var i = 0
        var j = heights.size - 1

        while (i < j) {
            best = maxOf(best, minOf(heights[i], heights[j]) * (j - i))

            if (heights[i] <= heights[j]) {
                i++
            }
            else {
                j--
            }
        }
        return best
    }
}
