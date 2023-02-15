from random import randint

print("Let's play the guess game - think of a number from 0 to 100")
x=randint(0,100)

count_enumeration=0

#iterative method
for i in range(0,101):
    count_enumeration+=1
    if i==x:
        print("The number is found!")
        break

print("Your number was ", x, " and it took ", count_enumeration, " iterations for the iterative method to guess it!")

count_random=1

print("Let's play the guess game - think of a number from 0 to 100")

y=randint(0,100)

#random guess method
while x!=y:
    y=randint(0,100)
    count_random+=1

print("Your number was ", x, " and it took ", count_random, " iterations for the random method to guess it!")


from random import randint
right=10000000
left=0

print("Let's play the guess game - think of a number from 0 to 100")
z=randint(left,right)

count_bin=1

mid=(right + left) // 2

while z!=mid:
    print(mid)
    if z<mid: 
        print("less")
        right=mid-1
    else: 
        print("more")
        left=mid+1
    mid=(right + left) // 2
    count_bin+=1

print("Your number was ", z, " and it took ", count_bin, " iterations for the binary algorithm to guess it!")

