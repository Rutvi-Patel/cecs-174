def countWords( sentence ):
    counts = sentence.count(" ")+1
    return counts

print(countWords("thisisonelongword"))