from gendiff.get_diff import get_diff
from gendiff.load_files import load_files


def generate_diff(file_pass1, file_pass2):
    file1, file2 = load_files(file_pass1), load_files(file_pass2)
    return get_diff(file1, file2)


