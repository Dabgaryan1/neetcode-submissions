class Solution {
    fun numIslands(grid: Array<CharArray>): Int {
        var count = 0
        if (grid.isEmpty()) {return 0}

        fun dfs(r: Int, c: Int): Unit {
            if (r < 0 || c < 0 || r >= grid.size || c >= grid[0].size) {
                return
            }
            if (grid[r][c] == '0') {
                return
            }
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        }

        for (r in 0 until grid.size) {
            for (c in 0 until grid[0].size) {
                if (grid[r][c] == '1') {
                    count++
                    dfs(r, c)
                }
            }
        }
        return count
    }
}
