"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], 
and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
"""

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        num_per = len(costs)/2
        city_a = [a for a,b in costs]
        city_b = sorted([b-a for a,b in costs])
        return sum(city_a) + sum(city_b[:num_per])
