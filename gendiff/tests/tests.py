import pytest
from gendiff.gendiff import generate_diff
from fixtures.right_ans import right_ans


def tests_right():
    result = generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json')
    assert right_ans == result 


tests_right()