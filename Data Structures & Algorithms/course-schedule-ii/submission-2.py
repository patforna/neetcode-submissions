from collections import defaultdict, deque

class Solution:
    def findOrder(self, num: int, prs: List[List[int]]) -> List[int]:
        # thoughts/ideas:
        # 
        # - find all available courses with no prerequisites
        # - take them (keeping track)
        # - remove them as prerequisites from dependent courses
        # - if dependent courses become available, take them
        # - repeat until no more courses available
        # - return taken courses
        # 
        # - use a queue to process available courses
        # - use dicts for looking of prerequisites and dependent courses

        taken = []
        reqs = defaultdict(list)
        dependents = defaultdict(list)
        for c, r in prs:
            reqs[c].append(r)
            dependents[r].append(c)

        available = deque()
        for i in range(num):
            if i not in reqs:
                available.append(i)

        while available:
            course = available.popleft()
            taken.append(course)

            for dep in dependents[course]:
                reqs[dep].remove(course)
                if not reqs[dep]:
                    available.append(dep)
        
        return taken if len(taken) == num else []