
help:
	@echo "test - run tests quickly with the default Python"
	@echo "clean-pyc - remove Python file artifacts"

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

test: clean-pyc
	CUDA_VISIBLE_DEVICES=""  pytest tests --disable-warnings

coverage: clean-pyc
	CUDA_VISIBLE_DEVICES="" coverage run -m --source prometeo pytest tests --disable-warnings
	coverage html --omit="tests/*,*/__init__.py"
	xdg-open  htmlcov/index.html

clean: clean-pyc
	rm -r htmlcov .coverage site

env-export:
	conda env export > environment.yml

develop:
	python setup.py develop

serve-docs:
	mkdocs serve

deploy-docs:
	git push
	mkdocs gh-deploy