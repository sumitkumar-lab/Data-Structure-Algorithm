s = "aanagram"

def isAnagram(s: str, t: str) -> bool:
    map={}
    map2={}

    for i in s:
        if i in map:
            map[i]+=1
        else:
            map[i]=1
    for i in t:
        if i in map2:
            map2[i]+=1
        else:
            map2[i]=1
    
    if map == map2:
        return True
    
    return False

s = "anagram"
t = "nagaram"

print(isAnagram(s, t))