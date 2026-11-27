from collections import Counter

class Solution:
    # thoughts/ideas:
    # - there are only 26 differnt tasks
    # - count frequencies of tasks, e.g. X:2, Y:2
    # - greedily pick next available task with highest frequency (use max heap)
    # - decrement frequency count and remember when it can processed next (use queue)
    # - increment time and return total
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        heap = [-x for x in count.values()] # max heap
        heapq.heapify(heap)

        time = 0
        queue = deque() # (count, time) tuples

        while heap or queue:
            time += 1

            if heap:
                count = heapq.heappop(heap) + 1 # = decrement
                if -count > 0:
                    queue.append((count, time + n))

            if queue and queue[0][1] <= time:
                count, _ = queue.popleft()
                heapq.heappush(heap, count)

        return time