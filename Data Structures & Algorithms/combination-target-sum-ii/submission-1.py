class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # thoughts/ideas:
        # backtracking - generate tree of combinations on the fly an record paths that sum to target

        result = []
        candidates.sort() # so we can de-dupe
        def dfs(start, path):
            cur_sum = sum(path)
            if cur_sum > target:
                return

            if cur_sum == target:
                result.append(path.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]: # don't start with the same number twice
                    continue

                path.append(candidates[i])
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])

        return result