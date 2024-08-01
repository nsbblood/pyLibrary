myFile= open("textfile.txt","w")

print("Name " + myFile.name)
print("Mode " + myFile.mode)

myFile.write("\n ABC: 100 \n DCF: 99 \n KKK: 85") # \n 
myFile.close()

myFile=open("textfile.txt", "r")
print("Reading..."+ myFile.read(10))
myFile.close()

myFile=open("textfile.txt", "r")
print("Reading..."+ myFile.read(10))
