import unittest
import HtmlTestRunner

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        assert self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    # 定义测试套件
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestStringMethods))

    # 定义测试报告的目录和命名
    kwargs = {
        "output": 'test_reports',  # 输出报告文件夹的名称
        "report_name": 'test_report',  # 报告名称
        "combine_reports": True,  # 将所有用例结果合并到一个报告文件中
        "add_timestamp": True,  # 增加时间戳
    }

    # 运行测试用例，并生成HTML报告
    runner = HtmlTestRunner.HTMLTestRunner(**kwargs)
    runner.run(test_suite)