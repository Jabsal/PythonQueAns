# split sentence into words
# sum of len divided by len of list

class Solution:

    def Average_Length(sentence):

        lst = sentence.split()
        result = sum(len(word) for word in lst) / len(lst)
        return result

print(Solution.Average_Length("I am blessed and highly favoured"))