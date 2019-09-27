def testForAnagram(first,second):
    if (sorted(first) == sorted(second)):
        return "Anagram"
    else:
        return "Different words"
print(testForAnagram("bored".lower(),"robeb".lower()))
