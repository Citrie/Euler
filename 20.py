product = 1

for i in range(1,100):
    product*=i
    while not product%10:
        product/=10    

string=str(product)

sumup = 0
for number in string:
    sumup += int(number)

print sumup

