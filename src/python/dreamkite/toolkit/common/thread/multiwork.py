from concurrent import futures

from dreamkite.toolkit.common.log import logutil

LOOGER = logutil.get_default_logger()


def create_multi_works_with_param(workname, params, max_workers=10):
    future_list = []
    ret = []
    with futures.ThreadPoolExecutor(max_workers) as executer:
        for param in params:
            future_list.append(executer.submit(workname, param))
    try:
        for future in future_list:
            ret.append(future.result())
    except BaseException:
        LOOGER.exception("Multiwork raise exception for %s." % workname.__name__)


def create_multi_works_without_param(workname, multi_num, max_workers=10):
    future_list = []
    ret = []
    with futures.ThreadPoolExecutor(max_workers) as executer:
        for param in range(multi_num):
            future_list.append(executer.submit(workname))
    try:
        for future in future_list:
            ret.append(future.result())
    except BaseException:
        LOOGER.exception("Multiwork raise exception for %s." % workname.__name__)


if __name__ == '__main__':
    import time


    def work(n):
        LOOGER.info('begin to work-{}'.format(n))
        time.sleep(2)
        if n == 5:
            raise Exception()
        LOOGER.info('finished {}'.format(n))
        return n


    create_multi_works_with_param(work, [1, 2, 3, 4, 5, 6], 10)
    time.sleep(50)
