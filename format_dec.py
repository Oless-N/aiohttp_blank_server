import logging
import os

from setting import cfg


class _Formatter(logging.Formatter):
    def format(self, record):
        env_name = os.environ.get("RC_VER") or 'local'
        record.env_name = env_name
        return super(_Formatter, self).format(record)
