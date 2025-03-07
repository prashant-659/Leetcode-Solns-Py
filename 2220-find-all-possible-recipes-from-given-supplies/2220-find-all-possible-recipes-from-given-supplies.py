class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph=defaultdict(list)
        indegree=defaultdict(int)

        for recipie, ingredient in zip(recipes, ingredients):
            indegree[recipie]=len(ingredient)

            for ing in ingredient:
                graph[ing].append(recipie)
        
        ans=[]
        q=deque(supplies)
        recipes=set(recipes)

        while q:
            supply=q.popleft()

            if supply in recipes:
                ans.append(supply)
            for recipie in graph[supply]:
                indegree[recipie]-=1

                if indegree[recipie]==0:
                    q.append(recipie)
        return ans