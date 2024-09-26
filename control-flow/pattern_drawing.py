pattern = int(input("Enter the size of the pattern: "))

count = 0
while count < pattern:
    for i in range(pattern):
        print("*", end="")
    print()
    count += 1