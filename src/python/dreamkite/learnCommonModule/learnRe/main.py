import re

def main01():
    """
    点分式的版本号匹配 1.0.02.sp1

    """
    pattern = re.compile(r'((sp){0,1}[0-9]+.)+(sp){0,1}[0-9]+')
    matcher = pattern.match('1.0.02.sp1')
    if matcher:
        print(matcher.group())


def main02():
    """
    固定格式的版本号匹配 R21C00SPC21

    """
    pattern = re.compile(r'^R(?P<R>[0-9]+)C(?P<C>[0-9]+)SPC(?P<SPC>[0-9]+)$')
    matcher = pattern.match('R21C00SPC21')
    if matcher:
        print(matcher.group())
        print(int(matcher.group('R')))
        print(int(matcher.group('C')))
        print(int(matcher.group('SPC')))


if __name__ == '__main__':
    main01()
    main02()