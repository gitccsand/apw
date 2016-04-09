#----------section1----------------
def fn(args):
	print(args+'\nprinted by fn')
	return 'ok'

import asyncio
def bb(fn,args):
	# fn = asyncio.coroutine(fn)
	y=yield from fn(args)#fn如果是generaor初始化后再执行一次，如果不是generator,则执行完毕后,从fn结束。
	
	if y:
		print(y)
	else:
		print('no y')
#----------------------------------

#----------section2----------------

def fn_g():
	msg = 'i am returned from fn_g'
	while True:
		from_out = yield msg
	
	print('from_out in fn_g:%s'%from_out)
	# return from_out
	return msg

def cc():
	from_out=yield 
	print('from_out in cc:%s'%from_out)
	from_out_covered=yield from fn_g()##fn_g如果是generaor初始化后再执行一次，如果不是generator,则执行完毕后,从fn_g结束。
	if from_out_covered:
		print('from_out_covered covered by fn_g:%s'%from_out_covered)
	else:
		print('nothing returned')

#----------------------------------


def main():

	## test section1
	g = bb(fn,'B***')
	g.send(None)
	next(g)

	## test section2
	# g = cc()
	# g.send(None)
	# g.send('c')
	# g.send('d')

if __name__ == '__main__':
	main()