import unittest

from admin.sorting.basic.models import *


# import sys
# sys.path.append('/admin/sorting')


# Create your tests here.
class TestMySum(unittest.TestCase):
    # ott = OneToTen()

    def test_one_to_ten_sum_1(self):
        ott = MySum()
        ott.start_number = 1
        ott.end_number = 11
        res = ott.one_to_ten_sum_2()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 55)


class TestPalindrome(unittest.TestCase):
    def test_str_to_list(self):
        inst=Palindrome()
        inst.input_string="when will i be free from IBS"
        res=inst.isPalindrome()
        print(res)
        # ls = [i for i in "A man, a plan, a canal: Panama" if i.isalnum()]
        # print(f'test_str_to_list : {ls}')

    # def test_isPalindrome(self) -> bool:
    #     ls = [i for i in "A man, a plan, a canal: Panama" if i.isalnum()]
    #     dict = {"RESULT": True for i in ls if ls.pop(0) != ls.pop()}
    #     print(f'test_isPalindrome: {dict["RESULT"]}')
        # self.mock.isPalindrome()


    def test_reverse_list(self):
        inst=Palindrome()
        inst.input_string="when will i be free from IBS"
        res=inst.reverse_string()
        print(res)
        # ls = [i for i in 'when will i be free from IBS' if i.isalnum()]
        # print(ls[::-1])
        # self.mock.reverse_list(self.mock.str_to_list(payload))
    #
    # def test_list_to_str(self) -> str:
    #     ls = [i for i in 'when will i be free from IBS' if i.isalnum()]
    #     print(" ".join([i for i in ls]))


if __name__ == '__main__':
    unittest.main()
