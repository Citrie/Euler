def name_value(name):
    value = 0
    for string in name:
        value += ord(string)-64
    return value

with open('names.txt','r') as f:
    names = f.readline()
f.closed

names = names.replace('"','').split(',')

names.sort()
sumup=0

for i in range(len(names)):
    sumup += (i+1) * name_value(names[i])

print sumup