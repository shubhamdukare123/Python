def nivenNo(num=1):
    sum = 0
    while(num>0):
        sum = sum + num%10
    if(num%sum == 0):
        return num
    nivenNo(num/10)
for i in range(4):
    for j in range(4):
        print(nivenNo(), end = " ")
    print()



