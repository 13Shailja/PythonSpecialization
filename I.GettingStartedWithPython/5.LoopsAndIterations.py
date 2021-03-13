#%% Assignment 5.2

# ================================================================================================================
# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message 
# and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
# ================================================================================================================


largest = None
smallest = None

while True:
    svalue = input("Enter a number: ")
    if svalue == "done":
        break
    try:
        ivalue = int(svalue)
    except:
        print("Invalid input")
    	continue
    if smallest is None:
        smallest = ivalue
    elif ivalue < smallest:
        smallest = ivalue
    if largest is None:
        largest = ivalue
    elif ivalue > largest:
        largest = ivalue

print("Maximum is", largest)
print("Minimum is", smallest)




# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done" : break
#     print(num)

# print("Maximum", largest)





# Invalid input
# Maximum is 10
# Minimum is 2
