import random

random_limit = input("Enter the limit for the random number ")

guess = 0

if random_limit.isdigit():
	random_limit = int(random_limit)

else:
	print("Invalid input")


while True:
	user_number = input("Enter ur guess ")
	random_number = random.randint(0,  random_limit)

	if user_number.isdigit():
		user_number = int(user_number)
		print(f"Random generated number is {random_number}")

		if random_number == user_number:
			print("U got it ")
			guess += 1
			break

		else:
			guess += 1
			continue

	else:
		print("Enter a number next time")



print(f"The number of guesses u took to crack it is {guess}")
