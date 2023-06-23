import logging

from icecream import ic, install
import logging
import logging.config as log_config

import time


def _prefix_time():
    return f"{time.strftime('%X')}"


def setup_log() -> [logging.Logger]:
    def _info(s):
        print(s)
        # alog.info(f'{s}')

    ic.configureOutput(prefix=_prefix_time, outputFunction=_info, includeContext=False)

    log_config.fileConfig(fname='config/log_config.ini', disable_existing_loggers=True)
    alog = logging.getLogger('app')
    return alog


"""
Logging Config

# https://docs.python.org/3/library/logging.config.html

"""
