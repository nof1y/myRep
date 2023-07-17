def isPalindrom(s1 = input()):

    s2 = s1[::-1]
    
    print("s1 = " + s1, "s2 = " + s2)

    if s1 == s2:
        return True
    else:
        return False


print(isPalindrom())
