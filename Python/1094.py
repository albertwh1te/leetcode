# 1094. Car Pooling

# Hint
# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

# You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

# Example 1:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
# Example 2:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true
 

# Constraints:

# 1 <= trips.length <= 1000
# trips[i].length == 3
# 1 <= numPassengersi <= 100
# 0 <= fromi < toi <= 1000
# 1 <= capacity <= 105

from heapq import heappush, heappop

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        trips = sorted(trips, key=lambda x: x[1])
        current_passengers = 0

        min_heap = []
        
        for item in trips:
            num_passengers, from_location, to_location  = item

            current_passengers += num_passengers

            while min_heap and min_heap[0][0] <= from_location:
                _, num_passengers_out = heappop(min_heap)
                current_passengers -= num_passengers_out

            if current_passengers > capacity:
                return False

            heappush(min_heap, (to_location, num_passengers))

        return True
        
if __name__ == "__main__":
    trips = [[2,1,5],[3,3,7]]
    capacity = 4
    result = Solution().carPooling(trips=trips,capacity=capacity)
    print(result)
    assert result==False,"example 1 is wrong"

    trips = [[2,1,5],[3,3,7]]
    capacity = 5
    result = Solution().carPooling(trips=trips,capacity=capacity)
    print(result)
    assert result==True,"example 2 is wrong"