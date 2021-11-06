import os
import re

from dreamkite.toolkit.common.io.file import fileutils


def get_value_from_properties_by_key(filename, key):
    '''
    解析格式为k=v的properties文件

    :param filename: 文件路径
    :param key: key值
    :return: key值对应的value，找不到返回None
    '''
    # (?P<value>.*?)  : 由?P<value>和.*?，前者为后面group找的key值，后者为匹配模式，然后用括号包起来
    pattern = r'%s\s*=(?P<value>.*)$' % key
    # 商用环境需要调用安全写（加锁）的cbb去写
    with open(filename, 'r', encoding='utf-8') as fp:
        line = fp.readline()
        while line:
            matcher = re.match(pattern, line)
            if matcher:
                return matcher.group('value').strip()
            line = fp.readline()
        return None


def get_all_kv_from_properties(filename):
    pattern = r'(?P<key>.*)\s*=(?P<value>.*)$'
    kv = {}
    with open(filename, 'r', encoding='utf-8') as fp:
        line = fp.readline()
        while line:
            matcher = re.match(pattern, line)
            if matcher:
                kv[matcher.group('key').strip()] = matcher.group('value').strip()
            line = fp.readline()
        return kv


def write_properties_by_kv(filename, new_content: dict, append=False):
    """
    写properties文件

    :param new_content:
    :param isappend: 是否追加，默认不追加去覆盖
    :param filename: 文件路径
    """
    if append:
        old_kv = get_all_kv_from_properties(filename)
        old_kv.update(new_content)
        new_content = old_kv
    with open(filename, 'w+', encoding='utf-8') as fp:
        content_list = []
        for kv in new_content:
            content_list.append(f'{kv}={new_content[kv]}')
        fp.write('\n'.join(content_list))


if __name__ == '__main__':
    from dreamkite.toolkit.common.os import toolkitpath

    # read
    # print(get_value_from_properties_by_key(toolkitpath.get_temp_path('temp.properties'), 'redis_port'))
    # print(get_all_kv_from_properties(toolkitpath.get_temp_path('temp.properties')))

    # write
    content = {'author': 'huangjunkai', 'alias': 'DreamKite', 'redis_port': '26307'}
    write_properties_by_kv(toolkitpath.get_temp_path('temp.properties'), {'append': 'value'}, append=True)
