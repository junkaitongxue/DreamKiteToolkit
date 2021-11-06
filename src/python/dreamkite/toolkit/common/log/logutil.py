import logging
import sys

from dreamkite.toolkit.common.os import toolkitpath

FORMAT = '%(asctime)-15s\t (%(process)d|%(thread)d) [%(levelname)s] [%(module)s:%(lineno)d] %(message)s'
GLOBAL_LOG = dict()


def get_default_logger():
    if 'dafault' in GLOBAL_LOG:
        return GLOBAL_LOG.get('default')
    formatter = logging.Formatter(FORMAT)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger = logging.getLogger('default')
    logger.setLevel(logging.INFO)
    logger.addHandler(stream_handler)
    return logger


def set_default_logger(logger):
    GLOBAL_LOG['default'] = logger


def get_output_logger(log_name):
    """
    记录log日志

    :param log_name: 日志名
    :return:
    """
    formatter = logging.Formatter(FORMAT)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(toolkitpath.get_logger_path('%s.log' % log_name))
    file_handler.setFormatter(formatter)

    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger


if __name__ == '__main__':
    # print(toolkitpath.get_logger_path('%s.log' % 'test'))
    LOGGER = get_output_logger('test')
    LOGGER.info("huangjunkai is test a file log.")
