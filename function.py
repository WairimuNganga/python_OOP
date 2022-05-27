#They allow us to write code that we can use later.
# We can give functions unique input and generate unique output.
# We can run a function as many time as we want.They only run when called.
# Def,,,Function name,,, then brackets,,,Then colon. 

# def hello():
#     print('Hello AnitaB')
 


#IMPORTING A FUNCTION
#Once a function is defined it can be imported and used in another file.
#from function ie file name,,,import function eg hello()

#Function Arguments.
#A function can accept one or more args

def hello(name,age):
    year=2022-age
    # print("Welcome to AkiraChix")
    #  return
    # print(f"Hello {name},you were born in the year {year}")
    return f"Hello {name},you were born in the year {year}"
    

#SYNTAX RULES
#A function name cannot start with a number,BUT!!! can contain a number.eg Hello2()
#It cannot contain spaces.

#CONVENTIONAL RULES
#A function name should be in lowercase.
#If a function name has more than one word you should 
#combine them using the Underscore(_)
#A function name should REFLECT what it does.

#RETURN KEYWORD
#A function can have an optional return keyword which ends the function and can optionally returns a value.