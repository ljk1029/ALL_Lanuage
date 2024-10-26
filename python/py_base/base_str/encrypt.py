#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
说明文档：第三方库，配置解析

作者： ljk
日期:  2024/01/01

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2
"""

def json_extern():
  # Python 字典
  data = {
      "name": "John Doe",
      "age": 30,
      "isEmployed": True
  }

  # 将 Python 对象转换为 JSON 字符串
  json_string = json.dumps(data)
  print('json:', json_string)

  # 非空格
  json_string_pretty = json.dumps(data, indent=4)
  print('json:', json_string_pretty)

  data_with_non_ascii = {
      "name": "Jöhn Döe"
  }

  # 非ASCII
  json_string_non_ascii = json.dumps(data_with_non_ascii, ensure_ascii=False)
  print('json ascii:', json_string_non_ascii)
  json_string_non_ascii = json.dumps(data_with_non_ascii)
  print('json ascii:', json_string_non_ascii)

# json用法
import json
def json_demo():
    d = dict(name='Bob', age=20, score=88)
    print("json转换:", json.dumps(d))
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    print("json转换:", json.loads(json_str))



# base64用法
import base64
def base64_demo():
    L = b'binary\x00string'
    A = base64.b64encode(L)
    Q = b'YmluYXJ5AHN0cmluZw=='
    B = base64.b64decode(Q)
    print("enbsse64转换:", L, A)
    print("debsse64转换:", Q, B)



# 数据哈希用法
import hashlib
def hash_demo():
    L = 'how to use md5 in python hashlib?'
    print("hash计算前:", L)
    md5 = hashlib.md5()
    md5.update(L.encode('utf-8'))
    print("md5计算:", md5.hexdigest())
    sha1 = hashlib.sha1()
    sha1.update(L.encode('utf-8'))
    print("sha1计算:", sha1.hexdigest())


# yaml使用
import yaml
def yaml_demo():
    yaml_string = """
    a: 1
    b: 2
    c:
      - foo
      - bar
      - baz
    """
    data = yaml.safe_load(yaml_string)
    print("yaml解析: ",data)

    data = {
        'a': 1,
        'b': 2,
        'c': ['apple', 'banana', 'cherry']
    }
    yaml_string = yaml.dump(data)
    print("yaml生成: ", yaml_string)
    with open('output.yaml', 'w') as file:
        yaml.dump(data, file)

# main
if __name__ == '__main__':
    json_demo()
    base64_demo()
    hash_demo()
    yaml_demo()