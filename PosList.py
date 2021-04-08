print("Enter your list of numbers:(enter 'x' to end list)",end='\n')
poslist=[]
while True:
    x=input()
    if x=='x':
        break
    x= int(x)
    if x > 0:
        poslist.append(x)
print(poslist)
