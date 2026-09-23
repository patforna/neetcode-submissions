from collections import defaultdict, deque


class Solution:
    def canFinish(self, num: int, prs: List[List[int]]) -> bool:
        # thoughts/ideas
        #
        # - find available courses (i.e. without prerequisites)
        # - taken them
        # - remove them from the prerequisites list
        # - find newly available courses
        # - repeat until no more newly available courses
        # - return whether all courses have been taken

        finished = 0

        # create dicts for easier lookup - both ways
        reqs = defaultdict(list)
        dependents = defaultdict(list)
        for course, req in prs:
            reqs[course].append(req)
            dependents[req].append(course)


        # seed with courses that have no prereqs
        available = deque()
        for i in range(num):
            if i not in reqs: 
                available.append(i)
        
        while available:            
            course = available.popleft()
            finished += 1
                
            for dep in dependents[course]: # remove course as a prereq
                reqs[dep].remove(course)
                if not reqs[dep]: # course ub has no more prereqs now
                    available.append(dep)

        return finished == num