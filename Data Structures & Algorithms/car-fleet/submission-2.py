class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        index_sort = [] 
        for i in range(len(position)):
            index_sort.append([position[i], (target-position[i])/(speed[i])])

        index_sort.sort(key=lambda x: x[0])
        res = 0 

        while(len(index_sort)>0):
            value = index_sort.pop()[1]


            while len(index_sort)>0 and value >= index_sort[-1][1]: 
                index_sort.pop() 
            
            res += 1 
        
        return res 
            


            
            
        
        

