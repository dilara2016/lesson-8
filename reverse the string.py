#input a word or a sentece
string = input("Please enter youre own string : ")
string2 = ('')
#loop for printing in reverse
for i in string:
    string2 = i+string2

print("/nThe Original String = ", string)
print("/nThe Original String2 = ", string2)