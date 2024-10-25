class Trie:
    def __init__(self):
        self.children={} #string -> Trie
        self.end_folder=False
    def add(self,path):
        cur=self
        for f in path.split("/"):
            if f not in cur.children:
                cur.children[f]=Trie()
            cur=cur.children[f]
        cur.end_folder=True

    def prefix_search(self,path):
        cur=self
        folders=path.split("/")

        for i in range(len(folders)-1):
            cur=cur.children[folders[i]]
            if cur.end_folder:
                return True
        return False
        


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie=Trie()


        for f in folder:
            trie.add(f)
        
        res=[]
        for f in folder:
            if not trie.prefix_search(f):
                res.append(f)
        return res


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # folder_set=set(folder)
        # res=[]

        # # O(n*L2)
        # for f in folder:
        #     res.append(f)
        #     for i in range(len(f)):
        #         if f[i]=="/" and f[:i] in folder_set:
        #             res.pop()
        #             break
        # return res

