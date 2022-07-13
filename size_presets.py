SIZE_PRESETS = {}


class SizePreset:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height


def load_size_presets():
    default = SizePreset("default", 900, 200)
    github_social = SizePreset("github_social", 1280, 640)
    github_banner = SizePreset("github_banner", 1280, 320)

    SIZE_PRESETS["default"] = default
    SIZE_PRESETS["github_social"] = github_social
    SIZE_PRESETS["github_banner"] = github_banner