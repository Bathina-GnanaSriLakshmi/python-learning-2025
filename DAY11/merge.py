#To merge two dictionaries
dict1 = {"gnana":5,"sri":3}
dict2 = {"lakshmi": 7}
for j in dict2:
    dict1[j] = dict2[j]
print(dict1)