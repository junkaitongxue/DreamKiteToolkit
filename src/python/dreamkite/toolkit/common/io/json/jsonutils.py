import json

from dreamkite.toolkit.common.os import toolkitpath


def load_json_from_dict(content_dict: dict) -> str:
    return json.dumps(content_dict)


def load_dict_from_json(json_str: str) -> dict:
    return json.loads(json_str)


def write_json_file_from_dict(content_dict, file_name):
    with open(file_name, 'w+', encoding='utf-8') as fp:
        json.dump(content_dict, fp, indent=4)


def read_dict_from_json_file(file_name):
    with open(file_name, 'r') as fp:
        return json.load(fp)


if __name__ == '__main__':
    a_dict = {"a": "a_v俊楷"}
    a_json = load_json_from_dict(a_dict)
    print(a_json)
    a_dict2 = load_dict_from_json(a_json)
    print(a_dict2.get('a'))

    print(toolkitpath.get_temp_path('temp.json'))
    write_json_file_from_dict(a_dict, toolkitpath.get_temp_path('temp.json'))
    print(read_dict_from_json_file(toolkitpath.get_temp_path('temp.json')))
