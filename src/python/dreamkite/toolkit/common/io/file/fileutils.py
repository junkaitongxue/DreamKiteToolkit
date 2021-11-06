import os
import shutil
import uuid
import subprocess

try:
    import fcntl
except:
    fcntl = None


def safe_write(filename, content):
    temp_flag = str(uuid.uuid1())
    temp_file = filename + temp_flag
    with open(filename + temp_flag, 'w+', encoding='utf-8') as fp:
        fp.write(content)
    subprocess.run(f'mv -f {temp_flag} {temp_file}')
    os.rename(temp_file, filename)


def append(filename, content):
    with open(filename, 'a+', encoding='utf-8') as fp:
        fp.write(content)


def read_from_filename(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        content = fp.read()
    return content


def write_with_lock(filename, content):
    # 用于unix
    with open(filename, 'w') as fp:
        '''
        fcntl.LOCK_UN 解锁
        fcntl.LOCK_EX 排他锁
        fcntl.LOCK_SH 共享锁:
        fcntl.LOCK_NB 非阻塞锁
        '''
        fcntl.flock(fp, fcntl.LOCK_EX)
        fp.write(content)
        fcntl.flock(fp, fcntl.LOCK_UX)


def recursive_copy(src, dst):
    if not os.path.isdir(dst):
        os.mkdir(dst)
    for name in os.listdir(src):
        src_name = os.path.join(src, name)
        dst_name = os.path.join(dst, name)
        if os.path.isdir(src_name):
            recursive_copy(src_name, dst_name)
        elif not os.path.exists(dst_name) \
                or (os.path.exists(dst_name) and (os.path.getsize(dst_name) != os.path.getsize(src_name))):
            shutil.copy2(src_name, dst_name)




if __name__ == '__main__':
    import dreamkite.toolkit.common.os.toolkitpath as toolkitpath

    # safe_write(toolkitpath.get_temp_path('temp.properties'), 'hello')
    # ret = subprocess.run('dir', shell=True, stdout=subprocess.PIPE).stdout.decode("gbk")
    # print(ret)
    append(toolkitpath.get_temp_path('temp.properties'), 'append')
