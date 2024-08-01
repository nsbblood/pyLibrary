print(min(5,-44,44,32,16))
print(max(5,-44,44,32,16))

print(min('Max','Min'))
print(max('Bob','Alex'))

myGPA= 4.6
print(round(myGPA))
myGPA= 4.4
print(round(myGPA))
myGPA= 4.5
print(round(myGPA))

distanceAway= -13
print(abs(distanceAway))

chanceOfTails= 0.5
inARowTails=3
print(pow(chanceOfTails,inARowTails))

#double your money in 25 years,double it every year

startingBalance= 10000
doublePerYear=1.5
years=20

i=0

while i<years:
    startingBalance=startingBalance*doublePerYear
    startingBalance=startingBalance+10000
    i=i+1
    print(f" {i}. year you will have {startingBalance}")

print(f"You will have {startingBalance} money {years} years later")
