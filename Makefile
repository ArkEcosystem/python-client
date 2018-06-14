test:
	py.test -v -s $(ARGS)

lint:
	flake8 .
