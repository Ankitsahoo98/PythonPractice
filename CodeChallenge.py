l1 = []
l2 = []
l3 = []
n = int(input("Enter number of elements: "))
for i in range(n):
    l3.append("a")
for i in range(n):
    l1.insert(i, int(input("Enter order: ")))
for i in range(n):
    l2.insert(i, input("Enter list: "))
d = dict()
for i in range(n):
    d[l1[i]] = l2[i]
for i in range(n):

    if (l1[i] == len(l2[i]) and (d[i + 1] != l2[i])):
        l3[l1[i] - 1] = l2[i].upper()
    elif (d[i + 1] == l2[i]):
        l3[l1[i] - 1] = l2[i]
    else:
        l3[l1[i] - 1] = l2[i].lower()
for i in range(n):
    print(l3[i])
