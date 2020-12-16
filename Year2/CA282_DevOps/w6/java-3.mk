javac = $(wildcard *.java)
javad = $(patsubst %.java, %.class, $(javac))

$(javad): $(javac)
	javac $(javac)

clean: $(javad)
	rm -f $(javad)

.PHONY: clean
