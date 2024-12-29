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
