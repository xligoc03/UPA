SRCS_DIR = src/
DEPS = requirements.txt

.PHONY: all check-pylint deps docker

all : deps docker check-pylint run

check-pylint: $(SRCS_DIR)
	python3 -m pylint $(SRCS_DIR) --rcfile=pylintrc

deps: $(DEPS)
	pip3 install -r $(DEPS)

docker:
	docker-compose up -d --build

run:
	make docker
	make deps
	export PYTHONPATH=$(shell pwd) && python3 src/__main__.py

