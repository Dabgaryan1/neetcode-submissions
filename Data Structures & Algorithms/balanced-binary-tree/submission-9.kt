/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun isBalanced(root: TreeNode?): Boolean {
        var balanced = true
        fun dfs(node: TreeNode?): Int {
            if (node == null) { return 0 }

            val left = dfs(node.left)
            val right = dfs(node.right)
            if (abs(left - right) > 1) {
                balanced = false
            }
            return 1 + maxOf(left, right)
        }
        dfs(root)
        return balanced
    }
}
