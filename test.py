import unittest

from function import manage_txt, if_else_elif_num, switch_case_num

words = ['int', 'int', 'double', 'long', 'switch', 'case', 'break', 'case', 'break', 'case', 'break', 'default',
         'break', 'switch', 'case', 'break', 'case', 'break', 'default', 'break', 'if', 'if', 'else', 'elif', 'if',
         'elif', 'elif', 'else', 'else', 'if', 'else', 'return']
with open('text.1', encoding = 'utf-8') as C_object:
    lines = C_object.readlines()
count = 35


class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_words, test_count = manage_txt(lines)
        self.assertEqual(test_words, words)  # add assertion here
        self.assertEqual(test_count, 35)  # add assertion here

    def test_something1(self):
        test_case_num, test_switch_num = switch_case_num(words)
        self.assertEqual(test_case_num, [3, 2])
        self.assertEqual(test_switch_num, 2)

    def test_something3(self):
        test_if_num, test_if_elseif_else = if_else_elif_num(words)
        self.assertEqual(test_if_num, 4)
        self.assertEqual(test_if_elseif_else, 2)


if __name__ == '__main__':
    unittest.main()
