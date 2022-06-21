import re


def name_convert_to_camel(name: str) -> str:
    """下划线转驼峰(小驼峰)"""
    return re.sub(r'(_[a-z])', lambda x: x.group(1)[1].upper(), name)


def get_attr_value(line):
    """提取出属性名"""
    pattern = '.* (?P<attr>\w+)'
    mo = re.match(pattern, line)
    if mo:
        return mo.group('attr') if mo.group('attr') else None


if __name__ == '__main__':
    in_file_name = 'in.java'
    out_file_name = 'out.java'
    try:
        with open(in_file_name, 'r', encoding='utf-8') as r:
            lines = r.readlines()

        with open(out_file_name, 'w', encoding='utf-8') as w:
            for line in lines:
                attr = get_attr_value(line)
                w.writelines(f'        @JsonAlias("{attr}")' + '\n')
                new_attr_name = name_convert_to_camel(attr)
                new_line = line.replace(attr, new_attr_name)
                w.writelines(new_line + '\n')
    except FileNotFoundError as e:
        print(e)
