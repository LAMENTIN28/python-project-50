from gendiff.gendiff import generate_diff
from gendiff.gendiff_yaml import generate_diff_yaml
from fixtures.right_ans1 import right_ans



def test_right_json():
	assert generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json') == right_ans
	print('first test passed')


def test_right_yaml():
	assert generate_diff_yaml('gendiff/files/file1.yaml', 'gendiff/files/file2.yaml') == right_ans
	print('second test passed')


test_right_json()
test_right_yaml()
