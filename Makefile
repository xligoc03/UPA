SRCS_DIR = src/
DEPS = requirements.txt

.PHONY: all check-pylint deps

all : deps check-pylint

check-pylint: $(SRCS_DIR)
	python3 -m pylint $(SRCS_DIR) --rcfile=pylintrc

deps: $(DEPS)
	pip3 install -r $(DEPS)

