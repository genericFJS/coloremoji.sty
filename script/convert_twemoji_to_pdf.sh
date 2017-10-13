#!/bin/bash
command -v inkscape >/dev/null 2>&1 || { echo >&2 "Inkscape required.  Aborting."; exit 1; }
cd "${0%/*}"
echo "Converting svg via inkscape to pdf:"
for f in ../twemoji/svg/*.svg
do
	filename=$(basename "$f");
	filename="${filename%.*}";
	echo "$f --export-pdf=../emoji_images/$filename.pdf" | DISPLAY= inkscape --shell;
done
echo "quit"
echo "done."