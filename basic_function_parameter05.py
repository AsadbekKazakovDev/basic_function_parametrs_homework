# Create a function named count_vowels that takes a string as a parameter.
# Inside the function, count the number of vowels (a, e, i, o, u, A, E, I, O, U) in the given string.
# Return the count of vowels.
def count_vowels():
    satr="Hello World!"
    ans=0
    i=0
    while i<len(satr):
        if satr[i] in ('a','e','i','o','u','A','E','I','O','U'):
            ans+=1
        i+=1
    return ans
print(count_vowels())