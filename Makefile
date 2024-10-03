######################################################################
# Settings
######################################################################
# Docker Compose command based on environment variable
DOCKER_ENV ?= dev

# Docker Compose command based on environment
ifeq ($(DOCKER_ENV),prod)
    DOCKER_COMPOSE := docker-compose -f docker-compose.prod.yml
else
    DOCKER_COMPOSE := docker-compose -f docker-compose.yml
endif

TECHSCREEN_CMD = $(DOCKER_COMPOSE) run --rm techscreen

######################################################################
# Instructions
######################################################################
.PHONY: help
help:
	@echo "Usage: make [options] <target>"
	@echo "Options: see 'make --help'"
	@echo "Targets:"
	@echo "  all: build, format, lint all projects"
	@echo "  diagrams: build the d2 diagrams"
	@echo "  format: format python code, d2 and jinja2 templates"
	@echo "  lint: run linters"
	@echo "  monitor-logs: tail all the dev logs"
	@echo "  pip-freeze: freeze packages to requirements.txt"
	@echo "  pip-upgrade: upgrade python packages"
	@echo "  share-env: make a env.zip to share with fellow devs"
	@echo "  start-dockers: start all dockers required for techscreen"
	@echo "  stop-dockers: stop all dockers"
	@echo "  tests: run pytest"
	@echo "  upgrade: upgrade docker images and rebuild"
	@echo "  watch: start watching techscreen for changes"

.PHONY: all
all: format lint

######################################################################
# Code Support
######################################################################
.PHONY: lint
lint: 
	$(TECHSCREEN_CMD) flake8 . | tee lint.out

.PHONY: black
black:
	$(TECHSCREEN_CMD) black --preview -q -l 79 .

.PHONY: isort
isort: 
	$(TECHSCREEN_CMD) isort .

.PHONY: djlint
djlint: 
	$(TECHSCREEN_CMD) sh -c 'rg --files -g "*.j2" | xargs -n1 djlint --reformat --profile=jinja'

.PHONY: d2fmt
d2fmt:
	$(TECHSCREEN_CMD) sh -c 'd2 fmt diagrams/*.d2'

.PHONY: format
format: isort black djlint d2fmt

.PHONY: upgrade
upgrade: 
	$(DOCKER_COMPOSE) down
	$(DOCKER_COMPOSE) pull
	$(DOCKER_COMPOSE) build --no-cache

.PHONY: pip-freeze
pip-freeze:
	$(TECHSCREEN_CMD) pip freeze > requirements.txt

.PHONY: pip-upgrade
pip-upgrade:
	$(TECHSCREEN_CMD) sh -c 'pip install --upgrade pip && pip install --upgrade -r requirements.txt'

######################################################################
# Dockers
######################################################################
.PHONY: start-dockers
start-dockers: 
	$(DOCKER_COMPOSE) up -d

.PHONY: stop-dockers
stop-dockers: 
	$(DOCKER_COMPOSE) down

.PHONY: monitor-logs
monitor-logs: 
	$(DOCKER_COMPOSE) logs -f

.PHONY: watch
watch:
	$(DOCKER_COMPOSE) up

.PHONY: tests
tests:
	$(TECHSCREEN_CMD) python -m pytest

.PHONY: share-env
share-env:
	$(TECHSCREEN_CMD) sh -c 'rm -f env.zip && zip -9r env.zip .env .env_files'

.PHONY: diagrams 
diagrams: 
	$(TECHSCREEN_CMD) sh -c 'rg --files -g "*.d2" | xargs -n1 -I {} d2 {} docs/{}.svg'

.PHONY: techscreen-shell
techscreen-shell:
	$(TECHSCREEN_CMD) /bin/bash

.PHONY: push-dockerhub
push-dockerhub:
	docker tag ai_engineer_tech_challenge-techscreen:latest robertmeta/techscreen
	docker push robertmeta/techscreen:latest


.PHONY: tf-plan
tf-plan:
	$(TECHSCREEN_CMD) sh -c 'terraform init'
	$(TECHSCREEN_CMD) sh -c 'terraform plan'

.PHONY: tf-apply
tf-apply:
	$(TECHSCREEN_CMD) sh -c 'terraform init'
	$(TECHSCREEN_CMD) sh -c 'terraform apply'
