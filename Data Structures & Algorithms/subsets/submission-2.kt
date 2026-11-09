class Solution {
    fun subsets(nums: IntArray): List<List<Int>> {
        var res = mutableListOf<List<Int>>()

        var subset = mutableListOf<Int>()

        fun dfs(i: Int): Unit {
            if (i >= nums.size) {
                res.add(subset.toList())
                return
            }
            subset.add(nums[i])
            dfs(i + 1)

            subset.removeLast() 
            dfs(i + 1)
        }
        dfs(0)
        return res
    }
}
