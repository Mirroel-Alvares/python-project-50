install:
	poetry install

package-remove:
	python3 -m pip uninstall hexlet_code

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*whl

gendiff:
	poetry run gendiff

publish:
	poetry publish  --dry-run

# Запуск линтера
lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

# Запуск тестов
tests:
	poetry run pytest -vv

# Запуск тестов с покрытием
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests

# Проверка зависимостей
selfcheck:
	poetry check

# Общая проверка
check: selfcheck lint tests


asciinema start:
	asciinema rec demo.cast

asciinema overwrite:
	asciinema rec demo.cast --overwrite

upload:
	asciinema upload demo.cast

# cd /mnt/c/Users/mirroel/PycharmProjects/MirroelpythonProject/python-project-50/
