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
### General
To create a basic banner with most default settings, run main.py and use the `-t` (title) flag, followed by your banner's
lettering. This will default to the Arial Bold typeface, with dimensions that match the recommended sizing for the
GitHub social image, and randomly select a background palette.
`python main.py -t project`

We can group words on multiple lines by enclosing each line in it's own quotes:  
`python main.py -t "this is" "my project"`

We can add subtitle lines in a similar fashion, though use of the -st (subtitle) flag:  
`python main.py -t "this is" "my project" -st "and this is subtitle line 1" "and this is subtitle line 2"`

### Text spacing
Our text is a little too close to the left border. We can adjust the text's _offset_ with the `-o` flag, which takes two
integers as arguments, representing the number of pixels to offset the text by on the x and y axis, respectively:  
`python main.py -t "this is" "my project" -st "and this is subtitle line 1" "and this is subtitle line 2" -o 30 0`

### Font/Typeface
There are a couple options for specifying the font - we can use the -fn flag by itself to specify the font name. This
will use the default fonts folder located at `C:\Windows\Fonts\`. You must use the font's file name (without the .ttf
extension), and not the display name used by Windows. You can get the file name by right-clicking on a font and checking
it's properties. In the example below, we are using `Comic Sans MS Bold`, which has a file name of `comicbd`.  
`python main.py -t projectname -fn comicbd`

If your font is housed in a different directory, we can override the default directory using the -fd (font directory)
flag:  
`python main.py -t projectname -fn comicbd -fd C:\\Path\\To\\Directory\\`

Or, we can specify an absolute path to our desired font with a single flag, -f (font):  
`python main.py -t projectname -f C:\\Path\\To\\Font\\font.ttf`

### Colour Palette
We can specify a colour palette with the -p flag:  
`python main.py -t project -p flare`

### Dimensions
And we can specify banner size with the -w (width) and -he (height) flags:  
`python main.py -t project -p flare -w 900 -he 400`

### Border and Edge Buffer
There are two flags for adjusting the framing: border thickness and edge buffer. Border thickness is how thick the
border/frame is in pixels. Edge buffer is the amount of pixels between the outer edge of the image canvas and the start
of the border.

The border thickness can be specified via the `-b` flag, and the edge buffer can be specified via the `-e` flag:  
`python main.py -t project -b 60 -e 60`

Setting either of these values to 0 allows you to create a banner without a border or an edge buffer.

### Alignments
Text alignment can be adjusted through the -a flag. There are 5 accepted values for the alignment argument: `top_left`,
`top_right`, `bottom_left`, `bottom_right`, and `center`.  
`python main.py -t project -a bottom_right`

### Output File
The output file name can be specified with the `-fn` flag, and the file type can be specified with the `-ft` flag. The
output file name will default to banner and the file type will default to png when no arguments are given.
`python main.py -t project -fn my_banner -ft jpg`

When the program saves the output, it's just using the .save() function from PIL, and thus the file type can be set to
any of the accepted file type options that PIL's .save() will take.

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
