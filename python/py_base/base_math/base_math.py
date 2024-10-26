#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
说明文档： 数学公司使用说明

作者： ljk
日期： 2023/12/07

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2
"""

"""
    1、数学测试
"""
# abs max
def math_demo():
    a = abs(-20)
    print("ads测试:", a)
    b = max(2, 3, 1, -5)
    print("max测试:", b)




"""
    2、迭代器测试部分
"""
class generator:
    # 打印生成数据
    def print_data(self, g):
        print("data:", g)
        while True:
            try:
                x = next(g)
                print('Generator:', x)
            except StopIteration as e:
                print('Generator return value:', e.value)
                break

    # generator 测试
    def generator_test(self, num:int):
        g = (x * x for x in range(num))
        return g, num
    
    # yield 测试
    def fib(self, max):
        # yield 关键字用于定义一个生成器函数generator， 
        # return 'done' 存在于函数内，但它并不会被直接返回给调用者。生成器函数的返回值是一个生成器对象，而不是 'done'
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            a, b = b, a + b
            n = n + 1
        return 'done'
    def yield_test(self, num:int):
        g = self.fib(num)
        return g, num
    
    # iter 测试
    def iter_test(self, num:int):
        it = iter([x * x for x in range(num)])
        return it
    
    # 测试
    def test(self):
        g, _ = self.generator_test(10)
        y, _ = self.yield_test(6)
        i = self.iter_test(5)
        self.print_data(g)
        self.print_data(y)
        self.print_data(i)

from functools import reduce
class data_handle():
    # map
    def map_test(self, list_data:list = [1, 2, 3, 4, 5, 6, 7, 8, 9]):
        input_data = list(map(str, list_data))
        print("map:", input_data)
        print("map:", type(input_data))
        return input_data
    
    # reduce
    def fn(self, x, y):
        return x * 10 + y
    def reduce_test(self, list_data:list = [1, 3, 5, 7, 9]):
        output_data = reduce(self.fn, list_data)
        print("reduce:", output_data)
        print("reduce:", type(output_data))
        return output_data

    # filter
    def is_odd(self, n):
        return n % 2 == 1
    def filter_test(self, list_data:list = [1, 2, 4, 5, 6, 9, 10, 15]):
        output_data = list(filter(self.is_odd, list_data))
        print("filter:", output_data) 
        print("filter:", type(output_data))
        return output_data 

    # ['bob', 'about', 'Zoo', 'Credit']
    # [36, 5, -12, 9, -21]
    # sorted
    def sorted_test(self, L:list):
        print("sorted:", L)  
        print("sorted:", sorted(L))   
        return L

#main
if __name__ == '__main__':
    math_demo()
    G = generator()
    G.test()
    H = data_handle()
    H.map_test()
    H.reduce_test()
    H.filter_test()
    H.sorted_test(['bob', 'about', 'Zoo', 'Credit'])
    H.sorted_test([36, 5, -12, 9, -21])
    