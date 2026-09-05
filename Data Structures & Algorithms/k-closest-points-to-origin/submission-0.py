class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            dis.append([dist, x, y])

        heapq.heapify(dis)
        res = []

        while k > 0:
            dist, x, y = heapq.heappop(dis)
            res.append([x, y])
            k -= 1
        return res