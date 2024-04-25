from gendiff import generate_diff
from fixtures.right_ans1 import right_ans



def test_right():
	assert generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json') == right_ans
	print('fist test passed')


test_right()
