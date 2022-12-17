""" This programs prints out the instructions to solve the problem """


def tower(n,s,a,d):
    if(n==1):
        print('Move the disk from source to destination',s,d)
    else:
        tower(n-1,s,d,a)
        print('Move the disk from source to destination',s,d)
        tower(n-1,a,s,d)
print()
print("Tower of Hanoi-Recursion")
tower(3,1,2,3)
    
