
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr_wait = 0
        total_wait = 0
        for arrival, time in customers: 
            if arrival > curr_wait: 
                total_wait += time
                curr_wait = arrival + time
            else: 
                total_wait += time + (curr_wait - arrival)
                curr_wait += time
        return total_wait / len(customers)