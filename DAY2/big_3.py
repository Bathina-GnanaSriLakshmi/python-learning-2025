a,b,c = map(int,input("Enter three numbers: ").split())
if a>b and a>c : 
    print(f"{a} is the biggest number")
elif b>c :
    print(f"{b} is the biggest number")
else :
    print(f"{c} is the biggest number")