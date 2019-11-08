import math
import time
import string


def task_1_list_unique(first_l, second_l):
    return list(set(first_l) & set(second_l))


def task_2_number_of_a(data):
    return data.count('a')


def task_3_power_of_three(number):
    num = math.log(number, 3)
    return num == int(num)


def task_4_sum_of_digits(number):
    list_of_digits = sum([int(digit) for digit in str(number)])
    if list_of_digits <= 9:
        return list_of_digits
    else:
        return task_4_sum_of_digits(list_of_digits)


def task_5_push_zeros(numbers):
    for _ in numbers:
        if 0 in numbers:
            numbers.append(numbers.pop(numbers.index(0)))
    return numbers


def task_6_arithmetic_progression(numbers):
    if len(numbers) < 2:
        return False
    diff = numbers[1] - numbers[0]
    for i in range(len(numbers)-1):
        if not (numbers[i+1] - numbers[i]) == diff:
            return False
    return True


def task_7_numbers_occur_once(numbers):
    return [number for number in numbers if numbers.count(number) == 1]


def task_8_missing_number_in_list(numbers):
    return [number for number in range(numbers[0], numbers[-1]+1) if number not in numbers]


def task_9_count_elements_until_tuple(numbers):
    for number in range(len(numbers)):
        if isinstance(numbers[0], tuple):
            return 0
        if number+1 == len(numbers):
            return len(numbers)
        if isinstance(numbers[number+1], tuple):
            return number+1
    return number


def task_10_text_in_reversed_order(text):
    return ''.join(reversed(text))


def task_11_converted_into_hours_minutes(given_time):
    return time.strftime("%-M:%-S", time.gmtime(given_time))


def task_12_find_the_longest_word(word_list):
    word_list = [char for char in word_list if char not in string.punctuation]
    word_list = ''.join(word_list)
    return max(word_list.split(), key=len)


def task_13_reversed_string():
    text = input('Write a long string containing multiple words: ')
    split_text = text.split(' ')
    split_text = split_text[::-1]
    return ' '.join(split_text)


def task_14_sequence_of_fibonacci_numbers():
    user_number = int(input('Your number: '))
    if user_number < 0:
        return "Can't be negative numbers"
    elif user_number in [0, 1]:
        return user_number
    else:
        result = [0, 1]
        for number in range(2, user_number):
            result.append((result[number - 1]) + (result[number-2]))
        return result


def task_15_even_elements_in_list(numbers):
    return [element for element in numbers if element % 2 == 0]


def task_16_sum_from_one_to_input_number():
    number = int(input('Your number: '))
    result = 0
    for element in range(1, number+1):
        result += element
    return result


def task_17_factorial(number):
    assert number >= 0 and type(number) is int, "Incorrect value for factorial"
    result = 1
    for element in range(1, number+1):
        result *= element
    return result


def task_18_transform_into_next_letter(text):
    converted_text = []
    for letter in text:
        if letter.isalpha():
            letter = chr(ord(letter) + 1) if letter != 'z' else 'a'
            if letter in "aeiou":
                letter = letter.upper()
            converted_text += letter
    return ''.join(converted_text)


def task_19_transform_in_alphabetical_order(text):
    text = [char for char in text if not char.isdigit() and char not in string.punctuation]
    return ''.join(sorted(text))


def task_20_comparing_two_numbers():
    number1 = int(input('Your first number: '))
    number2 = int(input('Your second number: '))
    if number1 == number2:
        return '-1'
    else:
        return number2 > number1
