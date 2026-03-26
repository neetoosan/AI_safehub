"""Who Are You Screen - Choose between Reporter or Admin"""

import flet as ft
from config.settings import COLORS
from utils.responsive import ResponsiveConfig, create_responsive_text


def create_who_are_you_screen(on_reporter=None, on_admin=None, responsive=None):
    """Create screen where user chooses between reporter or admin"""
    
    if responsive is None:
        responsive = ResponsiveConfig(360, 740)
    
    def handle_reporter(e):
        if on_reporter:
            on_reporter()
    
    def handle_admin(e):
        if on_admin:
            on_admin()
    
    card_width = responsive.card_width() if isinstance(responsive.card_width(), (int, float)) else 280
    card_height = responsive.card_height()
    icon_size = responsive.font_size_h2() + 20

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(height=responsive.spacing_vertical()),
                
                # Header
                create_responsive_text(
                    "Welcome to AI SupportHub",
                    responsive,
                    size_type="h1",
                    weight="bold",
                    color=COLORS["primary"],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=responsive.margin_small()),
                
                create_responsive_text(
                    "Who are you?",
                    responsive,
                    size_type="h2",
                    color=COLORS["text"],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Reporter Card
                ft.GestureDetector(
                    on_tap=handle_reporter,
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Icon(
                                    icon=ft.Icons.PERSON,
                                    size=icon_size,
                                    color=COLORS["primary"],
                                ),
                                ft.Container(height=responsive.margin_medium()),
                                create_responsive_text(
                                    "I'm a Reporter",
                                    responsive,
                                    size_type="h2",
                                    weight="bold",
                                    color=COLORS["primary"],
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                ft.Container(height=responsive.margin_small()),
                                create_responsive_text(
                                    "Report an incident anonymously",
                                    responsive,
                                    size_type="body",
                                    color=COLORS["text"],
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0,
                        ),
                        width=card_width,
                        height=card_height,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=responsive.border_radius(),
                        padding=responsive.padding_medium(),
                        shadow=ft.BoxShadow(
                            blur_radius=8,
                            color="#00000015",
                        ),
                    ),
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Admin Card
                ft.GestureDetector(
                    on_tap=handle_admin,
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Icon(
                                    icon=ft.Icons.ADMIN_PANEL_SETTINGS,
                                    size=icon_size,
                                    color=COLORS["critical"],
                                ),
                                ft.Container(height=responsive.margin_medium()),
                                create_responsive_text(
                                    "I'm an Admin",
                                    responsive,
                                    size_type="h2",
                                    weight="bold",
                                    color=COLORS["critical"],
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                ft.Container(height=responsive.margin_small()),
                                create_responsive_text(
                                    "Manage and review reports",
                                    responsive,
                                    size_type="body",
                                    color=COLORS["text"],
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0,
                        ),
                        width=card_width,
                        height=card_height,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=responsive.border_radius(),
                        padding=responsive.padding_medium(),
                        shadow=ft.BoxShadow(
                            blur_radius=8,
                            color="#00000015",
                        ),
                    ),
                ),
                
                ft.Container(expand=True),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        ),
        bgcolor=COLORS["background"],
        padding=responsive.padding_large(),
        expand=True,
    )
