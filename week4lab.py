def meaning(someString):
    if ":)" in someString:
        return 1
    if "-.-" in someString:
        return 2
    if ":(" in someString:
        return 3
    if ":O" in someString:
        return 4
    if ":P" in someString:
        return 5
    else:
        return 0

def scoring(someString):
    score = -5
    for i in range(len(someString)):
        if 'a' or 'e' or 'i' or 'o' or 'u' == someString[i]:
            score += 5
        if 'j' or 'q' or 'x' or 'z' == someString[i]:
            score -= 4 * i  
        if len(someString) % 2 == 0:
            score *= 2 
        else:
            score *= 1.0
    return score

print(scoring('asdfghjkkl123456'))