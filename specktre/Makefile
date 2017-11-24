ROOT = $(shell git rev-parse --show-toplevel)
SPECKTRE = $(ROOT)/specktre

$(SPECKTRE)/requirements.txt: $(SPECKTRE)/requirements.in
	docker run --rm --tty --volume $(SPECKTRE):/src micktwomey/pip-tools
