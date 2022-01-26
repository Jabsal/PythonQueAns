# traverse list and store them in dictionary
# get the difference between target and current value in the list
# If the result is in dictionary, return the indices of the 2

class Solution:

    def sum_two_numbers(lst, target):

        dic = {}

        for idx, val in enumerate(lst):
            
            second_num = target - val
            if second_num in dic:
                return [dic[second_num], idx]
            else:
                dic[val] = idx

print(Solution.sum_two_numbers([1,2,3,5,6,7], 11))

        