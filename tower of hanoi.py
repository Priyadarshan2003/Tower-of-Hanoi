# tower of hanoi
# coded by NSP
a=[]
b=[]
c=[]
print("Tower of Hanoi\n")
print("max no of disks is 20\n")
n=int(input("Enter the no of disks : "))
if n>20:
    n=20
for i in range(0,n):
        a.append(n-i)
print(f"Initial state : \na = {a}\nb = {b}\nc = {c}\n\n")
y=2**n-1
print(f"The no of steps required is : {y}\n")
q=0
while(q<30000000):
    q+=1
i=1
def tower(n, start, end, spare):
    # n is the number of disks
    global i
    if n==1:
        end.append(start.pop())
        print(f"Step {i} :")
        i+=1
        print(f"a = {a}\nb = {b}\nc = {c}\n")
    else:
        tower(n-1, start, spare, end)
        end.append(start.pop())
        print(f"Step {i} :")
        i+=1
        print(f"a = {a}\nb = {b}\nc = {c}\n")
        tower(n-1, spare, end, start)
    return i-1
x=tower(n, a, c, b)
print(f"The no of steps taken is : {x}")
if y==x:
    print("\nSuccess")
while(q<100000000):
    q+=1
