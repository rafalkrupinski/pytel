import logging.config

if False:
    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'simple': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                'formatter': 'simple',
                'stream': 'ext://sys.stdout',
            }},
        'loggers': {
            'simpleExample': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': 'no',
            }},
        'root': {
            'level': 'DEBUG',
            'handlers': ['console']
        }
    })
