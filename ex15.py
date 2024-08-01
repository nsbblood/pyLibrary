from datetime import datetime

now=datetime.now()

print(now.strftime("%a %A %d"))
print(now.strftime("%b %B %m"))
print(now.strftime("%A %B %d"))
print(now.strftime("%A %B %d %m"))

print(now.strftime("%H: %M : %S %p")) #time 

print(now.strftime("%y %Y")) #year