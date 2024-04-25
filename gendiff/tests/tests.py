import pytest
from gendiff.gendiff import generate_diff
from fixtures.right_ans import right_ans


def tests_right():
    print(generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json'))
    assert right_ans == generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json')

def tests_unright():
    assert " " == generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json')

tests_right()
