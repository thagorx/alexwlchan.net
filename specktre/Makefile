ROOT = $(shell git rev-parse --show-toplevel)
SPECKTRE = $(ROOT)/specktre

$(SPECKTRE)/requirements.txt: $(SPECKTRE)/requirements.in
	docker run --rm --tty --volume $(SPECKTRE):/src micktwomey/pip-tools

docker_deps = \
	$(SPECKTRE)/requirements.txt \
	$(SPECKTRE)/Dockerfile

build-specktre: $(docker_deps)
	docker build --tag alexwlchan/specktre $(SPECKTRE)

.PHONY: build-specktre
