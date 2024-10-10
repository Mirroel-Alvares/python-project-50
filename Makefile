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
#
# install-games: # Для установки пакета из операционной системы используйте команду
# 	python3 -m pip install --user dist/*.whl.
#
# lint:
# 	poetry run flake8 brain_games
#
asciinema start:
	asciinema rec demo.cast

asciinema overwrite:
	asciinema rec demo.cast --overwrite

upload:
	asciinema upload demo.cast
