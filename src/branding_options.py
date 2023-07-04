```python
class BrandingOptions:
    def __init__(self):
        self.options = {
            "logo": None,
            "color_scheme": None,
            "banner": None,
            "custom_url": None
        }

    def set_logo(self, logo):
        self.options["logo"] = logo

    def set_color_scheme(self, color_scheme):
        self.options["color_scheme"] = color_scheme

    def set_banner(self, banner):
        self.options["banner"] = banner

    def set_custom_url(self, custom_url):
        self.options["custom_url"] = custom_url

    def get_branding_options(self):
        return self.options
```