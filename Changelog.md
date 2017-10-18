# Changelog #

## Limitations ##
- No names and keywords in coverage list yet (for better searching and finding)
- %, # and \ are not allowed as ascii-emoji input; $ is allowed but not recommended
- Performance?!
- No package options yet
- Composite emoji which are glued together with a ZWS are not working yet as utf8 input (shortnames are always working)

## Version 0.4 ##
18.10.2017
### Features ###
- Add support for (almost) all composite emoji consisting of 2 emoji
- Add support for inserting emoji with shortnames ```\emoji{:-)}``` or ```\emoji{:smile:}```
- Add a coverage list with all emoji and corresponding shortnames
- Update Python script to generate tex files to reflect these changes (shortnames via emojitwo)

## Version 0.3 ##
17.10.2017
### Features ###
- Add [emojitwo](https://github.com/EmojiTwo/emojitwo) support
- Add python script to generate emoji .pdf from twemoji, emojitwo or any other .svg emoji source
- Add (more) robust support for composite emoji (flags)
	- can handle a single composite emoji without breaking following spaces/commands in XeTeX/LuaTeX
- Code clean up (indents, comments, …)

## Version 0.2 ##
15.10.2017
### Features ###
- Add [twemoji](https://github.com/twitter/twemoji) support (twemoji as submodule, bash script to convert .svg files to .pdf)
- Add python script
- Add checks (for existenc/validity) for emoji images
- Add rudimentary support for composite emoji (flags)
## Version 0.1 ##
12.10.2017
### Features ###
- Change from utf8x to utf8 inputenc
## Original Fork ##
Fork of coloremoji.sty by [pavelkryukov](https://github.com/pavelkryukov/coloremoji.sty) (original coloremoji.sty by [alecjacobson](https://github.com/alecjacobson/coloremoji.sty))
### Features ###
- inserted utf-8 are printed as images in TeX
- works for pdflatex, xelatex and lualatex
### Limits ###
- nearly no error-checks
- uses utf8x inputenc
- does not support composite emoji (flags, skin color variations, …)