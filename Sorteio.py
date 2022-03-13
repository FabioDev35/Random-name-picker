from random import randint
import time
amount = int(input("\nWrite how many names you want to draw: "))
names = []
for x in range(amount):
    k = input("Write a name: ")
    names.append(k)

random_number = randint(0, len(names))

name_number = (random_number - 1)

random_name = names[name_number]

print("\nThe selected name is: " + random_name + "!!" + " Congratulations!")

time.sleep(5)
