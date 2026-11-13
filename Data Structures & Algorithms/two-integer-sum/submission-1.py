class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

            hola=[]
            for j in range(len(nums)):
                i = j+1
                for i in range(len(nums)):
                    if(nums[j]+nums[i]==target and i != j) :
                        hola.append(j)
                        hola.append(i)
                        return hola
            return hola          