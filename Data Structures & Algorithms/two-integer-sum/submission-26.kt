class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val map = hashMapOf<Int, Int>()

        for ((i, v) in nums.withIndex()) {
            val g = target - nums[i]

            if (map.containsKey(g)) {
                return intArrayOf(map[g]!!, i)
            }
            map[v] = i
        }
        return intArrayOf()
    }
}
