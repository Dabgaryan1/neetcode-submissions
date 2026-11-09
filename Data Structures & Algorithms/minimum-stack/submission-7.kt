class MinStack() {
    var stack = ArrayDeque<Int>()
    var minStack = ArrayDeque<Int>()

    fun push(`val`: Int) {
        stack.addLast(`val`)
        if (minStack.isEmpty()) {
            minStack.addLast(`val`)
        }
        else {
            minStack.addLast(minOf(`val`, minStack.last()))
        }
        
    }

    fun pop() {
        stack.removeLast()
        minStack.removeLast()
    }

    fun top(): Int {
        return stack.last()
    }

    fun getMin(): Int {
        return minStack.last()
    }
}
