def anagram(s):
     
    if len(s) % 2 != 0:
        return -1
    
    
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
     
    count_s1 = [0] * 26
    count_s2 = [0] * 26
    
    for char in s1:
        count_s1[ord(char) - ord('a')] += 1
    
    for char in s2:
        count_s2[ord(char) - ord('a')] += 1
    
   
    changes_needed = 0
    for i in range(26):
        changes_needed += abs(count_s1[i] - count_s2[i])
    
     
    return changes_needed // 2

 
test_cases = [
    "aaabbb",
    "ab",
    "abc",
    "mnop",
    "xyyx",
    "xaxbbbxx"
]

for test_case in test_cases:
    result = anagram(test_case)
    print(result)
