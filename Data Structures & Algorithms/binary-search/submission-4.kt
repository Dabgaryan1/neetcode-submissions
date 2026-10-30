class Solution {
    fun search(nums: IntArray, target: Int): Int {
        var l = 0
        var r = nums.size - 1

        while (l <= r) {
            var mid = (l + r).floorDiv(2)

            if (nums[mid] < target) {
                l = mid + 1
            }
            else if (nums[mid] > target) {
                r = mid - 1
            }
            else {
                return mid
            }
        }
        return -1
    }
}
