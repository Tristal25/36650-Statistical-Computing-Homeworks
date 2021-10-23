def panlindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] == string[-1]:
        string = string[1:-1]
        return panlindrome(string)
    else:
        return False



panlindrome("kayak")
panlindrome("hello")

