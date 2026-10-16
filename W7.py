numbers = []

with open("example.txt", "r") as file:
    for line in file:
        num = int(line)
        numbers.append(num)

print("Numbers:", numbers)
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Average:", sum(numbers) / len(numbers))
