# Create a function named find_smallest that takes a list of numbers as a parameter.
# Inside the function, find the smallest number in the given list.
# Return the smallest number.
def find_smallest():
    lst=[4,7,3,9,1,2,6,5]
    i=1
    ans=lst[0]
    while i<len(lst):
        if ans>lst[i]:
            ans=lst[i]
        i+=1
    return ans
print(find_smallest())