try:
	print(num)
	open('xxx.txt')
except NameError:
	print('我糙')
finally:
	print('我插')

