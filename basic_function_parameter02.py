# Create a function named calculate_sum that takes a list of numbers as a parameter.
# Inside the function, calculate the sum of all the numbers in the given list.
# Return the sum.
def calculate_sum():
    lst=[2,4,6,8]
    i=0
    ans=0
    while i<len(lst):
        ans+=lst[i]
        i+=1
    return ans
print(calculate_sum())