#Program that takes names input and assigns uppercase to first character
#added space in between inputs
name1 = str(input("First name: "))
name2 = str(input("Last name: "))
res1 = name1[0].upper() + name1[1:].lower()
res2 = name2[0:].lower()
print("The full name is: "+ str(res1)+ " " + str(res2))S


