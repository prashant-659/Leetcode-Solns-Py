class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        # cur=""
        # for p in path +"/":
        #     if p=="/":
        #         if cur=="..":
        #             if stack:
        #                 stack.pop()
        #         elif cur!="" and cur!=".":
        #             stack.append(cur)
        #         cur=""
        #     else:
        #         cur+=p
        # return "/"+"/".join(stack)                
        stack=[]
        paths=path.split("/")
        for cur in paths:
            if cur=="..":
                if stack:
                    stack.pop()
            elif cur!="" and cur!=".":
                stack.append(cur)
        return "/"+"/".join(stack)

        

            
