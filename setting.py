import logging
from configparser import ConfigParser
import os
from logging.config import fileConfig

import sentry_sdk

SENTRY = os.environ['SENTRY_DSN']
sentry_test_dns= 'https://___14@sentry.io/1___5'
env_name = os.environ["RC_VER"]
sentry_sdk.init(SENTRY or sentry_test_dns, environment= env_name or 'unknow')

cfg = ConfigParser()
cfg.read('cfg.ini')
rc_var=str(cfg['main']['rc_version'])
print (rc_var)
fileConfig('log_cfg.ini')

logger = logging.getLogger('setting')

try:
    rc_var=os.environ["RC_VER"]
    print(rc_var)

except Exception as k:
    logger.error (f'Error environ {k}')

