def reverseString(a_str):
    lis = a_str.split(" ")
    final = []
    print(lis)
    for x in range(0,len(lis),2):
        for i in range(1):
            revers = lis[x]
            final.append(revers[::-1])
            if x+1<len(lis):
                final.append(lis[x+1])
    return ' '.join(final)


if __name__ == '__main__': ## for your module test
    print(reverseString(input("Enter a sentence: ")))