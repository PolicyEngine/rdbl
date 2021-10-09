all:
	python setup.py sdist bdist_wheel
install:
	pip install -e .
install-dev:
	pip install pytest black autopep8
	pip install -e .
test:
	pytest rdbl/tests -vv
format:
	autopep8 -r --in-place .
	black . -l 79