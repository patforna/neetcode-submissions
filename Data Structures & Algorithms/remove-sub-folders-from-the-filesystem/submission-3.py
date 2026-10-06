# thoughts/ideas:
# - put every folder path in a hash set - O(n) time & space
# - for each folder path
#   - iterate over parent paths, starting with shortest (i.e. /a/b/c -> /a) - O(n * max path segments)
#   - if parent path is in in hash set, skip
#   - if none of the parent paths are in the hash set, add to result list


class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folder_set = set(folders)
        result = []

        for f in folders:
            should_add = True
            segments = f.split("/")
            for i in range(1, len(segments) - 1):
                parent_path = "/".join(segments[0 : i + 1])
                if parent_path in folder_set:
                    should_add = False
                    break

            if should_add:
                result.append(f)

        return result


# /a/b
# parents=["", "a", "b"], len=3, range=(1, 2)=>[1], "/a"
