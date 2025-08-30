numbers= []
for i in range(1,6):
    numbers.append(i)
print(numbers)





numbers= [i for i in range(1,6)]









numbers= [i for i in range(1,11) if i % 3 == 0]
print(numbers)











animals=["dog", "cat", "parrot"]
for index, animals in enumerate(animals):
    print(f"{index + 1}- {animals}")