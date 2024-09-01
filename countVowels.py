Write a Python Program to Find Vowels From a String

str=input()
vow="AaEeIiOoUu"
count=0
for i in str:
    if i in vow:
        count=count+1
print(count)