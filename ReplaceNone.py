# traverse list and store previous val that is not null
# append val to list
class Solution:

    def replace_none(lst):
        
        result, prev = [], None

        for val in lst:
            if val != None:
                prev = val

            result.append(prev)

        return result

print('replace_none is', Solution.replace_none([None,1,2,None,None,5,7]))