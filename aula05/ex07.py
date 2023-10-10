def ispalindrome(s):
    s_inversa = ""
    for i in range(len(s)-1, -1, -1):
        s_inversa += s[i]
    
    return s == s_inversa
