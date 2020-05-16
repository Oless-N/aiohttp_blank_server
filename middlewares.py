import logging
import time

from aiohttp import web

logger = logging.getLogger(__name__)


@web.middleware
async def logging_context_middleware(request, handler):
    # TODO: add logger

    start_time = time.time()

    response = await handler(request)

    logger.info('')

    return response
