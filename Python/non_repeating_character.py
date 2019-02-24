# first Non repeating:

import unittest


def non_repeating_string(str1):
    temp_dict = dict()
    temp_list = list()
    for i in str1:
        temp_dict[i] = 0
    for i in str1:
        temp_dict[i] = temp_dict[i] + 1
    for key in temp_dict.keys():
        if temp_dict[key] <= 1:
            temp_list.append(key)        
    for item in str1:
        if item in temp_list:
            return(item)


class TestStringMethods(unittest.TestCase):

    def test_non_repeating_string(self):
        self.assertEqual("a", non_repeating_string("bbbaddddd"))


unittest.main(exit=False)


# better approach:

def non_repeating(str1):
    temp_dict = dict()
    for i in str1:
        temp_dict.update({i: str1.count(i)})
    for item in str1:
        if item in temp_dict and temp_dict[item] == 1:
            return item


class TestStringMethod(unittest.TestCase):

    def test_non_repeating_string(self):
        self.assertEqual("a", non_repeating("bbbaddddd"))


unittest.main(exit=False)
