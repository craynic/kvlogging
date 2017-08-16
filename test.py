import logging
import kvlogging
logger = kvlogging.getLogger('module')
handler_json = logging.StreamHandler()
handler_json.setFormatter(kvlogging.JsonFormatter())
logger.addHandler(handler_json)
handler_stream = logging.StreamHandler()
handler_stream.setFormatter(kvlogging.StreamFormatter(
    fmt='%(levelname)s %(asctime)s %(message)s %(kvdata)s'))
logger.addHandler(handler_stream)
logger.info('hello')
logger.info('hello, %(target)s', target='world', name='Hally')
logger.info('hello, %(target)s', name='Hally')
