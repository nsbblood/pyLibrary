import itertools

election ={1: "Barbie", 2:"Karen",3:"Jack"}

for p in itertools.permutations(election):
    print(p)

for p1 in itertools.permutations(election.values()): 
    print(p1)