

def is_prime(x):
	prime=True
	for i in range(2,x,1) :
		if  x%i==0:
			print("not a prime")
			prime=False
			break
	if prime== True:
		print("prime num")

			

is_prime(7)

def easy(x):
	
	for i in range(2,x,1) :
		if  x%i==0:
			
			return False
			
	return True

easy(7)
		
		
