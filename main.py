import time

while True:
	i = 0
	ii = 0
	iii = 0
	time_user = int(input('Введіть кількість секунд: '))
	comment = input('Введіть комментар: ')
	for q in range(time_user):
		time.sleep(1)
		i += 1
		print('Пройшло секунд:', i)
		if i % 60 == 0:
			ii += 1
			print('Пройшло хвилин:', ii)
		if i % 3600 == 0:
			iii += 1
			print('Пройшло годин:', iii)

	print('Час сі скінчив!')
	print(comment)