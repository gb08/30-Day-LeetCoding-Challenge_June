"""
Problem:
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), 
where h is the height of the person and k is the
number of people in front of this person who have a height greater than or equal to h.
Write an algorithm to reconstruct the queue.
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: (x[0], -x[1]))
        # Initialize the final list with 0
        queue = [0] * len(people)

        for height, num in people:
            zero_count, idx = 0, 0
            while zero_count <= num:
                if queue[idx] == 0:
                    zero_count += 1
                idx += 1
            queue[idx - 1] = [height, num]
        return queue

