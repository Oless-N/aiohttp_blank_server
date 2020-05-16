from aiohttp import web
import json
from setting import cfg
from models import User, __await_insert__, __await_get__


async def handler_of_userinfo(request):
    body = (await request.read()).decode("utf-8").replace("'", '"')
    # header = request.headers
    try:
        body = json.loads(body)
    except Exception as e:
        return web.Response(text=str(e))
    current_user = User(body['name'], body['age'], body['city'])
    await __await_insert__(current_user)
    cursor_to_search = current_user.id
    check_user_fromdb = await __await_get__('id', cursor_to_search)
    if check_user_fromdb[0]['id'] == current_user.__dict__['id']:
        return web.json_response(text=f"data saved and processed {True}", status=200)
    else:
        return web.json_response(text=f"can not save or processing data {False}", status=400)


async def health_check():
    return True, f"{cfg['main']['title']} helth is ok"
