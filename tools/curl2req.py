"""Autoweb convert curl to python request."""
import json


def parse_head(curl):
    """Parse curl content by split '-H'.

    :param curl: curl content.
    """
    param_list = curl.split("' -H '")
    return param_list


def parse_kv(key_value):
    """Parse keys and values.

    :param key_value: key value string.
    """
    kv_list = key_value.split(': ')
    return kv_list


def build_head(head_list):
    """Build heads use head list.

    :param head_list: head_list.
    """
    head_dict = {}
    for kv in head_list:
        kv_list = parse_kv(kv)
        head_dict.setdefault(kv_list[0], kv_list[1])
    return head_dict


def parse_curl(curl_content):
    """Parse curl content.

    This can only parse a well write curl
    copied fromchrome or firefox console,
    end with --data or -compressed.

    :param curl_content: curl content string.
    """
    param_list = curl_content.split("' -H '")

    ender = param_list[-1]
    ender_list = ender.split(' --')

    # useful infomation
    url = param_list[0][param_list[0].rfind('\'') + 1:]
    head_list = param_list[1:-1] + [ender_list[0].strip('\'')]
    head_dict = build_head(head_list)

    if ender_list.__len__() == 2:
        data = ()
    else:
        data = ender_list[1].split(' ')

    return url, head_dict, data,


def curl_from_path(path):
    """Read curl content from path.

    :param path: curl file path.
    """
    with open(path, 'r') as curl_file:
        curl_content = curl_file.read()
    return curl_content


def convert(curl):
    """Convert the curl to a readable requests scripts.

    :param curl: curl content string.
    """
    method = 'get'
    template_list = [
        'import requests',
        'url = "{url}"',
        'headers = {headers}',
        'data = {data}',
        'if __name__ == \'__main__\':',
        '    resp = requests.{method}(url, headers=headers, data=data)',
        '    print(resp.status_code)',
        '    print(resp.content)',
    ]

    url, head_dict, data = parse_curl(curl)

    if data:
        data = data[1]
        method = 'post'
    else:
        data = 'None'
    headers = json.dumps(head_dict, indent=4)

    template = '\n'.join(template_list).rstrip('\n')
    template = '{}\n'.format(template)
    complete = template.format(
        url=url, headers=headers, method=method, data=data)
    return complete
