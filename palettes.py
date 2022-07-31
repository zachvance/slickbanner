PALETTES = {}


class Palette:
    def __init__(self, name, start_list, stop_list, is_horizontal_list):
        self.name = name
        self.start_list = start_list
        self.stop_list = stop_list
        self.is_horizontal_list = is_horizontal_list


def load_palette_presets():
    lavender = Palette("lavender", (130, 130, 255), (150, 100, 200), (True, False, False))
    husl = Palette("husl", (225, 225, 75), (75, 75, 200), (True, False, False))
    cotton_candy = Palette(
        "cotton_candy", (200, 200, 200), (0, 100, 200), (True, False, False)
    )
    flare = Palette("flare", (200, 50, 20), (55, 5, 70), (True, False, False, False))
    electric = Palette("electric", (255, 50, 20), (50, 5, 255), (True, False, False))
    raspberry = Palette("raspberry", (120, 5, 10), (10, 5, 120), (True, False, False))
    mint = Palette("mint", (0, 190, 100), (0, 190, 190), (True, False, False))
    blueberry = Palette("blueberry", (40, 30, 80), (100, 40, 230), (False, True, False))

    PALETTES["lavender"] = lavender
    PALETTES["husl"] = husl
    PALETTES["cotton_candy"] = cotton_candy
    PALETTES["flare"] = flare
    PALETTES["electric"] = electric
    PALETTES["raspberry"] = raspberry
    PALETTES["mint"] = mint
    PALETTES["blueberry"] = blueberry
