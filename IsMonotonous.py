# check if it is always ascending
# check if it is always descending
# return true if one of them is true

class Solution:

    def is_monotonous(lst):

        is_asc = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
        is_desc = all(lst[i] >= lst[i+1] for i in range(len(lst)-1))

        return (is_asc or is_desc)

print(Solution.is_monotonous([1,2,4,5,7]))
print(Solution.is_monotonous([1,2,4,3,5,7]))