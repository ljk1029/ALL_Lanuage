#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' base fuction module '

__author__ = 'ljk'

# 函数测试名打印
def method_decorator(method):
    from functools import wraps
    import time
    @wraps(method)  # 保留原始方法的名称和文档字符串
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 计算函数开始时间
        print(f"[__{method.__name__}__]-测试开始: 参数是{args}和{kwargs}")
        result = method(*args, **kwargs)  # 执行函数并保存返回值
        end_time = time.time()  # 计算函数结束时间
        print(f"[__{method.__name__}__]-结束结束. 耗时: {end_time - start_time:.2f}秒\n")
        return result  # 返回函数执行的结果
    return wrapper


class BaseType:
    def method_decorator(method):
        def wrapper(self, *args, **kwargs):
            print(f"[{method.__name__}测试]:")
            return method(self, *args, **kwargs)
        return wrapper

    # print使用
    @method_decorator
    def demo_print(self):
        print(b'ABC'.decode('ascii'))
        str_z = 'ABC'
        str_b = str_z.encode('ascii')
        print("decode:", str_z)
        print("encode:", str_b)
        print("dncode:", str_b.decode('ascii'))
        print("len:", len(str_z))
        str_z = '您好!, python'
        str_b = str_z.encode('utf-8')
        print("decode:", str_z)
        print("encode:", str_b)
        print("dncode:", str_b.decode('utf-8'))
        str_z = '中文, chinese'
        str_b = str_z.encode('gb2312')
        print("decode:", str_z)
        print("encode:", str_b)
        print("dncode:", str_b.decode('gb2312'))

    # list使用
    @method_decorator
    def demo_list(self)->list:
        print("[list测试]:")
        list_name = ['Michael', 'Bob', 'Tracy']
        # pop
        print("list:", list_name)
        print("list:", list_name.pop())
        print("list:", list_name.pop(1))
        print("list:", list_name)
        print("list range(5):", list(range(5)))
        # 排序
        list_a = ['c', 'b', 'a', 'a']
        print("list init:", list_a)
        print("list sort:", list_a.sort())
        print("list index:", list_a.index('c'))
        return list_name

    # tuple使用, 一旦初始化就不能修改
    @method_decorator
    def demo_tuple(self)->tuple:
        tuple_name = ('Michael', 'Bob', 'Tracy')
        print("tuple:", tuple_name)
        # 防止只有一个元素，歧义
        t = (1,)
        print("tuple:", t)
        return tuple_name

    # dict使用
    @method_decorator
    def demo_dict(self)->dict:
        dict_name = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
        print("dict:", dict_name)
        print("dict:", dict_name['Michael'])
        # add
        dict_name['Adam'] = 67  
        print("dict:", dict_name['Adam'])
        # exist
        print("dict Thomas exist:", 'Thomas' in dict_name)
        # pop
        print("dict:", dict_name.pop('Bob'))
        print("dict:", dict_name)
        # get不存在就返回默认值
        print("dict:", dict_name.get('Bob', -1))
        return dict_name

    # set使用 元素不能重复
    @method_decorator
    def demo_set(self)->set:
        set_num = set([1, 1, 2, 2, 3, 3])
        print("set:", set_num)
        set_num.add(4)
        print("set add:", set_num)
        set_num.remove(3)
        print("set  rm:", set_num)
        return set_num

    # str使用
    @method_decorator
    def demo_str(self)->str:
        str_a = 'abcD'
        print("str:", str_a)
        print("str:", str_a.replace('a', 'A'))
        print("str:", str_a)
        print("str:", str_a.lower())
        return str_a   

    # 类型转换
    @method_decorator
    def test_type(self):
        print("类型转换:", int('123')) 
        print("类型转换:", int(12.34))
        print("类型转换:", float('12.34'))
        print("类型转换:", str(1.23))
        print("类型转换:", str(100))
        print("类型转换:", bool(1))
        print("类型转换:", bool(''))
        print("类型显示:", type(self))
        print("类型显示:", isinstance(self, int))


# main
if __name__ == '__main__':
    basetype = BaseType()
    basetype.demo_print()
    basetype.demo_list()
    basetype.demo_tuple()
    basetype.demo_dict()
    basetype.demo_set()
    basetype.demo_str()
    basetype.test_type()

