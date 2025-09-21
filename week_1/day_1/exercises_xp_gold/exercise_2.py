for i in range(1, 20):
    print(i)

print("----------------------------------")
numbers = list(range(1, 21))
for index in range(len(numbers)):
    if index % 2 == 0:
        print(numbers[index])
    