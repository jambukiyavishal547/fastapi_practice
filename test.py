
# check list pair(first,second) is same parity

l = [1, 2, 3, 4, 5, 5]
flag = 0

for i in range(len(l) - 1):  
    if (l[i] % 2 == 0 and l[i + 1] % 2 == 0) or (l[i] % 2 != 0 and l[i + 1] % 2 != 0):
        flag = 1
        break  
if flag == 1:
    print('same parity found')
else:
    print('same parity not found')


    
for value in range(len(l) - 1):
    def check_parity(value):
        if (l[value] % 2 == 0 and l[value + 1] % 2 == 0):
            return 
        else :
            return 