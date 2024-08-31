from gendiff.gendiff_yaml import generate_diff_yaml
from gendiff.gendiff import generate_diff
from gendiff.gendiff_recurs import generate_diff_recurs
from gendiff.gendiff_recurs_yaml import generate_diff_recurs_yaml
from gendiff.tests.fixtures.right_ans import right_ans
from gendiff.tests.fixtures.right_ans_recurs import right_ans_rec
from gendiff.plain import generate_diff_plain
from gendiff.tests.fixtures.right_ans_plain import right_ans_plain


def test_right_json():
    assert generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json') == right_ans
    print('first test passed')


def test_right_yaml():
    assert generate_diff_yaml('gendiff/files/file1.yaml', 'gendiff/files/file2.yaml') == right_ans
    print('second test passed')


def test_right_recurs_json():
    assert generate_diff_recurs('gendiff/files/file1_rec.json',
                                'gendiff/files/file2_rec.json') == right_ans_rec
    print('third test passed')


def test_right_recurs_yaml():
    assert generate_diff_recurs_yaml('gendiff/files/file1_rec.yaml',
                                     'gendiff/files/file2_rec.yaml') == right_ans_rec
    print('fourth test passed')


def test_right_plain():
    assert generate_diff_plain('gendiff/files/file1_rec.json',
                               'gendiff/files/file2_rec.json', 'plain') == right_ans_plain
    print('fifth test passed')
    assert generate_diff_plain('gendiff/files/file1_rec.json',
                               'gendiff/files/file2_rec.json') is None
    print('sixth test passed')


test_right_json()
test_right_yaml()
test_right_recurs_json()
test_right_recurs_yaml()
test_right_plain()
