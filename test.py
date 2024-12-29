from gendiff import generate_diff

diff = generate_diff("python-project-50/tests/fixtures/file1.json", "python-project-50/tests/fixtures/file2.json")
print(diff)
