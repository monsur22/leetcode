a = input(("Enter a string:"))
reverse = a[::-1]
print (reverse)
if a == reverse:
    print ("Palindrome")
else:
    print ("Not a Palindrome")
# leetcode
    # if x<0:
    #         return False
    #     n = int(str(x)[::-1])
    #     if n == x:
    #         return True
    #     return False
