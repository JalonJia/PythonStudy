j = int(input('请输入一个数字:'))

if (j >= 0) and (j < 10):
	print('这个数字是一位数。')
elif (j >= 10) and (j < 100):
	print('这个数字是两位数。')
elif (j >= 100) and (j < 1000):
	print('这个数字是三位数。')
elif (j >= 1000) and (j < 10000):
	print('这个数字是四位数。')
elif (j >= 10000) and (j < 100000):
	print('这个数字是五位数。')
elif (j > 100000) or (j == 100000):
	print('这个数字太大了。')
else:
	print('不知道什么情况')	