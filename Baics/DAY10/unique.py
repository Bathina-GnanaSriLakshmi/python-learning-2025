#To find the number of unique words in the sentence
s = set(map(str,input("Enter the sentence: ").split()))
words = 0
for i in s:
    words += 1
print(f"No. of unique words are {words}")