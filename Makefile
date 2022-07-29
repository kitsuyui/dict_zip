.PHONY: lint
lint: flake8 mypy check_import_order check_format

.PHONY: test
test: pytest test_types

.PHONY: format
format: isort black

.PHONY: generate_type_stub
generate_type_stub: generate_type_stub_pre format

.PHONY: generate_type_stub_pre
generate_type_stub_pre:
	python ./generate_type_stub.py > dict_zip/__init__.pyi

.PHONY: isort
isort:
	isort dict_zip tests

.PHONY: black
black:
	black dict_zip tests

.PHONY: flake8
flake8:
	flake8 dict_zip tests

.PHONY: mypy
mypy:
	mypy dict_zip tests

.PHONY: check_import_order
check_import_order:
	isort --check-only --diff dict_zip tests

.PHONY: check_format
check_format:
	black --check dict_zip tests

.PHONY: test_types
test_types:
	mypy tests/test_types.py

.PHONY: pytest
pytest:
	pytest --cov=dict_zip tests --doctest-modules --cov-report=xml

.PHONY: build
build:
	python3 -m build .

.PHONY: clean
clean:
	rm -rf dict_zip.egg-info dist

.PHONY: test_install
test_install: clean build
	./scripts/test_install.sh
