def fn(args):
	print(args+' printed by fn')

def aa(f):
	f('****')

def main():

	a=None
	fn='hello'
	if callable(fn):
		a=fn
	aa(a or print)

if __name__ == '__main__':
	main()