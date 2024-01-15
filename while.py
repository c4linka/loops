number = 0

while number <=5:
    print(number)
    number += 1

number = 15

while number >=0:
    print(number)
    number -=1


print("Hello, I will ask you to write down 4 numbers to sum them up, follow\
the instructions please")

addResult = 0

i = 0
while i < 4:
    x = int(input("Write any number: "))
    addResult += x
    i += 1

print("The result of addition is:", addResult)
