import math
import time
import string


def task_1_list_unique(first_l, second_l):
    """Returns a list that contains only the elements that are
    common between the lists (without duplicates)"""
    return list(set(first_l) & set(second_l))


def task_2_number_of_character(data, character):
    """Return the number of times that the letter appears
    anywhere in the given string"""
    return data.count(character)


def task_3_power_of_three(number):
    """Check if a given positive integer is a power of three"""
    num = math.log(number, 3)
    return num == int(num)


def task_4_sum_of_digits(number):
    """Add the digits of a positive integer repeatedly until
    the result has a single digit"""
    digits = sum([int(digit) for digit in str(number)])
    return digits if digits <= 9 else task_4_sum_of_digits(digits)


def task_5_push_zeros(numbers):
    """Push all zeros to the end of a list"""
    for _ in numbers:
        if 0 in numbers:
            numbers.append(numbers.pop(numbers.index(0)))
    return numbers


def task_6_arithmetic_progression(numbers):
    """Check a sequence of numbers is an arithmetic progression
     or not"""
    if len(numbers) < 2:
        return False
    diff = numbers[1] - numbers[0]
    for i in range(len(numbers)-1):
        if not (numbers[i+1] - numbers[i]) == diff:
            return False
    return True


def task_7_numbers_occur_once(numbers):
    """Find the number in a list that doesn't occur twice"""
    return [number for number in numbers if numbers.count(number) == 1]


def task_8_missing_number_in_list(numbers):
    """Find a missing number from a list"""
    return [number for number in range(numbers[0], numbers[-1]+1) if number not in numbers]


def task_9_count_elements_until_tuple(numbers):
    """Count the elements in a list until an element is a tuple"""
    for number in range(len(numbers)):
        if isinstance(numbers[0], tuple):
            return 0
        if number+1 == len(numbers):
            return len(numbers)
        if isinstance(numbers[number+1], tuple):
            return number+1
    return number


def task_10_text_in_reversed_order(text):
    """Take the str parameter being passed and return the
    string in reversed order"""
    return text[::-1]


def task_11_converted_into_hours_minutes(given_time):
    """Take the num parameter being passed and return the
    number of hours and minutes the parameter converts to"""
    return time.strftime("%-M:%-S", time.gmtime(given_time))


def task_12_find_the_longest_word(word_list):
    """Return the largest word in the string"""
    word_list = ''.join([char for char in word_list if char not in string.punctuation])
    return max(word_list.split(' '), key=len)


def task_13_reversed_string():
    """Asks the user for a long string containing multiple
    words. Print back to the user the same string, except with the
    words in backwards order."""
    text = input('Write a long string: ').split(' ')[::-1]
    return ' '.join(text)


def task_14_sequence_of_fibonacci_numbers():
    """Asks the user how many Fibonnaci numbers to generate
    and then generates them"""
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
    """Makes a new list that has only the even elements of
    this list in it"""
    return [element for element in numbers if element % 2 == 0]


def task_16_sum_from_one_to_input_number():
    """Add up all the numbers from 1 to input number"""
    number = int(input('Your number: '))
    return sum(range(number+1))


def task_17_factorial(number):
    """Take the parameter being passed and return the
    factorial of it"""
    assert number >= 0 and type(number) is int, "Incorrect value for factorial"
    result = 1
    for element in range(1, number+1):
        result *= element
    return result


def task_18_transform_into_next_letter(text):
    """Take the str parameter being passed and modify it using
    the following algorithm. Replace every letter in the string with
    the letter following it in the alphabet (ie. c becomes d, z becomes
    a). Then capitalize every vowel in this new string (a, e, i, o, u)
    and finally return this modified string."""
    converted_text = []
    for letter in text:
        if letter.isalpha():
            letter = chr(ord(letter) + 1) if letter != 'z' else 'a'
            if letter in "aeiou":
                letter = letter.upper()
            converted_text += letter
    return ''.join(converted_text)


def task_19_transform_in_alphabetical_order(text):
    """Take the str string parameter being passed and return
    the string with the letters in alphabetical order (ie. hello
    becomes ehllo)"""
    text = [char for char in text if not char.isdigit() and char not in string.punctuation]
    return ''.join(sorted(text))


def task_20_comparing_two_numbers():
    """Take both parameters being passed and return the true
    if num2 is greater than num1, otherwise return the false. If the
    parameter values are equal to each other then return the string
    -1"""
    number1 = int(input('Your first number: '))
    number2 = int(input('Your second number: '))
    return '-1' if number2 == number1 else number2 > number1
