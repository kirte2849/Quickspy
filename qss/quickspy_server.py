from aiohttp import web


#inition database here
from dao_mongo import Client
db = Client()
######################


class Server:

    def __init__(self):
        pass

    async def handle_intro(self, request):
        return web.Response(text="Hello, world")

    async def handle_greeting(self, request):
        name = request.match_info.get('name', "Anonymous")
        txt = "Hello, {}".format(name)
        return web.Response(text=txt)

handler = Server()

#Add http server actions here
handers=[web.get('/intro', Server.handle_intro),
         web.get('/greet/{name}', Server.handle_greeting),
         #web.get('', ),
         ]

#start http server here
app = web.Application()
app.add_routes(handers)