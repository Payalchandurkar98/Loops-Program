# Write a program in Python to check if a number is divisible by 8 and 12 up to 100 numbers

print("The numbers divisible by 8 and 12 are :")

for i in range(1, 100):
    if i % 8 == 0 and i % 12 == 0:
        print(i)