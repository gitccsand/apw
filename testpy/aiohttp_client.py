import asyncio
import aiohttp

if __name__ == '__main__':

	# async def fetch_page(client, url):
	#     async with client.get(url) as response:
	#         assert response.status == 200
	#         return await response.read()

	@asyncio.coroutine
	def fetch_page(client, url):
	    response = yield from client.get(url) 
	    assert response.status == 200
	    content = yield from response.read()
	    return content

	loop = asyncio.get_event_loop()
	client = aiohttp.ClientSession(loop=loop)
	css = loop.run_until_complete(
	    fetch_page(client, 'http://172.16.0.5:8080/WageCx/images/newlogin/BasicLayout.css'))
	html = loop.run_until_complete(
	    fetch_page(client, 'http://172.16.0.5:8080/WageCx'))
	print('html:%s ---------------\r css:%s'%(html,css))
	client.close()
