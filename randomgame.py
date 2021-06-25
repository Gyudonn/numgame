import random

start = input('Input the start num of range')
start = int(start)
end = input('Input the end num of range')
end = int(end)

r = random.randint(start, end)
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

