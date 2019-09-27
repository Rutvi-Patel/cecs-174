def findLongestWord(a_str):
    x = a_str.split(" ")
    list = []
    for i in range (len(x)-1,-1,-1):
        for y in range (len(x[i])):
            final = y+1
        list.append(final)
    x = x[::-1]
    return x[list.index(max(list))]
if __name__ == '__main__': ## for your own module test
    print(findLongestWord(input("Enter a sentence: ")))