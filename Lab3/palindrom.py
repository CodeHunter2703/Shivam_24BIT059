def ispalindrome(s):
    s=s.split(' ')
    s="".join(s)
    print(s)
    if s[:]==s[:-1]:
        return "palindrome"
    return "not palindrome"
res=ispalindrome("s h i va m ")
print(res)
