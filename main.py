from aiohttp import web

from application import app
from setting import cfg

web.run_app(app, port=cfg["server"]['port'], host=cfg["server"]['host'])

"""
web.run_app(app, *, host=None, port=None, path=None, sock=None,
            shutdown_timeout=60.0, ssl_context=None,
            print=print, backlog=128, access_log_class=helpers.AccessLogger,
            access_log_format=helpers.AccessLogger.LOG_FORMAT,
            access_log=access_logger, handle_signals=True,
            reuse_address=None, reuse_port=None):
"""