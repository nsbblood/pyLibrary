import itertools

for x in itertools.count(50,5):
    print(x)
    if x==44*2+2:
        break

i=0
for c in itertools.cycle("Elisa"): #cycle in words,names etc
    print(c)
    i=i+1
    if i>50:
        break

