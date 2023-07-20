# Create a function named calculate_average that takes a list of numbers as a parameter.
# Inside the function, calculate the average of all the numbers in the given list.
# Return the average.
# Return the average.
def calculate_average():
    lst=[85, 90, 92, 88, 95]
    i=0
    ans=0
    while i<len(lst):
        ans+=lst[i]
        i+=1
    return ans//len(lst)
print(calculate_average())