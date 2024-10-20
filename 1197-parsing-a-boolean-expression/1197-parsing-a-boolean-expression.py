class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        s=expression
        i=0
        def helper():
            nonlocal i
            c=s[i]
            i+=1
            if c=="t":
                return True
            if c=="f":
                return False
            if c=="!":
                i+=1
                res= not helper()
                i+=1
                return res
            
            child=[]
            i+=1
            while s[i]!=")":
                if s[i]!=',':
                    child.append(helper())
                else:
                    i+=1
                # $(t,f,&,(t,f))

            i+=1
            if c=="&":
                return all(child)

            if c=="|":
                return any(child)
        return helper()