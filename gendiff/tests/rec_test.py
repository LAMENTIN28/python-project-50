from gendiff.gendiff_yaml import generate_diff_yaml
from gendiff.gendiff import generate_diff
from gendiff.gendiff_recurs import generate_diff_recurs
from gendiff.tests.fixtures.right_ans import right_ans
from gendiff.tests.fixtures.right_ans_recurs import right_ans_rec
import pytest



def test_right_json():
	assert generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json') == right_ans
	print('first test passed')


def test_right_yaml():
	assert generate_diff_yaml('gendiff/files/file1.yaml', 'gendiff/files/file2.yaml') == right_ans
	print('second test passed')


def test_right_recurs_json():
	print(right_ans_rec)
	res = generate_diff_recurs('gendiff/files/file1_rec.json', 'gendiff/files/file2_rec.json')
	print(res)
	assert generate_diff_recurs('gendiff/files/file1_rec.json', 'gendiff/files/file2_rec.json') == right_ans_rec
	print('third test passed')

test_right_json()
test_right_yaml()
test_right_recurs_json()
