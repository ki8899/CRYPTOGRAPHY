l1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
      'X', 'Y', 'Z']

keyword = input("Enter the text: ").upper()
ind = []

l2 = []
for i in keyword:
    if i not in l2:
     if i != " ":
            l2.append(i)

for j in l1:
    if j not in l2:
        if j != " ":
            l2.append(j)

print(l2)
ch = int(input("Enter the process: \n1)Encryption \n2)Decryption\t:"))

if ch == 1:
    pt = input("Enter the plain text: ").upper()
    k = int(input("Enter the k value: "))
    for i in pt:
        if i in l2:
            x = l2.index(i)
            cip = (x + k) % 26
            ind.append(l2[cip])

    for i in ind:
        print(i, end="")
if ch == 2:
    pt = input("Enter the cipher text: ").upper()
    k = int(input("Enter the k value: "))
    for i in pt:
        if i in l2:
            x = l2.index(i)
            cip = (x - k) % 26
            ind.append(l2[cip])

    for i in ind:
        print(i, end="")
