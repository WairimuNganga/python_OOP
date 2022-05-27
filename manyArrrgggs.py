#A function that accepts any number of keyword arguments.
#A function that accepts any njmber of keyword arguments.
def greet_multiple(**kwargs):
    # print(kwargs)
    # print(kwargs.keys())
    # print(kwargs.values())
    keys=kwargs.keys()

    if "country" in keys:
        print (f"Hello,{kwargs['name']},you are from {kwargs['country']}")
    elif "age" in keys:
        year = 2022-kwargs["age"]
        print(f"Hello,{kwargs['name']},you were born in,{year}")
    elif not kwargs:
        print("Helllo anonymous")
def sum_and_greet(*Args,**kwargs):
        sum=0 
        for num in Args:
            sum+=num
        keys= kwargs.keys()
        if"name" in keys:
            print(f"Hello{kwargs['name']} the answer is {sum}")

        elif "country" in keys:
            print(f"Hello,from {kwargs['country']},the answer is {sum}")

        elif not kwargs:
            print("Hello Anonymous")