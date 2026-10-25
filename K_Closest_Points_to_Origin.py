# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
# Input: 
points = [[1,3],[-2,2]]
k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

import heapq, math

def calc_dist(a, b):
    return a ** 2 + b ** 2


def find_nearest(points_, k):
    points = [calc_dist(point[0], point[1]) for i, point in enumerate(points_)]
    heapq.heapify(points)
    while len(points) > k:
        heapq.heappop(points)
    return [points_[points[i][1]] for i in range(k)]
    


if __name__=='__main__':
    # points = [[3,3],[5,-1],[-2,4]]
    # k = 2
    print(find_nearest(points, k))
