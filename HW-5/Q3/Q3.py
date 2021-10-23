def one_edit(string1, string2):
    if (string1 == string2): return True
    elif (s in string2 for s in string1) and (len(string2)-len(string1) == 1): return True
    elif (s in string1 for s in string2) and (len(string1)-len(string2) == 1): return True
    elif (len(string1) == len(string2)):
        k = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                k += 1
                if k > 1: return False
        return True
    return False

one_edit("pale", "ple")
one_edit("pales", "pale")
one_edit("pale", "bale")
one_edit("pale", "bake")