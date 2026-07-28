class Solution(object):
    def twoSum(self, numbers, target):
        x, y = 0, len(numbers)-1
        while x < y:
            z = numbers[x] + numbers[y]
            if z == target:
                return [x+1, y+1]
            elif z < target:
                x += 1
            else:
                 y -= 1
         
        