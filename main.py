import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps
import argparse
from palettes import PALETTES, load_palette_presets
from size_presets import SIZE_PRESETS, load_size_presets


class Menu:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="An image generator for creating banners with text for projects and social media."
        )
        self.parser.add_argument(
            "-w",
            "--width",
            default=1000,
            type=int,
            help="The overall width of the banner.",
        )
        self.parser.add_argument(
            "-he",
            "--height",
            default=300,
            type=int,
            help="The overall height of the banner.",
        )
        self.parser.add_argument(
            "-t",
            "--title",
            nargs="+",
            default=[],
            type=str,
            help="The primary title text. Separate into multiple lines by encapsulating each line in quotes.",
        )
        self.parser.add_argument(
            "-st",
            "--subtitle",
            nargs="+",
            default=[],
            type=str,
            help="The subtitle text. Separate into multiple lines by encapsulating each line in quotes.",
        )
        self.parser.add_argument(
            "-p",
            "--palette",
            default="",
            type=str,
            help="The name of the palette to use.",
        )
        self.parser.add_argument(
            "-e",
            "--edge_buffer_value",
            default=60,
            type=int,
            help="The value in pixels between the edge of the banner and the start of the border.",
        )
        self.parser.add_argument(
            "-b",
            "--border_thickness_value",
            default=20,
            type=int,
            help="The thickness of the border in pixels.",
        )
        self.parser.add_argument(
            "-a",
            "--alignment",
            default="top_left",
            type=str,
            help="The text alignment.",
        )
        self.parser.add_argument(
            "-va",
            "--vertical_alignment",
            default="",
            type=str,
            help="The text's vertical alignment.",
        )
        self.parser.add_argument(
            "-fi",
            "--file_name",
            default="banner",
            type=str,
            help="The output file name for the banner.",
        )
        self.parser.add_argument(
            "-ft",
            "--file_type",
            default="png",
            type=str,
            help="The output file type for the banner.",
        )
        self.parser.add_argument(
            "-o",
            "--font_offset",
            nargs=2,
            default=[0, 0],
            type=int,
            help="The buffer values, in pixels, for offsetting the x and y of the font.",
        )
        self.parser.add_argument(
            "-ts",
            "--title_size",
            default=120,
            type=int,
            help="The size of the font for the primary titles.",
        )
        self.parser.add_argument(
            "-sts",
            "--subtitle_size",
            default=70,
            type=int,
            help="The size of the font for the subtitles.",
        )
        self.parser.add_argument(
            "-fd",
            "--font_directory",
            default="C:\\Windows\\Fonts\\",
            type=str,
            help="The font directory to use.",
        )
        self.parser.add_argument(
            "-fn",
            "--font_name",
            default="arialbd",
            type=str,
            help="The name of the ttf file to use without an extension.",
        )
        self.parser.add_argument(
            "-f",
            "--font",
            type=str,
            help="The absolute path to the .tff file to use. Overrides font_directory and font_name.",
        )
        self.parser.add_argument(
            "-pr",
            "--preset",
            type=str,
            help="Use a preset for the banner size. default | github_social | github_banner",
        )


class Banner:
    def __init__(
        self,
        width=0,
        height=0,
        edge_buffer_value: int = 0,
        border_thickness_value: int = 0,
        alignment: str = "top_left",
    ) -> None:
        self.preset = None
        self.width = width
        self.height = height
        self.dimensions = (self.width, self.height)
        self.border_thickness_value = border_thickness_value
        self.border_thickness = tuple([border_thickness_value] * 4)
        self.edge_buffer_value = edge_buffer_value
        self.edge_buffer = tuple([edge_buffer_value] * 4)
        self.combined_values = border_thickness_value + edge_buffer_value
        self.palette = None
        self.frame_alpha = None
        self.background = None
        self.title: list = []
        self.title_size: int = 100
        self.subtitle: list = []
        self.subtitle_size: int = 50
        self.font = None
        self.font_offset = (0, 0)
        self.composite = None
        self.inner_top_left = (self.combined_values, self.combined_values)
        self.inner_top_right = (self.width - self.combined_values, self.combined_values)
        self.inner_bottom_left = (
            self.combined_values,
            self.height - self.combined_values,
        )
        self.inner_bottom_right = (
            self.width - self.combined_values,
            self.height - self.combined_values,
        )
        self.alignment = alignment
        self.vertical_alignment = None

    def create_background(self):
        array = get_gradient_3d(
            width=self.width, height=self.height, palette=self.palette
        )
        bg = Image.fromarray(np.uint8(array))
        alpha = self.create_frame_alpha()
        frame = ImageOps.invert(self.create_frame_alpha())

        bg.putalpha(alpha)
        bg.paste(frame, (0, 0), frame)
        self.background = bg

    def load_background(
        self, perspective=False, blur=False, tilt_shift=False, darken=False
    ):
        pass

    def create_frame_alpha(self):
        img = Image.new(
            "L",
            (self.width - (self.combined_values * 2), self.height - (self.combined_values * 2)),
            color="white",
        )

        color = "black"
        alpha = ImageOps.expand(img, border=self.border_thickness, fill=color)

        color = "white"
        alpha = ImageOps.expand(alpha, border=self.edge_buffer, fill=color)
        return alpha

    def add_text(self):
        li = self.zip_titles_with_size()

        if self.alignment == "center":
            y = self.inner_top_left[1] + self.font_offset[1]
            for item in li:
                d = ImageDraw.Draw(self.background)
                fnt = ImageFont.truetype(self.font, item[1])
                text_box = d.textbbox(xy=(0, 0), text=item[0], font=fnt)
                text_length = text_box[2]
                text_height = text_box[3]

                x = (self.width / 2) - (text_length / 2)

                if self.vertical_alignment == "center":
                    y = (self.height / 2) - (text_height / 2) - self.font_offset[1]

                d.text((x, y), item[0], fill=(255, 255, 255), font=fnt)
                y += text_height + 15

        if self.alignment == "top" or self.alignment == "top_left":
            x = self.inner_top_left[0] + self.font_offset[0]
            y = self.inner_top_left[1] + self.font_offset[1]
            for item in li:
                d = ImageDraw.Draw(self.background)
                fnt = ImageFont.truetype(self.font, item[1])
                text_box = d.textbbox(xy=(0, 0), text=item[0], font=fnt)
                text_height = text_box[3]

                d.text((x, y), item[0], fill=(255, 255, 255), font=fnt)
                y += text_height + 15

        if self.alignment == "bottom" or self.alignment == "bottom_left":
            x = self.inner_bottom_left[0] + self.font_offset[0]
            y = self.inner_bottom_left[1] - self.font_offset[1]
            for item in li[::-1]:
                d = ImageDraw.Draw(self.background)
                fnt = ImageFont.truetype(self.font, item[1])
                text_box = d.textbbox(xy=(0, 0), text=item[0], font=fnt)
                text_height = text_box[3]
                y = y - text_height
                d.text((x, y), item[0], fill=(255, 255, 255), font=fnt)
                y -= 15

        if self.alignment == "bottom_right":
            y = self.inner_bottom_right[1] + self.font_offset[1]
            for item in li[::-1]:
                x = self.inner_bottom_right[0] - self.font_offset[0]
                d = ImageDraw.Draw(self.background)
                fnt = ImageFont.truetype(self.font, item[1])
                text_box = d.textbbox(xy=(0, 0), text=item[0], font=fnt)
                text_length = text_box[2]
                text_height = text_box[3]
                x -= text_length
                y = y - text_height
                d.text((x, y), item[0], fill=(255, 255, 255), font=fnt)
                y -= 15

        if self.alignment == "top_right":
            y = self.inner_top_right[1] + self.font_offset[1]
            for item in li:
                x = self.inner_top_right[0] - self.font_offset[0]
                d = ImageDraw.Draw(self.background)
                fnt = ImageFont.truetype(self.font, item[1])
                text_box = d.textbbox(xy=(0, 0), text=item[0], font=fnt)
                text_length = text_box[2]
                text_height = text_box[3]
                x -= text_length
                d.text((x, y), item[0], fill=(255, 255, 255), font=fnt)
                y += text_height + 15

        self.composite = self.background

    def zip_titles_with_size(self) -> list:
        l1 = []
        for line in self.title:
            l1.append(self.title_size)
        l2 = []
        for line in self.subtitle:
            l2.append(self.subtitle_size)
        sizes = l1 + l2
        text = self.title + self.subtitle
        zipped = list(map(list, zip(text, sizes)))
        return zipped

    def save(self, file_name):
        self.composite.save(file_name)


# Gradients code modified from: https://note.nkmk.me/en/python-numpy-generate-gradation-image/
def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T


def get_gradient_3d(
    width,
    height,
    start_list=None,
    stop_list=None,
    is_horizontal_list=None,
    palette=None,
):
    if palette:
        result = np.zeros((height, width, len(palette.start_list)), dtype=float)

        for i, (start, stop, is_horizontal) in enumerate(
            zip(palette.start_list, palette.stop_list, palette.is_horizontal_list)
        ):
            result[:, :, i] = get_gradient_2d(start, stop, width, height, is_horizontal)
    else:
        result = np.zeros((height, width, len(start_list)), dtype=float)

        for i, (start, stop, is_horizontal) in enumerate(
            zip(start_list, stop_list, is_horizontal_list)
        ):
            result[:, :, i] = get_gradient_2d(start, stop, width, height, is_horizontal)

    return result


def main():

    load_palette_presets()
    load_size_presets()

    m = Menu()
    args = m.parser.parse_args()

    # Other possibility is C:\\Users\\{User}\\AppData\\Local\\Microsoft\\Windows\\Fonts
    font_directory = args.font_directory
    font_name = args.font_name

    if args.font:
        font = args.font
    else:
        font = f"{font_directory}{font_name}.ttf"

    ebv = args.edge_buffer_value
    btv = args.border_thickness_value

    if args.preset:
        preset = SIZE_PRESETS[args.preset]
        width = preset.width
        height = preset.height
    else:
        width = args.width
        height = args.height

    if args.palette:
        p = PALETTES[args.palette.lower()]
    else:
        p = np.random.choice(list(PALETTES.values()))

    banner = Banner(width=width, height=height, edge_buffer_value=ebv, border_thickness_value=btv)

    banner.alignment = args.alignment
    banner.vertical_alignment = args.vertical_alignment
    banner.font = font
    banner.font_offset = tuple(args.font_offset)
    banner.title = args.title
    banner.subtitle = args.subtitle
    banner.title_size = args.title_size
    banner.subtitle_size = args.subtitle_size
    banner.palette = p

    banner.create_background()
    banner.add_text()
    banner.save(f"{args.file_name}.{args.file_type}")


if __name__ == "__main__":
    main()
