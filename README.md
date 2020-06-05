coloremoji.sty
==============
Style package for directly including color emojis in latex documents

[Related blog entry](http://www.alecjacobson.com/weblog/?p=4018)

## Installation

    TEXMFHOME=`kpsewhich -var-value TEXMFHOME`
    mkdir -p ${TEXMFHOME}/tex/latex/local
    cd ${TEXMFHOME}/tex/latex/local
    git clone https://github.com/genericFJS/coloremoji.sty.git

You'll also need to generate emoji images. Grab one of
[twemoji](https://github.com/twitter/twemoji) ([CC-BY](https://github.com/twitter/twemoji#attribution-requirements)) or
[emojitwo](https://github.com/EmojiTwo/emojitwo) ([CC-BY](https://github.com/EmojiTwo/emojitwo/blob/master/LICENSE.md)); both contain SVG emojis. The
`convert_svg-emoji_to_pdf.py` script in the `script/` directory can convert
these to PDF format for use with this package; it takes a path as an argument.
For instance using twemoji:
    1. `git clone https://github.com/twitter/twemoji.git`
    2. `python3 convert_svg-emoji_to_pdf.py ../twemoji/svg`

The script requires `cairo` installed locally (this is available in `brew` and
other package managers), as well as the `cairosvg` Python library, which can be
installed via `pip`.

## Examples

The following LaTeX code:

    \documentclass{article}
    \usepackage{coloremoji}
    \begin{document}
    Hello, 🌎.
    \end{document}

produces something like:

![Hello, world.](http://alecjacobson.com/weblog/media/hello-world-emoji.png)

You can even use emojis in math. The following LaTeX code:

    \[
    🐊^{🐊^{🐊}} = ∫_{🎃} 🙊 \ d🍀
    \]

produces something like:

![Emojis in math
mode.](http://alecjacobson.com/weblog/media/alligator-power-integral-jack-o-lantern.png)

## Known issues

This style sheet creates a PDF where each emoji is actually an embedded _image_
rather than a character using the [Apple Color Emoji
typeface](http://en.wikipedia.org/wiki/Apple_Color_Emoji). This means you won't
be able to correctly copy and paste emjois from the resulting .pdf files.

The encoding of the `.tex` must support emoji's, that is unicode characters. So switch your encoding to something like UTF-8.
