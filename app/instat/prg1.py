from aiohttp import web
import pac_mode_a as pm
import iks_zero as iz

routes = web.RouteTableDef()


@routes.get('/')
async def print_class(request):
    i_am = pm.moduleA.class_im('this need print')
    i_am.print_im()

    my_game = iz.main_iz.game_place()
    game_st = my_game.ver_game_state()
    return web.Response(text="test for InStat (aiohttp) "+"статус игры "+ game_st)


@routes.post('/post')
async def post_handler(request):
    pass


app = web.Application()
app.add_routes(routes)
web.run_app(app)

if __name__ == "__main__":
    web.run_app(app)
