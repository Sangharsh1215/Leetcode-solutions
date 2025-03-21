// Last updated: 3/21/2025, 11:55:38 AM
class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        cancook = {s:True for s in supplies }
        recipe_index = {r:i for i,r in enumerate (recipes) }
        def dfs(r):
            if r in cancook:
                return cancook[r]
            if r not in recipe_index:
                return False
            cancook[r] = False

            for nei in ingredients[recipe_index[r]]:
                if not dfs(nei):
                    return False

            cancook[r] = True 
            return cancook[r]
        return [r for r in recipes if dfs(r)]

        
        