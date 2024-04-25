import pytest
from gendiff.gendiff import generate_diff
from fixtures.right_ans import right_ans


def tests_right():
    assert generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json').lower() == right_ans

def tests_unright():
    assert " " == generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json')

tests_right()

