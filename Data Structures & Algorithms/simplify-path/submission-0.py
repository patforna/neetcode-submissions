class Solution:
    # thougths/ideas:
    # - i wonder if we could use a stack for this
    #   - tokenise the path into segments
    #   - 
    #   - process and push each path segment onto the stack in canonical form
    #   - 
    def simplifyPath(self, path: str) -> str:
        stack = []
        segments = [p for p in path.split("/") if p]
        for seg in segments:
            if seg == ".":
                continue
            if seg == "..":
                if stack: 
                    stack.pop()
                continue
            
            stack.append(seg)

        return "/" + "/".join(stack)