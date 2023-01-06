import logging

def load_train_set():
    logger = logging.getLogger(__name__)
    logger.info('Loading training set')
    return [([], [])]