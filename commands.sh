#pdflatex --shell-escape main; 
#biber  main; 
#pdflatex --shell-escape main; 
#pdflatex --shell-escape main


pdflatex --shell-escape -draftmode main
biber  main; 
#makeindex file.idx # if needed
#makeindex -s style.gls ...# for glossary if needed
pdflatex --shell-escape main
pdflatex --shell-escape main
