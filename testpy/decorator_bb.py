
import functools

def get(path):
    '''
    Define decorator @get('/path')
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = path #闭包，可以访问path
        return wrapper
    return decorator

@get('/index')
def aa():
	pass

def main():

	print(aa.__route__)

if __name__ == '__main__':
	main()