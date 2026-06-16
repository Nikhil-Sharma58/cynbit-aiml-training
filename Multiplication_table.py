n = int(input("Enter a number to know its table: "))
print(f"Multiplication table of {n} is:")
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")