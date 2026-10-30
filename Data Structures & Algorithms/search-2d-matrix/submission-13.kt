class Solution {
    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
        var left = 0
        var right = matrix.size - 1

        while (left <= right) {
            var m = (left + right).floorDiv(2)

            if (target >= matrix[m][0] && target <= matrix[m][matrix[m].size - 1]) {
                var l = 0
                var r = matrix[m].size - 1

                while (l <= r) {
                    var mid = (l + r).floorDiv(2)

                    if (target == matrix[m][mid]) {
                        return true
                    }
                    else if (target < matrix[m][mid]) {
                        r = mid - 1
                    }
                    else {
                        l = mid + 1
                    }
                }
                return false
            }
            else if (target < matrix[m][0]) {
                right = m - 1
            }
            else {
                left = m + 1
            }
        }
        return false
    }
}
