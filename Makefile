.PHONY: install clean flake test train run

install:
	@echo "*** Installing dependencies ***"
	pip3 install -r dependencies.txt

clean:
	@echo "*** Cleaning unnecessary caches ***"
	rm -rf scripts/__pycache__ .pytest_cache

flake:
	@echo "*** Linting python code ***"
	flake8 . --ignore="E501"

run:
	@echo "*** Running simulation ***"
	python3 game.py

group:
	@echo "*** Grouping words by Character Count ***"
	python3 data/word_grouper.py

test:
	@echo "*** Unit testing game.py ***"
	python3 -m unittest test_game.py
