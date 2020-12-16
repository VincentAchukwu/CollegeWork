dst = $(HOME)/local/bin
src = $(wildcard [a-z]*)

install: $(dst)
install: $(addprefix $(dst)/, $(src))

$(dst)/%: %
	install -v -m 0555 $< $@

$(dst):
	mkdir -vp $@

.PHONY: install
