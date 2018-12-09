# python3
import time

def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit

if __name__ == '__main__':
	a, b = map(int, raw_input().split())
	starttime = time.time()
	print(sum_of_two_digits(a, b))
	endtime = time.time()
	time1 = endtime - starttime
	print time1