test:
	pytest -v -s $(ARGS)

lint:
	flake8 .
