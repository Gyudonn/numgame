import random

r = random.randint(1, 100)
count = 1

while True:
	num = input('Please input your answer: ')
	num = int(num)
	if int(num) == r:
		print('Correct')
		print('You gusee the ' + str(count) + ' times.')
		break
	else :
		if num > r:
			print('It is too Big.')
		else :
			print('It is too Small')		
		count = count + 1
		print('Guess again.')

