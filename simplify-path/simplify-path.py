class Solution:
    def simplifyPath(self, path: str) -> str:
        #keep a stack as you go down
        #construct the path after all operations
        path = path.split("/")
        stack = []
        for directory in path:
            if directory == "":
                # the case with multiple slashes
                continue
            elif directory == ".":
                continue
            elif directory == "..":
                if not stack:
                    #directory is empty
                    continue
                stack.pop()
            else:
                stack.append(directory)
        return "/"+"/".join(stack)