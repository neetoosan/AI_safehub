"""Stylized and interactive form input components"""

import flet as ft
from config.settings import COLORS
from utils.responsive import ResponsiveConfig


def create_styled_text_field(
    label: str,
    responsive: ResponsiveConfig,
    hint_text: str = "",
    icon: str = None,
    password: bool = False,
    multiline: bool = False,
    input_filter=None,
    width: int = None,
    on_change=None,
    error_text: str = "",
):
    """
    Create a stylized text input field with better UX
    
    Args:
        label: Field label
        responsive: ResponsiveConfig instance
        hint_text: Placeholder text
        icon: Optional icon to display in the field
        password: Whether to hide input (password field)
        multiline: Whether to allow multiple lines
        input_filter: Input validation filter
        width: Field width
        on_change: Callback when value changes
        error_text: Error message to display
    
    Returns:
        ft.Container with styled text field
    """
    
    if width is None:
        width = responsive.input_width()
    
    # Text field with enhanced styling
    text_field = ft.TextField(
        label=label,
        hint_text=hint_text,
        password=password,
        multiline=multiline,
        input_filter=input_filter,
        width=width,
        height=50 if not multiline else None,
        min_lines=4 if multiline else None,
        max_lines=8 if multiline else None,
        bgcolor=ft.Colors.WHITE,
        border_color=COLORS["secondary"],
        border_radius=8,
        border_width=2,
        focused_border_color=COLORS["primary"],
        focused_bgcolor=ft.Colors.WHITE,
        content_padding=15,
        label_style=ft.TextStyle(
            color=COLORS["primary"],
            size=14,
            weight="bold",
        ),
        text_style=ft.TextStyle(
            size=14,
            color=COLORS["text"],
        ),
        hint_style=ft.TextStyle(
            color="#999",
            size=13,
        ),
        prefix_icon=icon,
        on_change=on_change,
    )
    
    # Error message display
    error_display = ft.Text(
        error_text,
        size=11,
        color=COLORS["critical"],
        visible=bool(error_text),
    )
    
    # Container with spacing
    return ft.Column(
        controls=[
            text_field,
            error_display,
        ],
        spacing=6,
        tight=True,
    ), text_field, error_display


def create_styled_dropdown(
    label: str,
    responsive: ResponsiveConfig,
    options: list,
    icon: str = None,
    width: int = None,
    on_change=None,
    error_text: str = "",
):
    """
    Create a stylized dropdown field with better UX
    
    Args:
        label: Field label
        responsive: ResponsiveConfig instance
        options: List of ft.dropdown.Option items
        icon: Optional icon
        width: Field width
        on_change: Callback when value changes
        error_text: Error message to display
    
    Returns:
        Tuple of (container, dropdown_control, error_display)
    """
    
    if width is None:
        width = responsive.input_width()
    
    # Dropdown with enhanced styling
    dropdown = ft.Dropdown(
        label=label,
        width=width,
        options=options,
        bgcolor=ft.Colors.WHITE,
        border_color=COLORS["secondary"],
        border_radius=8,
        border_width=2,
        filled=True,
        focused_border_color=COLORS["primary"],
        focused_bgcolor=ft.Colors.WHITE,
        content_padding=15,
        label_style=ft.TextStyle(
            color=COLORS["primary"],
            size=14,
            weight="bold",
        ),
        text_style=ft.TextStyle(
            size=14,
            color=COLORS["text"],
        ),
        on_change=on_change,
    )
    
    # Error message display
    error_display = ft.Text(
        error_text,
        size=11,
        color=COLORS["critical"],
        visible=bool(error_text),
    )
    
    # Container with spacing
    return ft.Column(
        controls=[
            dropdown,
            error_display,
        ],
        spacing=6,
        tight=True,
    ), dropdown, error_display


def create_styled_button(
    text: str,
    responsive: ResponsiveConfig,
    on_click=None,
    button_type: str = "primary",  # "primary", "secondary", "danger"
    width: int = None,
    icon: str = None,
    enabled: bool = True,
):
    """
    Create a stylized button with better UX
    
    Args:
        text: Button label
        responsive: ResponsiveConfig instance
        on_click: Click callback
        button_type: "primary", "secondary", or "danger"
        width: Button width
        icon: Optional icon
        enabled: Whether button is enabled
    
    Returns:
        ft.Button with styling
    """
    
    if width is None:
        width = responsive.button_width_flexible()
    
    # Determine colors based on button type
    color_map = {
        "primary": {
            "bg": COLORS["primary"],
            "text": ft.Colors.WHITE,
        },
        "secondary": {
            "bg": COLORS["secondary"],
            "text": ft.Colors.WHITE,
        },
        "danger": {
            "bg": COLORS["critical"],
            "text": ft.Colors.WHITE,
        },
    }
    
    colors = color_map.get(button_type, color_map["primary"])
    
    button = ft.Button(
        content=ft.Text(text, color=colors["text"]),
        width=width,
        height=responsive.button_height(),
        bgcolor=colors["bg"],
        color=colors["text"],
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            overlay_color=ft.Colors.WHITE,
            elevation=2,
        ),
        on_click=on_click if enabled else None,
        disabled=not enabled,
    )
    
    return button


def create_styled_form_section(
    title: str,
    responsive: ResponsiveConfig,
    controls: list,
    description: str = "",
):
    """
    Create a styled form section with title and description
    
    Args:
        title: Section title
        responsive: ResponsiveConfig instance
        controls: List of form controls
        description: Optional section description
    
    Returns:
        ft.Container with styled section
    """
    
    section_controls = [
        ft.Text(
            title,
            size=responsive.font_size_h2(),
            weight="bold",
            color=COLORS["primary"],
        ),
    ]
    
    if description:
        section_controls.append(
            ft.Text(
                description,
                size=responsive.font_size_small(),
                color="#666",
            )
        )
    
    section_controls.extend(controls)
    
    return ft.Container(
        content=ft.Column(
            controls=section_controls,
            spacing=responsive.margin_medium(),
        ),
        padding=20,
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        border=ft.Border(
            left=ft.BorderSide(2, COLORS["secondary"]),
        ),
        margin=ft.margin.only(bottom=20),
    )


def create_input_group(
    label: str,
    responsive: ResponsiveConfig,
    controls: list,
    spacing: int = None,
):
    """
    Create a group of inputs with shared styling
    
    Args:
        label: Group label
        responsive: ResponsiveConfig instance
        controls: List of input controls
        spacing: Custom spacing
    
    Returns:
        ft.Column with styled input group
    """
    
    if spacing is None:
        spacing = responsive.margin_small()
    
    return ft.Column(
        controls=[
            ft.Text(
                label,
                size=responsive.font_size_body(),
                weight="bold",
                color=COLORS["text"],
            ),
            ft.Column(
                controls=controls,
                spacing=spacing,
            ),
        ],
        spacing=10,
    )


def create_success_message(
    message: str,
    responsive: ResponsiveConfig,
):
    """
    Create a styled success message
    
    Args:
        message: Message text
        responsive: ResponsiveConfig instance
    
    Returns:
        ft.Container with styled success message
    """
    
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(ft.Icons.CHECK_CIRCLE, color=COLORS["success"], size=20),
                ft.Text(
                    message,
                    color=COLORS["success"],
                    size=responsive.font_size_body(),
                    weight="bold",
                ),
            ],
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=15,
        bgcolor=f"{COLORS['success']}15",
        border_radius=8,
        border=ft.Border(
            left=ft.BorderSide(3, COLORS["success"]),
        ),
    )


def create_error_message(
    message: str,
    responsive: ResponsiveConfig,
):
    """
    Create a styled error message
    
    Args:
        message: Message text
        responsive: ResponsiveConfig instance
    
    Returns:
        ft.Container with styled error message
    """
    
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(ft.Icons.ERROR, color=COLORS["critical"], size=20),
                ft.Text(
                    message,
                    color=COLORS["critical"],
                    size=responsive.font_size_body(),
                    weight="bold",
                ),
            ],
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=15,
        bgcolor=f"{COLORS['critical']}15",
        border_radius=8,
        border=ft.Border(
            left=ft.BorderSide(3, COLORS["critical"]),
        ),
    )


def create_warning_message(
    message: str,
    responsive: ResponsiveConfig,
):
    """
    Create a styled warning message
    
    Args:
        message: Message text
        responsive: ResponsiveConfig instance
    
    Returns:
        ft.Container with styled warning message
    """
    
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(ft.Icons.WARNING, color=COLORS["warning"], size=20),
                ft.Text(
                    message,
                    color=COLORS["warning"],
                    size=responsive.font_size_body(),
                ),
            ],
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=15,
        bgcolor=f"{COLORS['warning']}15",
        border_radius=8,
        border=ft.Border(
            left=ft.BorderSide(3, COLORS["warning"]),
        ),
    )
