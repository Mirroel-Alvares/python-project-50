import pytest
from gendiff.generate_diff import generate_diff


def read_result(path_file):
    with open(path_file, "r") as file:
        return file.read()


@pytest.mark.parametrize(
    "file1, file2, result",
    [
        (
            "tests/fixtures/file1.json",
            "tests/fixtures/file2.json",
            "tests/fixtures/result_json.txt",
        )
    ],
)
def test_generate_diff(file1, file2, result):
    assert generate_diff(file1, file2) == read_result(result)







# import os
# import pytest
# import json
# from gendiff.get_diff import get_diff
# from gendiff.load_files import load_files


# @pytest.fixture
# def file_path():
#     return {
#         'json1': os.path.join('tests', 'fixtures', 'file1.json'),
#         'json2': os.path.join('tests', 'fixtures', 'file2.json'),
#         'result_json': os.path.join('tests', 'fixtures', 'result_json.txt')
#     }
#
#
# @pytest.fixture
# def expected_result(file_path):
#     results = {}
#     result_path = file_path['result_json']
#     with open(result_path, 'r') as file:
#         results['json'] = json.load(file)
#     return results
#
#
# @pytest.mark.parametrize("file1_key, file2_key, result_key", [
#                         ('json1', 'json2', 'json'),
#                     ])
# def test_gendiff(file_path, expected_result,
#                  file1_key, file2_key, result_key):
#
#     diff = get_diff(file_path[file1_key], file_path[file2_key],)
#     assert json.loads(diff) == expected_result[result_key]
