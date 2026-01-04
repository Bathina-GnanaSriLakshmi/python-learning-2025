#To count words ending with specific letter
sent = input("Enter sentence: ")
l = list(sent.split())
for i in l:
    if i.lower().endswith('i'):
        print(i)