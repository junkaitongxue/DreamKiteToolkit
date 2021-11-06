import os


def get_free_disk(path):
    '''
    单位为b
    '''
    d = os.statvfs(path)
    return d.f_bsize * d.f_bavail


if __name__ == '__main__':
    print(get_free_disk.__doc__)
