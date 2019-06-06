string=input("enter the string")
alphabets = digits = special = 0

for i in range(len(string)):
    if(string[i].isalpha()):
        special = special + 1
print("Total Number of Special Characters in this String :  ", special)
