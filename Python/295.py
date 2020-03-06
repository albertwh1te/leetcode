# 295. Find Median from Data Stream

# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

# For example,
# [2,3,4], the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Design a data structure that supports the following two operations:

# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.


# Example:

# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2


# Follow up:

# If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?


import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, num)
        heapq.heappush(self.max_heap, (-1) * heapq.heappop(self.min_heap))
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, (-1) * heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0] * (-1) + self.min_heap[0]) / 2.0
        else:
            return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
print(obj.findMedian())
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())

