from aiohttp import web
import pac_mode_a as pm


routes = web.RouteTableDef()


@routes.get('/')
async def print_class(request):
    i_am = pm.moduleA.class_im('this need print')
    i_am.print_im()
    return web.Response(text="test for InStat (aiohttp)")


@routes.post('/post')
async def post_handler(request):
    pass


app = web.Application()
app.add_routes(routes)
web.run_app(app)

if __name__ == "__main__":
    web.run_app(app)
