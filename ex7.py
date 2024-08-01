import random
randValue=random.randrange(4)

print(f"You rolled {randValue}")
print("Another random guess", str(random.randrange(1,11))) #you should make it str...
print("yep yeppp random guess", str(range(1,44))) #Take care the output
winners=random.sample(range(100),5)
print(winners)


petList=["Cat","Doge","Monkey"]
print(random.choice(petList)) 

random.shuffle(petList) 
print(petList)

