class Solution {
    fun isValid(s: String): Boolean {
        val stack = ArrayDeque<Char>()

        for (c in s) {
            if (c == '(' || c == '[' || c == '{') {
                stack.addLast(c)
            }
            else if (c == ')') {
                if (stack.isNotEmpty() && stack.last() == '(') {
                    stack.removeLast()
                }
                else {return false}
            }
            else if (c == ']') {
                if (stack.isNotEmpty() && stack.last() == '[') {
                    stack.removeLast()
                }
                else {return false}
            }
            else if (c == '}') {
                if (stack.isNotEmpty() && stack.last() == '{') {
                    stack.removeLast()
                }
                else {return false}
            }
        }
        return stack.isEmpty()
    }
}
