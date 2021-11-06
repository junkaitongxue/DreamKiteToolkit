import functools
import threading
from dreamkite.toolkit.common.log import logutil
import time
LOCK_DICT = dict()
LOGGER = logutil.get_default_logger()

def process_lock(lock_name, timeout=-1):
    """
    根据函数名为标识为函数添加线程锁

    :param timeout: 超时时间，默认为阻塞等待，单位s
    :param lock_name: 根据锁名找对对应的锁名，对该函数执行加锁
    :return:
    """

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if lock_name not in LOCK_DICT:
                LOCK_DICT[lock_name] = threading.Lock()
            if LOCK_DICT[lock_name].acquire(timeout=timeout):
                ret = func(*args, **kwargs)
                LOCK_DICT[lock_name].release()
                return ret
            else:
                LOGGER.info(f'Timeout in trying to acquired lock for {func.__name__}')
                return


        return wrapper

    return decorator


if __name__ == '__main__':
    @process_lock('test', 1)
    def test():
        import time
        print('start')
        time.sleep(2)
        print('end')


    import time
    from dreamkite.toolkit.common.thread import multiwork

    multiwork.create_multi_works_without_param(test, 10)
    time.sleep(30)
