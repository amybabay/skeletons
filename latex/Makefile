# LaTeX Makefile
#
# For the purposes of making LaTeX documents.
#
# Runs pdflatex once, then bibtex, then pdflatex twice to get
# all the references to work out.
#

LATEX=pdflatex
BIB=bibtex

all: template

template:
	$(LATEX) template.tex
#	$(BIB) template.aux
#	$(LATEX) template.tex
#	$(LATEX) template.tex
	open template.pdf

clean:
	rm -f *.aux *.bbl *.blg *.log *.out
