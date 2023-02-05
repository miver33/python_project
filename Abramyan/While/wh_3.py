n: int = int(input("enter n "))
k: int = int(input("enter k "))

counter: int = 0
while n >= k:

    n = n - k
    counter = counter + 1



print("частное равно", counter)
print("остаток деления равен", n)




