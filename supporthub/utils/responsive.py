"""Responsive design utilities for mobile and desktop screens"""

import flet as ft
from config.settings import COLORS


class ResponsiveConfig:
    """Handles responsive design calculations based on screen size"""
    
    # Breakpoints (width in pixels)
    MOBILE_SMALL = 360
    MOBILE_NORMAL = 480
    TABLET = 768
    DESKTOP = 1024
    
    def __init__(self, page_width: int, page_height: int):
        """Initialize responsive config with page dimensions"""
        self.page_width = page_width
        self.page_height = page_height
        self.device_type = self._detect_device_type()
    
    def _detect_device_type(self) -> str:
        """Detect device type based on width"""
        if self.page_width < self.MOBILE_NORMAL:
            return "mobile_small"
        elif self.page_width < self.TABLET:
            return "mobile"
        elif self.page_width < self.DESKTOP:
            return "tablet"
        else:
            return "desktop"
    
    def is_mobile(self) -> bool:
        """Check if device is mobile"""
        return self.device_type in ["mobile_small", "mobile"]
    
    def is_tablet(self) -> bool:
        """Check if device is tablet"""
        return self.device_type == "tablet"
    
    def is_desktop(self) -> bool:
        """Check if device is desktop"""
        return self.device_type == "desktop"
    
    # ===== FONT SIZES =====
    
    def font_size_h1(self) -> int:
        """Main heading (Page title)"""
        if self.device_type == "mobile_small":
            return 28
        elif self.device_type == "mobile":
            return 32
        elif self.device_type == "tablet":
            return 36
        else:
            return 42
    
    def font_size_h2(self) -> int:
        """Section heading"""
        if self.device_type == "mobile_small":
            return 18
        elif self.device_type == "mobile":
            return 20
        elif self.device_type == "tablet":
            return 24
        else:
            return 28
    
    def font_size_h3(self) -> int:
        """Subsection heading"""
        if self.device_type == "mobile_small":
            return 14
        elif self.device_type == "mobile":
            return 16
        else:
            return 18
    
    def font_size_body(self) -> int:
        """Body text"""
        return 12 if self.device_type == "mobile_small" else 14
    
    def font_size_small(self) -> int:
        """Small text (hints, labels)"""
        return 10 if self.device_type == "mobile_small" else 11
    
    def font_size_caption(self) -> int:
        """Caption/extra small text"""
        return 8 if self.device_type == "mobile_small" else 10
    
    # ===== SPACING =====
    
    def padding_large(self) -> int:
        """Large padding for containers"""
        if self.device_type == "mobile_small":
            return 16
        elif self.device_type == "mobile":
            return 20
        elif self.device_type == "tablet":
            return 24
        else:
            return 30
    
    def padding_medium(self) -> int:
        """Medium padding"""
        if self.device_type == "mobile_small":
            return 12
        elif self.device_type == "mobile":
            return 15
        else:
            return 20
    
    def padding_small(self) -> int:
        """Small padding"""
        if self.device_type == "mobile_small":
            return 8
        else:
            return 10
    
    def margin_large(self) -> int:
        """Large margin"""
        if self.device_type == "mobile_small":
            return 12
        elif self.device_type == "mobile":
            return 15
        else:
            return 20
    
    def margin_medium(self) -> int:
        """Medium margin"""
        if self.device_type == "mobile_small":
            return 8
        else:
            return 10
    
    def margin_small(self) -> int:
        """Small margin"""
        if self.device_type == "mobile_small":
            return 4
        elif self.device_type == "mobile":
            return 6
        else:
            return 8
    
    def spacing_vertical(self) -> int:
        """Vertical spacing between elements"""
        if self.device_type == "mobile_small":
            return 12
        elif self.device_type == "mobile":
            return 15
        else:
            return 20
    
    def spacing_horizontal(self) -> int:
        """Horizontal spacing between elements"""
        if self.device_type == "mobile_small":
            return 8
        elif self.device_type == "mobile":
            return 10
        else:
            return 15
    
    # ===== SIZES =====
    
    def input_width(self) -> int:
        """Input field width"""
        if self.device_type == "mobile_small":
            return self.page_width - (self.padding_large() * 2)
        elif self.device_type == "mobile":
            return 300
        elif self.device_type == "tablet":
            return 400
        else:
            return 450
    
    def button_width(self) -> int:
        """Button width"""
        if self.device_type == "mobile_small":
            return int(self.page_width - (self.padding_large() * 2))
        elif self.device_type == "mobile":
            return 300
        elif self.device_type == "tablet":
            return 350
        else:
            return 400
    
    def button_width_flexible(self) -> int:
        """Flexible button width that scales with page"""
        return int(self.page_width - (self.padding_large() * 2))
    
    def button_height(self) -> int:
        """Button height"""
        if self.device_type == "mobile_small":
            return 45
        else:
            return 50
    
    def icon_size(self) -> int:
        """Icon size"""
        if self.device_type == "mobile_small":
            return 60
        elif self.device_type == "mobile":
            return 70
        elif self.device_type == "tablet":
            return 80
        else:
            return 80
    
    def card_width(self) -> int:
        """Card width"""
        if self.device_type == "mobile_small":
            return self.page_width - (self.padding_large() * 2)
        elif self.device_type == "mobile":
            return self.page_width - 20
        elif self.device_type == "tablet":
            return (self.page_width - 30) / 2
        else:
            return 300
    
    def card_height(self) -> int:
        """Card height"""
        if self.device_type == "mobile_small":
            return 120
        elif self.device_type == "mobile":
            return 140
        else:
            return 160
    
    def border_radius(self) -> int:
        """Border radius for UI elements"""
        return 6 if self.device_type == "mobile_small" else 8
    
    # ===== COLUMN/ROW LAYOUT =====
    
    def form_column_spacing(self) -> int:
        """Spacing between form fields"""
        if self.device_type == "mobile_small":
            return 12
        else:
            return 15
    
    def text_field_height(self) -> int:
        """Text field height"""
        if self.device_type == "mobile_small":
            return 45
        else:
            return 50
    
    def text_field_multiline_min_lines(self) -> int:
        """Multiline text field minimum lines"""
        if self.device_type == "mobile_small":
            return 4
        else:
            return 5
    
    def text_field_multiline_max_lines(self) -> int:
        """Multiline text field maximum lines"""
        if self.device_type == "mobile_small":
            return 8
        else:
            return 10
    
    # ===== RESPONSIVE ROW LAYOUT =====
    
    def get_row_columns(self) -> int:
        """Get number of columns for responsive grid"""
        if self.device_type == "mobile_small":
            return 1
        elif self.device_type == "mobile":
            return 1
        elif self.device_type == "tablet":
            return 2
        else:
            return 3
    
    def get_stat_card_width(self) -> int:
        """Get stat card width for dashboard"""
        if self.device_type == "mobile_small":
            return self.page_width - (self.padding_large() * 2)
        elif self.device_type == "mobile":
            return self.page_width - 20
        elif self.device_type == "tablet":
            return (self.page_width - 30) / 2
        else:
            return 200


def get_responsive_config(page: ft.Page) -> ResponsiveConfig:
    """Get responsive configuration from page"""
    return ResponsiveConfig(int(page.window_width), int(page.window_height))


# ===== HELPER FUNCTIONS FOR COMMON PATTERNS =====

def get_main_padding(responsive: ResponsiveConfig) -> int:
    """Get main container padding"""
    return responsive.padding_large()


def get_form_spacing(responsive: ResponsiveConfig) -> int:
    """Get spacing between form elements"""
    return responsive.form_column_spacing()


def create_responsive_container(
    content,
    responsive: ResponsiveConfig,
    bgcolor=None,
    padding=None,
    expand=True
) -> ft.Container:
    """Create a responsive container"""
    if bgcolor is None:
        bgcolor = COLORS["background"]
    if padding is None:
        padding = responsive.padding_large()
    
    return ft.Container(
        content=content,
        bgcolor=bgcolor,
        padding=padding,
        expand=expand,
    )


def create_responsive_button(
    text: str,
    on_click,
    responsive: ResponsiveConfig,
    bgcolor=None,
    text_color=None,
) -> ft.Button:
    """Create a responsive button"""
    if bgcolor is None:
        bgcolor = COLORS["primary"]
    if text_color is None:
        text_color = ft.Colors.WHITE
    
    return ft.Button(
        text=text,
        color=text_color,
        width=responsive.button_width(),
        height=responsive.button_height(),
        bgcolor=bgcolor,
        on_click=on_click,
    )


def create_responsive_text(
    text: str,
    responsive: ResponsiveConfig,
    size_type: str = "body",
    weight: str = "normal",
    color: str = None,
    text_align=None,
) -> ft.Text:
    """Create responsive text with size based on device"""
    if color is None:
        color = COLORS["text"]
    
    size_map = {
        "h1": responsive.font_size_h1(),
        "h2": responsive.font_size_h2(),
        "h3": responsive.font_size_h3(),
        "body": responsive.font_size_body(),
        "small": responsive.font_size_small(),
        "caption": responsive.font_size_caption(),
    }
    
    size = size_map.get(size_type, responsive.font_size_body())
    
    return ft.Text(
        text,
        size=size,
        weight=weight,
        color=color,
        text_align=text_align,
    )
