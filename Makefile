install:
	poetry install

package-remove:
	python3 -m pip uninstall hexlet_code

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

gendiff:
	poetry run gendiff
#
# brain-even:
# 	poetry run brain-even
#
# brain-calc:
# 	poetry run brain-calc
#
# brain-gcd:
# 	poetry run brain-gcd
#
# brain-progression:
# 	poetry run brain-progression
#
# brain-prime:
# 	poetry run brain-prime
#
# publish:
# 	poetry publish  --dry-run
#
# install-games: # Для установки пакета из операционной системы используйте команду
# 	python3 -m pip install --user dist/*.whl.
#
# lint:
# 	poetry run flake8 brain_games
#
# asciinema start:
# 	asciinema rec demo.cast
#
# asciinema overwrite:
# 	asciinema rec demo.cast --overwrite
#
# upload:
# 	asciinema upload demo.cast
