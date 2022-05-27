#A function that accepts many no of positional arguments.
# greet_mutiple("Mary","Judy","Lisa",'Jelani')
def greet_mutiple (*names):
    # return f"Hello{names}"
    print(names)
    for name in names:
        print(f"Hello{name}")

#Write a function tha accepts ANY NUMBER OF INTERGERS AND RETURNS THE SUM OF
#ALL OF THEM.
def sum(*numbers):
    add = 0
    for number in numbers:
        add+=number
    return add
def multiply(*numbers):
    answer=1
    for number in numbers:
        answer*=number
    return answer