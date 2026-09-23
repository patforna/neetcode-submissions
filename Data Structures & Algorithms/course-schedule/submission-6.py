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

        finished = []

        # create dict for easier lookup
        reqs = defaultdict(list)
        used_by = defaultdict(list)
        for course, req in prs:
            reqs[course].append(req)
            used_by[req].append(course)


        # seed with courses that have no prereqs
        available = deque()
        for i in range(num):
            if i not in reqs: 
                    available.append(i)
        
        while available:            
            course = available.popleft()
            if course not in finished:
                finished.append(course)
                
                for ub in used_by[course]: # remove course as a prereq
                    reqs[ub].remove(course)
                    if not reqs[ub]: # course ub has no more prereqs now
                        available.append(ub)

        return len(finished) == num