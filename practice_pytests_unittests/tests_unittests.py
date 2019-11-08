import unittest
from practice import (
    task_1_list_unique,
    task_2_number_of_a,
    task_3_power_of_three,
    task_4_sum_of_digits,
    task_5_push_zeros,
    task_6_arithmetic_progression,
    task_7_numbers_occur_once,
    task_8_missing_number_in_list,
    task_9_count_elements_until_tuple,
    task_10_text_in_reversed_order
)


class Test(unittest.TestCase):

    def test_task_1_list_unique(self):
        first_list = [1, 1, 2]
        second_list = [1, 2, 3]
        self.assertListEqual(task_1_list_unique(first_list, second_list), [1, 2])

    def test_task_2_number_of_a(self):
        given_data = 'I am a good developer. I am also a writer'
        self.assertEqual(task_2_number_of_a(given_data), 5)

    def test_task_3_power_of_three(self):
        numbers = {
            'correct number1': [9, True],
            'correct number2': [3, True],
            'incorrect number': [8, False]
        }
        for subtest_name, (input_number, result) in numbers.items():
            with self.subTest(name=subtest_name):
                self.assertEqual(task_3_power_of_three(input_number), result, subtest_name)

    def test_task_4_sum_of_digits(self):
        self.assertEqual(task_4_sum_of_digits(97), 7)
        self.assertEqual(task_4_sum_of_digits(10), 1)

    def test_task_5_push_zeros(self):
        numbers = [0, 10, 4, 6, 7]
        self.assertEqual(task_5_push_zeros(numbers)[-1], 0)

    def test_task_6_arithmetic_progression_true(self):
        given_numbers = {
            'correct arithmetic progression1': [[3, 5, 7, 9, 11], True],
            'correct arithmetic progression2': [[13, 15, 17, 19], True],
            'incorrect arithmetic progression': [[3, 7, 9, 10], False],
            'arithmetic progression with one_element': [[1], False]
        }
        for subtest_name, (input_list, result) in given_numbers.items():
            with self.subTest(name=subtest_name):
                self.assertEqual(task_6_arithmetic_progression(input_list), result, subtest_name)

    def test_task_7_numbers_occur_once(self):
        given_numbers = {
            'numbers occur once': [[10, 2, 5, 5, 5, 3, 3, 4, 4], [10, 2]],
            'there are only duplicate numbers': [[3, 4, 3, 4], []],
        }
        for subtest_name, (input_list, result) in given_numbers.items():
            with self.subTest(name=subtest_name):
                self.assertEqual(task_7_numbers_occur_once(input_list), result, subtest_name)

    def test_task_8_missing_number_in_list(self):
        given_numbers = {
            'missing numbers in the list': [[1, 2, 3, 6, 7, 8, 10], [4, 5, 9]],
            'there are no missing numbers': [[1, 2, 3, 4, 5, 6], []],
        }
        for subtest_name, (input_list, result) in given_numbers.items():
            with self.subTest(name=subtest_name):
                self.assertEqual(task_8_missing_number_in_list(input_list), result, subtest_name)

    def test_task_9_count_elements_until_tuple(self):
        given_numbers = {
            'correct count of elements': [[1, 2, 3, (1, 2), 3], 3],
            'there are elements without tuple': [[1, 2, 3, 4], 4],
            'there are no elements with_tuple as a first element': [[(1, 2), 2, 3, 4], 0]
        }
        for subtest_name, (input_list, result) in given_numbers.items():
            with self.subTest(name=subtest_name):
                self.assertEqual(task_9_count_elements_until_tuple(input_list), result, subtest_name)

    def test_task_10_text_in_reversed_order(self):
        given_list = {
            'text in reversed order': ['Hello World and Coders', 'sredoC dna dlroW olleH'],
            'without text': ['', ''],
        }
        for subtest_name, (input_list, result) in given_list.items():
            with self.subTest(name=subtest_name):
                self.assertEqual(task_10_text_in_reversed_order(input_list), result, subtest_name)


if __name__ == "__main__":
    unittest.main()
