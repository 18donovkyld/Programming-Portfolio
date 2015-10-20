# python learning exercises

# Functions
def echo(thing):
	return thing

def swap(thing1, thing2):
	return thing2, thing1

	
def main_function():
	print "testing echo('marco'): ", echo('marco')
	print "testing echo('shut up'): ", echo('no, you shut up')
	print "testing swap('fame', 'fortune')", swap('fame', 'fortune')


#Arithmetic Functions
def reverse(x):
	return -x

def plus(a, b):
	return a + b
	
def diff(x, y):
	return x - y
	
def abs_diff(d, b):
	diff = d - b
	if diff < 0:
		diff *= -1
	return diff
	
def divide(w, p):
	return w / float(p)
	
	
def remainder(w, p):
	return w % p		
	
	
def power(x, e):
	answer = 1 
	for i in range(e):
		answer *= x
	return answer	
		
			
def calculate(a, b, c, d, e):
	return (a + b / d - e) * c		
		
		
def ratio(x, y):
	if float(x) > y:
		return x , y
	else: 
		return y , x
		
		
				
	
def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-3): ", reverse(-3)
	print "testing plus(1, 1): ", plus(1, 1)
	print "testin' diff(12, 5): ", diff(12, 5)
	print "test abs_diff(10, 5): ", abs_diff(10, 5)
	print "test abs_diff(5, 10): ", abs_diff(5, 10)
	print "test divide(10, 2): ", divide(10, 2)
	print "test divide(2, 10): ", divide(2, 10)
	print "test remainer(40, 19): ", divide(40, 19)
	print "test power(2, 3): ", power(2, 3)
	print "test calculate(1, 2, 3, 4, 5): ", calculate(1, 2, 3, 4, 5)
	print "test ratio(3, 1): ", ratio(3, 1)

	

def main():
	main_function()
	main_arithmetic()
	
main()








