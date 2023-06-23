import logging
import logging.config as log_config

# log_config.fileConfig(fname='log.conf', disable_existing_loggers=False)
LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'form1': {
            'class': 'logging.Formatter',
            'format': '{levelname} | {message} {arguments} | {asctime} | {funcName}:{filename}:{lineno}',
            'datefmt': '%d-%m-%Y %H:%M:%S ',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'form1',
            'stream': 'ext://sys.stdout',
        },
        # Uncomment this section for FileHandler
        # 'handF': {
        #     'class': 'logging.FileHandler',
        #     'level': 'INFO',
        #     'formatter': 'form1',
        #     'filename': 'logs/info.log',
        #     'mode': 'a',
        # },
    },
    'loggers': {
        'time_catcher': {
            'level': 'DEBUG',
            'propagate': 0,
            'handlers': ['console'],
        },
    },
}
log_config.dictConfig(LOGGING_CONFIG)

log = logging.getLogger("time_catcher")

# log.info = lambda msg,*args: log.info(f""""{msg} { " ".join((map(str,args)))}""")


log = logging.getLogger()

# log.info(1,111,1,1,1,1)
#
# log.info("rtsr",1,22,3)
# sys.exit(1)
