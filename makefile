# Variables
VENV           = ./venv
BIN            = $(VENV)/bin
VENV_PYTHON    = $(BIN)/python
SYSTEM_PYTHON  = $(or $(shell which python3), $(shell which python))
PYTHON         = $(or $(wildcard $(VENV_PYTHON)), $(SYSTEM_PYTHON))

init:
	rm -rf $(VENV)
	$(SYSTEM_PYTHON) -m venv $(VENV)
	#. $(BIN)/activate
	$(VENV_PYTHON) -m pip install --upgrade pip
	$(VENV_PYTHON) -m pip install -U setuptools wheel
	$(VENV_PYTHON) -m pip install -r requirements.txt

## Clean

clean:
	rm -rf .tox *.egg-info dis venv

.PHONY: clean
