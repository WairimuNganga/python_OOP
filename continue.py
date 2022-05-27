#The continue skips the remainder of the currrent iteration and
#moves to the next iteration to thne loop
x=1
y=20
while x<y:
    x+=1
    if x%2 != 0:
        continue
    print(x)
