import os

def get_temp_path(*args):
    if os.environ.get('TEMP_PATH', ''):
        log_path = os.path.normpath(os.environ.get('TEMP_PATH'))
    else:
        log_path = os.path.normpath(get_root_path('output', 'temp'))
    if args:
        return os.path.join(log_path, os.sep.join(args))
    else:
        return log_path


def get_logger_path(*args):
    if os.environ.get('LOG_PATH', ''):
        log_path = os.path.normpath(os.environ.get('LOG_PATH'))
    else:
        log_path = os.path.normpath(get_root_path('output', 'log'))
    if args:
        return os.path.join(log_path, os.sep.join(args))
    else:
        return log_path


def get_root_path(*args):
    if os.environ.get('ROOT_PATH', ''):
        root_path = os.path.normpath(os.environ.get('LOG_PATH', ''))
    else:
        root_path = os.path.normpath(os.getcwd().split('src')[0])
    if args:
        return os.path.join(root_path, os.sep.join(args))
    else:
        return root_path


