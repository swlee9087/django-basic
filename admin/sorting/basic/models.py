from dataclasses import dataclass



@dataclass
class MySum(object):
    start_number: int
    end_number: int

    @property
    def start_number(self) -> int: return self._start_number

    @property
    def end_number(self) -> int: return self._end_number

    @start_number.setter
    def start_number(self, start_number): self._start_number = start_number

    @end_number.setter
    def end_number(self, end_number): self._end_number = end_number

    def one_to_ten_sum_1(self):
        sum = 0
        for i in range(self.start_number, self.end_number):
            sum += i
        return sum

    def one_to_ten_sum_2(self):
        return sum(i for i in range(self.start_number, self.end_number))

    def one_to_ten_sum_3(self):
        return sum(range(self.start_number, self.end_number))


@dataclass
class Palindrome(object):
    input_string: str

    @property
    def input_string(self)-> str: return self._input_string

    @input_string.setter
    def input_string(self,input_string): self._input_string = input_string

    def str_to_list(self) -> []:
        return [i for i in self.input_string if i.isalnum()]

    def isPalindrome(self) -> bool:
        ls = self.str_to_list()
        print(f'ls len : {len(ls)}')
        return {"RESULT": False for i in ls if ls.pop(0) != ls.pop()}

    def reverse_string(self)-> []:
        strs = self.str_to_list()
        return strs[::-1]

#
# @dataclass
# class Reverse(object):
#     input_string: str
#
#     def str_to_list(self, payload: str) -> []:
#         return [i for i in payload if i.isalnum()]
#
#     def reverse_list(self, ls: []) -> []:
#         left = 0
#         right = 0
#         while left < right:
#             ls[left], ls[right] = ls[right], ls[left]
#             left += 1
#             right -= 1
#             return ls[::-1]
#
#     def list_to_str(self, ls: []) -> str:
#         return "".join([i for i in ls])
