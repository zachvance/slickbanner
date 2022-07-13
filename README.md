<img src="https://github.com/zachvance/slickbanner/blob/main/examples/banner.png" alt="Banner" width="1000"/>

# SlickBanner

 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
 [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Generate a GitHub social banner, or other banner-style images for projects and social medias.

## Background
I've wanted to do this project for a while now, and I'm reminded every time I make a new repository public on GitHub -
I always try to add a social image to my project before making it public, and it always takes extra time in Photoshop to
create one (not a lot of time, but time none the less).

I figured using Python and utilizing the Pillow library would allow me to recreate what I've been doing in Photoshop.

## Usage
`python main.py [options]`

## Preset Gradient Colour Palettes
Below are gradient presets available through the palette argument. (Yes, some of the colour schemes and palette names
have been adapted and borrowed from Seaborn.)  

`lavender` 
<img src="https://github.com/zachvance/slickbanner/blob/main/examples/lavender.png" alt="lavender" width="1000"/>

`husl`  
<img src="https://github.com/zachvance/slickbanner/blob/main/examples/husl.png" alt="husl" width="1000"/>

`cotton_candy`  
<img src="https://github.com/zachvance/slickbanner/blob/main/examples/cotton_candy.png" alt="cotton_candy" width="1000"/>

`flare`  
<img src="https://github.com/zachvance/slickbanner/blob/main/examples/flare.png" alt="flare" width="1000"/>

`electric`  
<img src="https://github.com/zachvance/slickbanner/blob/main/examples/electric.png" alt="electric" width="1000"/>

`raspberry`  
<img src="https://github.com/zachvance/slickbanner/blob/main/examples/raspberry.png" alt="raspberry" width="1000"/>

`mint`  
<img src="https://github.com/zachvance/slickbanner/blob/main/examples/mint.png" alt="mint" width="1000"/>

## Todo
- Add option to supply your own arguments for a gradient, in lieu of a preset palette.
- Add the ability to load an image to use as the background instead of using a gradient.
- Add the ability to load an image to use as a tiled background.
- For loaded images: specify perspective tilting, and blur or tilt/shift blur, and/or image darken or lighten via an
alpha layer.
- Add option to change frame colour, or use a generated gradient.
- Add option to change font colour, or use a generated gradient.
- Add option for a drop shadow on the font.
