from aiohttp import web
from aiohttp_healthcheck import HealthCheck

from setting import logger
from view import handler_of_userinfo, health_check

app = web.Application()
# app = web.Application(loop=loop, middlewares=middlewares)
app.router.add_route('POST', '/useradd', handler_of_userinfo)
# app.router.add_route('GET', '/{name}', handler)
logger.info('Application started')

health = HealthCheck()
app.router.add_get("/healthcheck", health)
health.add_check(health_check)

