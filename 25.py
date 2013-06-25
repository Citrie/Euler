import math 

f1, f2 = 1,1

index1, index2 = 1,2
while f1:
    f1, f2 = f1+f2, f2+f1+f2
    index1, index2 = index1+2, index2+2
    if len(str(f1))>999 or len(str(f2))>999:
        break

print f1, f2
print len(str(f1))>999, len(str(f2))>999
print index1, index2