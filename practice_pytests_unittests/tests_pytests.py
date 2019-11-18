import pytest
from practice import (
    task_11_converted_into_hours_minutes,
    task_12_find_the_longest_word,
    task_13_reversed_string,
    task_14_sequence_of_fibonacci_numbers,
    task_15_even_elements_in_list,
    task_16_sum_from_one_to_input_number,
    task_17_factorial,
    task_18_transform_into_next_letter,
    task_19_transform_in_alphabetical_order,
    task_20_comparing_two_numbers
)


@pytest.mark.parametrize(
    'time, result',
    [
        (63, '1:3'),
        (105, '1:45'),
        (5, '0:5'),
        (0, '0:0'),
    ]
)
def test_task_11_converted_into_hours_minutes(time, result):
    assert task_11_converted_into_hours_minutes(time) == result


@pytest.mark.parametrize(
    'input_string, result',
    [
        ('fun&!! time', 'time'),
        ('I love dogs', 'love')
    ]
)
def test_task_12_find_the_longest_word(input_string, result):
    assert task_12_find_the_longest_word(input_string) == result


@pytest.mark.parametrize(
    'input_string, result',
    [
        ('My name is Michele', 'Michele is name My'),
        ('', '')
    ]
)
def test_task_13_reversed_string(monkeypatch, input_string, result):
    monkeypatch.setattr('builtins.input', lambda x: input_string)
    assert task_13_reversed_string() == result


@pytest.mark.parametrize(
    'user_input, result',
    [
        (-5, "Can't be negative numbers"),
        (0, 0),
        (1, 1),
        (9, [0, 1, 1, 2, 3, 5, 8, 13, 21])
    ]
)
def test_task_14_sequence_of_fibonacci_numbers(monkeypatch, user_input, result):
    monkeypatch.setattr('builtins.input', lambda x: user_input)
    assert task_14_sequence_of_fibonacci_numbers() == result


@pytest.mark.parametrize(
    'given_list, result', [([1, 4, 9, 16, 25, 36, 49, 64, 81, 100], [4, 16, 36, 64, 100])]
)
def test_task_15_even_elements_in_list(given_list, result):
    assert task_15_even_elements_in_list(given_list) == result


@pytest.mark.parametrize('input_number, result', [(4, 10), (10, 55)])
def test_task_16_sum_from_one_to_input_number(monkeypatch, input_number, result):
    monkeypatch.setattr('builtins.input', lambda x: input_number)
    assert task_16_sum_from_one_to_input_number() == result


@pytest.mark.parametrize('number, result', [(4, 24), (0, 1)])
def test_task_17_factorial(number, result):
    assert task_17_factorial(number) == result


@pytest.mark.parametrize('number', [(-5), 2.6])
def test_task_17_factorial_failure(number):
    with pytest.raises(Exception) as exinfo:
        task_17_factorial(number)
    assert exinfo.type == AssertionError
    assert str(exinfo.value) == 'Incorrect value for factorial'


@pytest.mark.parametrize('input_string, result', [('abcdz4.', 'bcdEA')])
def test_task_18_transform_into_next_letter(input_string, result):
    assert task_18_transform_into_next_letter(input_string) == result


@pytest.mark.parametrize('input_text, result', [('hello', 'ehllo'), ('.edcba4', 'abcde')])
def test_task_19_transform_in_alphabetical_order(input_text, result):
    assert task_19_transform_in_alphabetical_order(input_text) == result


@pytest.mark.parametrize(
    'number1, number2, result',
    [
        (5, 10, True),
        (0, -1, False),
        (1, 1, '-1')
    ]
)
def test_task_20_comparing_two_numbers(mocker, number1, number2, result):
    mocker.patch('builtins.input',  side_effect=[number1, number2])
    assert task_20_comparing_two_numbers() == result
