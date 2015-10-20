# Python learning exercises

# Functions

def echo(thing):
	return thing
	
	
def swap(x , y):
	return 	y , x
	
def main_function():
	print "Testing echo('marco'): ", echo('marco')
	print "Testing echo('Shut Up'): ", echo('no, you shut up')
	print "Testing swap('fame' , 'fortune'): ", swap('fame' , 'fortune')
	
	
# Arithmetic Functions


def reverse(x):
	return -x
	
def plus(x , y):
	return x + y 
	
def diff(x , y):
	return x - y

def abs_diff(x , y):
	return 

	
def main_arithmetic():
	print "Test reverse(3): ", reverse(3)	
	print "Test reverse(-3): ", reverse(-3)
	print "Test plus(5 , 6): ", plus(5 , 6)
	print "Test diff(3 , 9): ", diff(3 , 9)
	
def main():
	main_function()
	main_arithmetic()
	
	
main()

			
 