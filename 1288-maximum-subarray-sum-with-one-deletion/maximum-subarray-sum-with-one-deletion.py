class Solution(object):
    def maximumSum(self, arr):
        no_del = arr[0]
        one_del = arr[0]
        max_sum = arr[0]

        for i in range(1, len(arr)):
            one_del = max(no_del, one_del + arr[i])
            no_del = max(arr[i], no_del + arr[i])
            max_sum = max(max_sum, no_del, one_del)

        return max_sum    

        