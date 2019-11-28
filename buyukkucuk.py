a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if(a==b) and(b==c):
    pass
else:
    if(a>b) and(a>c):
        print(a,"en boyukdur")
    elif(b>a) and(b>c):
        print(b,"en boyukdur")
    elif(c>a) and(c>b):
        print(c,"en boyukdur")
    if(a<b) and(a<c):
        print(a,"en kicikdir")
    elif(b<a) and(b<c):
        print(b,"en kicikdir")
    elif(c<a) and(c<b):
        print(c,"en kicikdir")
