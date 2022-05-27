#Using the while,if and continue print all the numbers between 100 and 200 that are divisible by 5
# x = 100
# y = 200
# while x < y:
#     x+=1
#     if x%5 != 0:
#         continue
#     print(x)
cost = int(input('ENTER COST:'))
if cost>100000:
    print('Tax is 15%')
elif cost>50000 and cost<=1000000:
    print('Tax is 10%')
else:
    print('Tax is 5%')

