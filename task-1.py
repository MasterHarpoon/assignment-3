# TASK 1

inpt = int(input("Enter a number: "))

def func(inpt):
    if inpt<2:
        return 1
    else:
        return inpt * func(inpt-1)
answer = func(inpt)
print(answer)