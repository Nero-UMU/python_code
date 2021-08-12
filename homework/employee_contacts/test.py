f1 = open('address_book.txt')
f1_list = f1.read().splitlines()
f2 = {}
for i in range(1, len(f1_list)+1):
    f3 = f1_list[i-1].split(':')
    f2[i] = f3[1]

print(f2)
