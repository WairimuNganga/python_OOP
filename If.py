
#If statement checks if the given statement is true or not.The code 
# inside the if the statement will only be executed if the condition is true.
# x = range(50,100)
# for y in x:
#     if y%2 != 0:
#         print(y)

# x = range(0,100,3)
# for y in x:
#     print(y)

# Given an array of N integers. Find the first element 
# that occurs atleast K number of times.

# def firstElementKTime(self,  a, n, k):
#        d = dict()
#        for i in a:
#            if i not in d: d[i] = 1
#            else: d[i] += 1
#            if d[i]==k:
#                return i
#        return -1
z=0      
z=int(input("Enter your grades: ")) 
if 80<=100:
    print('A')
elif z==70 and z<=79:
    print('B')
elif z==60 and z<=69:
    print('C')
elif z==50 and z<=59:
    print('D')
else:
    print('E')

 