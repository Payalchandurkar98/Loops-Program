#Write a program in Python to find the sum of all even numbers up to 50

sum = 0
for i in range(1, 51):
    if i % 2 == 0:
        sum += i
print("The sum of all even numbers up to 50 is", sum)