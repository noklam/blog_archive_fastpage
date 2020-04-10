import log
def do_something():
    logger.debug('submodule message')
logger = log.setup_custom_logger(__name__)
do_something()
