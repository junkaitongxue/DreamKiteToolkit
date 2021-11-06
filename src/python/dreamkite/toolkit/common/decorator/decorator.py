import functools
import time

from dreamkite.toolkit.common.log import logutil

LOGGER = logutil.get_default_logger()


def retry(max_time):
    """
    用于函数抛异常之后捕获之后进行重试

    :param max_time: 重试次数
    :return:
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, max_time + 1):
                try:
                    ret = func(*args, **kwargs)
                except Exception as exception:
                    LOGGER.error('Catch exception for function: %s, retry for %s time.' % (func.__name__, i))
                    if i == max_time:
                        raise exception
                    continue
                else:
                    return ret

        return wrapper

    return decorator


def timeit(func):
    """
    记录函数的执行耗时时间
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        LOGGER.info(f'Start to execute: {func.__name__}.')
        start_time = time.time()
        try:
            ret = func(*args, **kwargs)
        finally:
            LOGGER.info('End to execute: %s, spend %.3fs.' % (func.__name__, time.time() - start_time))
        return ret

    return wrapper


def singleton(cls):
    """
    修饰类
    :param cls:
    :return: 
    """
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner


if __name__ == '__main__':
    # @timeit
    # @retry(5)
    # def test():
    #     print("hjk")
    #     time.sleep(3)
    #     raise Exception("hello , i am a exception.")
    #
    # test()

    @singleton
    class Cls(object):
        def __init__(self):
            pass


    cls1 = Cls()
    cls2 = Cls()
    print(id(cls1) == id(cls2))
