class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        var map = hashMapOf<Int, Int>()

        for ((key, value) in nums.withIndex()) {
            val k = target - value

            if (k in map) {
                return intArrayOf(map[k]!!, key)
            }
            map[value] = key
        }
        return intArrayOf()
    }
}
