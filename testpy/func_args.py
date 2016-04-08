def fn(a,*a1,b=1,**c1):
	print('a=%s'%a)
	print(str(a1))
	print('b=%s'%b)
	print('c2=%s'%c1.get('c2',100))
	print('c3=%s'%c1.get('c3',100))

def aa():
	fn('a',2,3,4,b=1,c1='a',c2=99)

def main():

	aa()

if __name__ == '__main__':
	main()