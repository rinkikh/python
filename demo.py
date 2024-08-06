def substrings(string, substr):
    strlen = len(string)
    substrlen = len(substr)
    count = 0

    for i in range(strlen - substrlen + 1):
        if string[i:i + substrlen] == substr:
            count += 1
            

    return count

string = "abcdfabcfgabc"
substr = "abc"

count = substrings(string, substr)
print(substr)

print(count)  
